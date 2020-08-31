"""
Actualizar la base de datos.
"""

from datetime import datetime, timedelta
from math import ceil
from numpy import nan
from pandas import pandas as pd, DataFrame
from psycopg2 import connect
from sqlalchemy import create_engine, types
from TpsParse.Tps.TpsFile import TpsFile
from Utils.create_keys import create_keys
from Utils.keys import dicts
from Utils.sql import select
from Utils.tps_path import PATH
from Utils.truncate_db import truncate
from Utils.update_order import file_list
from Website.settings import DATABASES

COL_TYPES = {
    'Byte': types.Integer,
    'SignedShort': types.Integer,
    'UnsignedShort': types.Integer,
    'Date': types.Date,
    'Time': types.Time,
    'SignedLong': types.Integer,
    'UnsignedLong': types.Integer,
    'Float': types.Float,
    'Double': types.Float,
    'Bcd': types.Float,
    'FixedLengthString': types.String,
    'ZeroTerminatedString': types.String,
    'PascalString': types.String,
    'Group': types.String,
}

NAME = DATABASES['default']['NAME']
USER = DATABASES['default']['USER']
PASSWORD = DATABASES['default']['PASSWORD']
HOST = DATABASES['default']['HOST']
PORT = DATABASES['default']['PORT']
URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'
ENGINE = create_engine(URI)

# Columnas que deberian ser de tipo datetime
DATE_NAME_LIST = ('fec', 'periodo')


def format_date(df, cols_and_types):
    """
    Formatear la fecha de clarion (cantidad de días desde 28/12/1800)
    """
    date_columns = [c_name for c_name, c_type in cols_and_types
                    if c_name.startswith(DATE_NAME_LIST) and
                    c_type == 'SignedLong']

    for col in df[date_columns]:
        df[col] = datetime(1800, 12, 28) + df[col].map(timedelta)
        df.loc[df[col] == '1800-12-28', col] = None


def parse_data(file):
    """
    Procesar el tps con el parser para poder obtener los datos
    """
    cols_and_types = []
    columns = []
    records = []
    tps = TpsFile(file)
    for definition in tps.get_table_definitions():
        # Obtener campos
        for field in definition.fields:
            column = field.field_name.split(':')[1].lower()
            col_and_type = (field.field_name.split(':')[1].lower(), field.type)
            if column not in columns:
                columns.append(column)
                cols_and_types.append(col_and_type)
        # Obtener registros.
        for record in tps.get_data_records(definition):
            records.append([r.strip().title() if isinstance(r, str) else r
                            for r in record.values])

    # Crear una tabla que una las columnas con los registros para formar un DF
    table = []
    for record in records:
        dic = {}
        for col, rec in zip(columns, record):
            dic[col] = rec
        table.append(dic)

    df = pd.DataFrame(table, columns=columns)

    # Formatear los campos de tipo date.
    format_date(df, cols_and_types)

    # Reemplazar los campos vacíos con None.
    df.replace(to_replace='', value=nan, inplace=True)
    df.replace(to_replace=0, value=None, inplace=True)

    # Borrar los registros que tengan todos valores nulos.
    df.dropna(axis='index', how='all', inplace=True)

    # Eliminar registros duplicados.
    df.drop_duplicates(keep='last', inplace=True)

    return cols_and_types, df


def add_data(cols, df, file_name):
    """
    Agregar los datos del DF a la BD
    """
    # Machear tipos de datos
    dtypes = {c_name: COL_TYPES[c_type] for c_name, c_type in cols}
    # Agregar los datos a la BD
    df.to_sql(file_name, ENGINE, if_exists='append', index=False, dtype=dtypes)


def update_col_provincia(df):
    """
    Cambiar la descripcion de la provincia por el codigo de provincia.
    """
    with connect(URI) as connection:
        query = 'SELECT nro_provincia, descripcion FROM provincias'
        table = DataFrame(select(connection, query),
                          columns=('nro_provincia', 'descripcion'))
        prov = {nombre: nro for nombre, nro in
                zip(table.descripcion, table.nro_provincia)}
        df['provincia'] = df.provincia.map(prov)
    connection.close()


def update_col_localidad(df):
    """
    Cambiar la descripcion de la localidad por el codigo de localidad.
    """
    with connect(URI) as connection:
        query = 'SELECT codigo, descripcion FROM localidad'
        table = DataFrame(select(connection, query),
                          columns=('codigo', 'descripcion'))
        loc = {nombre: nro for nombre, nro in
               zip(table.descripcion, table.codigo)}
        df['localidad'] = df.localidad.map(loc)
    connection.close()


def update_col_banc(df):
    """
    Cambiar el numero de banco por el nuevo id.
    """
    with connect(URI) as connection:
        query = 'SELECT id_banc, nrobanco FROM banc'
        table = DataFrame(select(connection, query),
                          columns=('id_banc', 'nrobanco'))
        loc = {nro: cod for nro, cod in zip(table.nrobanco, table.id_banc)}

        df['nro_banco'] = df.nro_banco.map(loc)
    connection.close()


def update_col_proveedor(df):
    """
    Cambiar la descripcion del proveedor por el codigo de proveedor.
    """
    with connect(URI) as connection:
        query = 'SELECT codigo, razon_social FROM Proctcte'
        table = DataFrame(select(connection, query),
                          columns=('codigo', 'razon_social'))
        loc = {nombre: nro for nombre, nro in
               zip(table.razon_social, table.codigo)}
        df['cod_proveedor'] = df.descripcion.map(loc)
    connection.close()


def replace_values(df, values, column_name):
    """
    Reemplazar valores problemáticos con None.
    """
    column = df[column_name].isin(values)
    df.loc[column, column_name] = df.loc[
        column, column_name].replace(values, None,
                                     inplace=True)
    return df


def replace_zeros(df, file_name):
    """
    Reemplazar ceros con None.
    """
    data = [x['fk'] for x in dicts if x['name'] == file_name and x['fk'] is
            not None and x['name'] != 'mensual' and x['name'] != 'nov_roll']
    flat_list = [x for sublist in data for x in sublist]
    for key in flat_list:
        replace_values(df, [0], key[0])


def update_db():
    """
    Actualizar la base de datos.
    """

    # Borrar los datos existentes en la BD.
    print('Borrando datos existentes...')
    truncate()

    print('Procesando los archivos tps...')
    # Recorrer todos los archivos TPS
    for i in file_list:
        with open(PATH + i, 'r+b') as file:
            file_name, extension = i.lower().split('.')

            # Procesar el TPS con el parser para poder obtener los datos
            cols_and_type, df = parse_data(file)

            # Reemplazar ceros con None.
            replace_zeros(df, file_name)

            """
            Correciones en casos especiales de datos que no funcionan.
            """
            # if file_name == 'mensual':
            #     update_col_proveedor(df)
            #
            # if file_name == 'banc':
            #     # Eliminar los bancos nulos.
            #     df.dropna(axis='index', how='any', inplace=True)
            #
            # if file_name == 'cheques':
            #     # Eliminar cheques duplicados.
            #     df.drop_duplicates(subset='nro_cheque', keep='last',
            #                        inplace=True)
            #     # Cambiar la descripcion de localidad por el codigo.
            #     update_col_localidad(df)
            #     replace_values(df, [0, 72, 243, 312, 480], 'nrorecibo')
            #
            # if file_name == 'cheqant':
            #     # Eliminar cheques duplicados.
            #     df.drop_duplicates(subset='nro_cheque', keep='last',
            #                        inplace=True)
            #     # Cambiar la descripcion de localidad por el codigo.
            #     update_col_localidad(df)
            #     replace_values(df, [72], 'nrorecibo')
            #
            # if file_name == 'cheqprop':
            #     orden_pago = [
            #         0, 1755, 1489, 3140, 300, 1604, 1619, 2160, 3597, 403, 404,
            #         2631, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4364, 4365,
            #         4366, 4367, 4373, 4384, 4385, 4390, 4393, 2121, 2246, 1782,
            #         1801, 2469, 566, 568, 569, 1620, 4325, 4327, 4328, 4329,
            #         4330, 4331, 4332, 4333, 4337, 4396, 4397, 4398, 4399, 4400,
            #         4401, 4402, 4403, 4406, 4422, 4423, 4431, 4432, 4433, 4434,
            #         4435, 4437, 4438, 4439, 4440, 4441, 4442, 4450, 4451
            #     ]
            #     replace_values(df, orden_pago, 'nro_ordenpago')
            #
            # if file_name == 'cheqrec':
            #     # Cambiar el código del banco por el nuevo id.
            #     update_col_banc(df)
            #     replace_values(df, [72, 243, 312, 480], 'nro_recibo')
            #
            # if file_name == 'cli':
            #     replace_values(df, ['B2301'], 'localidad')
            #
            # if file_name == 'cta_cte':
            #     replace_values(df, [44], 'cod_proveedor')
            #
            # if file_name == 'cobrados':
            #     replace_values(df, [5, 82], 'nro_recibo')
            #
            # if file_name == 'deposito':
            #     df.dropna(subset=['nro_banco'], inplace=True)
            #
            # if file_name == 'items':
            #     # replace_values(df, [2], 'movimiento')
            #     replace_values(df, [2, 6, 11], 'campana')
            #
            if file_name == 'localidad':
                # Cambiar la descripcion de provincia por nro_provincia.
                update_col_provincia(df)
            #
            # # if file_name == 'mov_silos':
            # #     replace_values(df, [2], 'movimiento')
            #
            # if file_name == 'mensual':
            #     provincias = [
            #         0, 17, 18, 20, 22, 36, 37, 41, 43, 44, 45, 48, 50,
            #         66, 74, 80, 83, 84, 86, 92, 96, 98, 100, 102, 103,
            #         104, 105, 111, 115, 117, 120, 126, 130, 136, 141,
            #         145, 147, 148, 153, 165, 168, 174, 176, 180, 184,
            #         188, 190, 200, 201, 204, 207, 208, 209, 224, 231,
            #         232, 235, 244, 252, 253, 254
            #     ]
            #     replace_values(df, provincias, 'cod_provincia')
            #
            # if file_name == 'mov_prod':
            #     replace_values(df, [1], 'destino')
            #
            if file_name == 'movimpu':
                #     provincias = [0, 17, 18, 20, 22, 35, 36, 37, 41, 43, 44, 45, 48,
                #                   56, 76, 84, 86, 93, 96, 102, 105, 111, 115,
                #                   117, 120, 135, 136, 141, 145, 148, 153, 168,
                #                   184, 188, 193, 200, 204, 207, 208, 209, 213,
                #                   232, 235, 238, 244, 252, 253, 254]
                #     replace_values(df, provincias, 'cod_provincia')
                #     orden_pago = [
                #         1, 305, 404, 1733, 1884, 1911, 1918, 1930, 1971, 4420,
                #         4394, 4464, 2121, 2160, 2229, 2214, 2246, 101, 0,
                #         1755, 2631, 2794, 300, 2469, 1782, 3140, 4401, 4402, 4403,
                #         1789, 3336, 3376, 3377, 403, 3597, 4429, 4430, 4431, 1801,
                #         3748, 3801, 582, 566, 568, 569, 672, 4411, 4412, 4413,
                #         4324, 4325, 4326, 4327, 4328, 4329, 4330, 4331, 4332, 4333,
                #         4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343,
                #         4344, 4345, 4346, 4347, 4348, 4349, 4350, 4351, 4373, 4352,
                #         4353, 4354, 4355, 4356, 4357, 4358, 4359, 4360, 4361, 4362,
                #         4363, 1604, 4364, 4365, 4366, 4367, 4368, 1977, 4369, 4370,
                #         4371, 4372, 4374, 4375, 4376, 4377, 4378, 4379, 4380, 4381,
                #         4382, 4383, 4384, 4385, 4386, 4387, 4388, 4389, 4390, 4391,
                #         4392, 4393, 4419, 4395, 4396, 4397, 4398, 4399, 4400, 4404,
                #         4405, 4406, 4407, 4408, 4409, 4410, 4414, 4415, 4416, 4417,
                #         4418, 4421, 4422, 4423, 4424, 4425, 4426, 4427, 4428, 4432,
                #         4433, 4434, 4458, 4456, 4457, 4435, 4436, 4437, 4438, 4439,
                #         4440, 4441, 4442, 4443, 4444, 4445, 4446, 4447, 4448, 4449,
                #         4459, 4450, 4451, 4452, 4453, 4454, 4455, 4460, 4461, 4462,
                #         4463, 1619, 1620, 4465, 4466]
                #     replace_values(df, orden_pago, 'nro_ordenpago')
                replace_values(df, [174, 351], 'tipo_proveedor')
                replace_values(df, [450, 529, 582, 584, 620, 699, 700, 701, 702, 703, 704,
                                    705, 706, 707, 708, 709, 710, 711, 712, 774, 1083,
                                    1110, 1121, 1132, 1136], 'cod_imput')

            if file_name == 'imputaci':
                df.drop_duplicates(subset=['codigo'], inplace=True)
                replace_values(df, [115, 509, 940], 'donde_acumula')

            if file_name == 'acumula':
                df.dropna(subset=['descripcion'], inplace=True)

            #
            # # Cambiar el código del banco por el nuevo id.
            # if file_name == 'novcherec':
            #     update_col_banc(df)
            #
            # if file_name == 'pendpago':
            #     replace_values(df, [44], 'cod_prove')
            #
            # if file_name == 'potreros':
            #     replace_values(df, [2, 5, 6, 7, 8, 9, 10, 11],
            #                    'campana_actual')
            #
            # if file_name == 'nov_agro':
            #     replace_values(df, [2], 'codigo_laboreo')
            #     replace_values(df, [9], 'codigo_formula')
            #
            # if file_name == 'nov_roll':
            #     replace_values(df, [0], 'nro_contratista')
            #     replace_values(df, [0], 'nro_tractorista')
            #     replace_values(df, [0], 'nro_tractor')
            #     replace_values(df, [0], 'nro_maquina')
            #     replace_values(df, [0], 'codigo_laboreo')
            #     replace_values(df, [0], 'nro_producto')
            #
            # if file_name == 'observop':
            #     replace_values(df, [2214, 3748, 4368, 4395], 'nro_orden_pago')
            #
            # if file_name == 'pagados':
            #     orden_pago = [
            #         649, 651, 653, 655, 657, 659, 665, 667, 669, 671, 673, 675,
            #         677, 615, 617, 619, 621, 623, 625, 627, 629, 631, 633, 635,
            #         637, 639, 641, 643, 645, 647, 1489, 911, 1782, 1789, 1801,
            #         1617, 2469, 3801, 101, 3376, 568, 569, 570, 571, 573, 574,
            #         577, 579, 581, 583, 584, 586, 588, 590, 592, 594, 597, 599,
            #         601, 603, 605, 607, 609, 611, 613, 2631, 0, 300, 566, 2229,
            #         2794, 2246, 1755, 3140, 403, 404, 1977, 4342, 4343, 4344,
            #         4358, 4359, 4360, 4361, 4362, 4363, 4365, 4366, 4367, 4369,
            #         4370, 4371, 3597, 2121, 1604, 4325, 4333, 4338, 4339, 4340,
            #         4341, 4372, 4373, 4386, 4391, 4392, 4393, 4394, 4400, 4401,
            #         4402, 4403, 4415, 4416, 4417, 4418, 4423, 4424, 4425, 4426,
            #         4427, 4428, 4429, 4430, 4431, 4432, 4433, 4434, 4435, 4451,
            #         4455, 4458
            #     ]
            #     replace_values(df, orden_pago, 'nro_orden_pago')
            #
            # if file_name == 'prgastos':
            #     replace_values(df, [4467], 'nro_orden_pago')
            #     replace_values(df, [512], 'nro_recibo')
            #
            # if file_name == 'provedor':
            #     replace_values(df, ['2'], 'localidad')
            #
            # if file_name == 'proctcte':
            #     replace_values(df, ['5285', 'B2342', '2451'], 'localidad')
            #
            # if file_name == 'resopago':
            #     orden_pago = [
            #         583, 584, 586, 588, 590, 592, 594, 597, 599, 601, 603, 605,
            #         607, 609, 611, 613, 615, 617, 619, 621, 623, 625, 627, 629,
            #         631, 633, 635, 637, 639, 641, 643, 645, 647, 649, 651, 653,
            #         655, 657, 659, 665, 667, 669, 671, 672, 673, 675, 677, 566,
            #         568, 569, 570, 571, 573, 574, 577, 579, 581, 101, 911, 1489,
            #         1604, 1617, 1619, 1620, 1755, 1782, 1789, 1801, 1977, 2121,
            #         2160, 2229, 2246, 2469, 300, 2631, 3140, 3336, 3376, 3377,
            #         403, 404, 3597, 3748, 3801, 4324, 4325, 4326, 4327, 4328,
            #         4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338,
            #         4339, 4340, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348,
            #         4349, 4350, 4351, 4352, 4353, 4354, 4355, 4356, 4357, 4358,
            #         4359, 4360, 4361, 4362, 4363, 4364, 4365, 4366, 4367, 4368,
            #         4369, 4370, 4371, 4372, 4373, 4374, 4375, 4376, 4377, 4378,
            #         4379, 4380, 4381, 4382, 4383, 4384, 4385, 4386, 4387, 4388,
            #         4389, 4390, 4391, 4392, 4393, 4394, 4395, 4396, 4397, 4398,
            #         4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407, 4408,
            #         4409, 4410, 4411, 4412, 4413, 4428, 4429, 4430, 4431, 4432,
            #         4433, 4434, 4435, 4436, 4437, 4438, 4439, 4440, 4441, 0,
            #         4442, 4443, 4444, 4445, 4446, 4447, 4448, 4449, 4450, 4451,
            #         4452, 4453, 4454, 4455, 2794, 4414, 4415, 4416, 4417, 4418,
            #         4419, 4420, 4421, 4422, 4423, 4424, 4425, 4426, 4427, 4456,
            #         4457, 4458, 4459, 4460, 4461, 4462, 4463, 4464, 4465, 4466
            #     ]
            #     replace_values(df, orden_pago, 'nro_orden')
            #
            # if file_name == 'temp_sto':
            #     replace_values(df, [122, 100, 101, 110, 126, 102, 119, 105],
            #                    'nro_producto')
            #
            # if file_name == 'ventas':
            #     provincias = [0, 17, 18, 20, 35, 36, 37, 41, 43, 45, 56, 76, 93,
            #                   99, 117, 135, 136, 148, 193, 195, 200, 207,
            #                   208, 209, 213, 238, 252, 253]
            #     replace_values(df, provincias, 'cod_provincia')
            #
            if file_name == 'terceros':
                # chr(0): tipo de dato Null que no le agrada a la BD.
                replace_values(df, [chr(0)], 'diroter')
                # replace_values(df, [1977, 4404], 'nro_ordenpago')

            # Agregar los datos la BD.
            print(f'Agregando {file_name} a la BD...')
            add_data(cols_and_type, df, file_name)

    print('Actualización de datos exitosa.')
