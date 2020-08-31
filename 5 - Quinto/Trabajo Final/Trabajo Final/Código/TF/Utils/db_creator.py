"""
Script para crear la BD, las tablas y las claves.
"""

from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from TpsParse.Tps.TpsFile import TpsFile
from Utils.create_keys import create_keys
from Utils.sql import execute_query
from Utils.tps_path import PATH
from Utils.update_db import DATE_NAME_LIST
from Utils.update_order import file_list
from Website.settings import DATABASES

NAME = DATABASES['default']['NAME']
USER = DATABASES['default']['USER']
PASSWORD = DATABASES['default']['PASSWORD']
HOST = DATABASES['default']['HOST']
PORT = DATABASES['default']['PORT']
URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'

TYPES = {
    'Byte': 'integer',
    'SignedShort': 'integer',
    'UnsignedShort': 'integer',
    'Date': 'date',
    'Time': 'time',
    'SignedLong': 'integer',
    'UnsignedLong': 'integer',
    'Float': 'real',
    'Double': 'real',
    'Bcd': 'real',
    'FixedLengthString': 'varchar',
    'ZeroTerminatedString': 'varchar',
    'PascalString': 'varchar',
    'Group': 'varchar',
}


def create_db():
    """
    Crear la BD, las tablas y las claves.
    """
    connection = connect(dbname='postgres',
                         user='postgres',
                         host='localhost',
                         password='1684')

    with connection:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        execute_query(connection, f"CREATE DATABASE tf;")

    print('Base de datos creada exitosamente.')
    connection.close()

    # Crear las tablas de la BD.
    create_tables()


def create_tables():
    # Conectarse a la BD.
    with connect(URI) as connection:
        # Procesar el tps con el parser para poder obtener los atributos y
        # crear las tablas.
        print('Creando las tablas de la BD...')
        for i in file_list:
            with open(PATH + i, 'r+b') as file:
                file_name, extension = i.lower().split('.')

                # Obtener los campos de cada archivo.
                cols_and_type = []
                columns = []
                tps = TpsFile(file)
                for definition in tps.get_table_definitions():
                    for field in definition.fields:
                        column = field.field_name.split(':')[1].lower()
                        col_and_type = (field.field_name.split(':')[1].lower(),
                                        field.type)
                        if column not in columns:
                            columns.append(column)
                            cols_and_type.append(col_and_type)

                # Crear una lista con los atributos y sus tipos de datos.
                list_attr = []

                # Creación de un id para usar como clave primaria
                # porque no se puede usar una combinada.
                create_id = [
                    'banc',
                    'carga',
                    'cargaoc',
                    'ccarga',
                    'cheqprop',
                    'cheqrec',
                    'cobrados',
                    'creditos',
                    'cta_cte',
                    'cteprocc',
                    'ctepro',
                    'cventa',
                    'deposito',
                    'gf',
                    'gg',
                    'humedad',
                    'items',
                    'movgan',
                    'pagados',
                    'pendcobro',
                    'pendpago',
                    'stockdep',
                    'ventas',
                    'bolsas',
                    'gan_car',
                    'giros',
                    'libroba',
                    'maeche',
                    'maecli',
                    'mensual',
                    'montos_para_girar',
                    'mov_camp',
                    'mov_cons',
                    'mov_cose',
                    'mov_hora',
                    'mov_leche',
                    'mov_potr',
                    'mov_prod',
                    'mov_silos',
                    'mov_suple',
                    'mov_trac',
                    'mov_trans',
                    'movimpu',
                    'nimpvta',
                    'nov_agro',
                    'nov_camp',
                    'nov_cons',
                    'nov_cose',
                    'nov_fert',
                    'nov_fin',
                    'nov_gran',
                    'nov_hora',
                    'nov_lluv',
                    'nov_maqu',
                    'nov_plan',
                    'nov_prod',
                    'nov_roll',
                    'nov_serv',
                    'nov_siem',
                    'nov_suel',
                    'nov_suple',
                    'nov_transp',
                    'novcherec',
                    'novchpro',
                    'novctcte',
                    'novedad',
                    'noventas',
                    'novimp',
                    'novimpgran',
                    'novimpserv',
                    'novimptransp',
                    'novimpu',
                    'novimpvta',
                    'novpref',
                    'observop',
                    'prgastos',
                    'pro_car',
                    'pro_car_oc',
                    'resopago',
                    'ret_prov',
                    'stocksil',
                    'temp_c',
                    'temp_prod',
                    'temp_sto',
                    'terceros',
                    'tmpcajas',
                    'vcarga',
                    'vcta_cte',
                    'ven_car'
                ]
                if file_name in create_id:
                    list_attr.append(f"id_{file_name} serial")

                for c_name, c_type in cols_and_type:
                    # Si el nombre del campo empieza con 'fec' o 'periodo',
                    # asignarle tipo 'date'.
                    if c_name.startswith(
                            DATE_NAME_LIST) and c_type == 'SignedLong':
                        list_attr.append(f"{c_name} {TYPES['Date']}")
                    # Cambiar el tipo de datos de ciertos campos.
                    # elif file_name == 'cod_comprob' and c_name == 'codigo':
                    #     list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'cheques' and c_name == 'nro_cheque':
                        list_attr.append(f"{c_name} {TYPES['SignedLong']}")
                    elif file_name == 'tanque' and c_name == 'nro_tanque':
                        list_attr.append(f"{c_name} {TYPES['SignedLong']}")
                    elif file_name == 'camion' and c_name == 'nro_camion':
                        list_attr.append(f"{c_name} {TYPES['SignedLong']}")
                    elif file_name == 'camion' and c_name == 'año':
                        list_attr.append(f"ano {TYPES[c_type]}")
                    elif file_name == 'acredita' and c_name == 'imputacion':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'novimpu' and c_name == 'nro_imputacion':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'carga' and c_name == 'cod_movimiento':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'cargaoc' and c_name == 'cod_movimiento':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'ccarga' and c_name == 'cod_movimiento':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'cventa' and c_name == 'cod_movimiento':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'vcarga' and c_name == 'cod_movimiento':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'cheqant' and c_name == 'nro_cheque':
                        list_attr.append(f"{c_name} {TYPES['SignedLong']}")
                    elif file_name == 'glibroba' and c_name == 'nrocheque':
                        list_attr.append(f"{c_name} {TYPES['SignedLong']}")
                    elif file_name == 'guaretenib' and c_name == 'provincia':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'ret_ib' and c_name == 'nrocheque':
                        list_attr.append(f"{c_name} {TYPES['SignedLong']}")
                    elif file_name == 'ret_ib' and c_name == 'provincia':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'localidad' and c_name == 'provincia':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'libroba' and c_name == 'nrocheque':
                        list_attr.append(f"{c_name} {TYPES['SignedLong']}")
                    elif file_name == 'temp_c' and c_name == 'campana_actual':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'mov_camp' and c_name == 'campana_actual':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'sector' and c_name == \
                            'responsable_sector':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    elif file_name == 'subsecto' and c_name == \
                            'responsable_sub_sector':
                        list_attr.append(f"{c_name} {TYPES['SignedShort']}")
                    else:
                        list_attr.append(f"{c_name} {TYPES[c_type]}")

                str_attr = ', '.join(list_attr)
                query = f'CREATE TABLE {file_name} ({str_attr});'

                # Crear la tabla en la BD.
                execute_query(connection, query)

                # Crear campo cod_proveedor en tabla Mensual.
                if file_name == 'mensual':
                    query = 'ALTER TABLE Mensual ADD cod_proveedor integer;'
                    execute_query(connection, query)

        # Crear tabla Tipo de Movimiento.
        query = 'CREATE TABLE tipo_movimiento ' \
                '(codigo integer PRIMARY KEY, descripcion varchar);'
        execute_query(connection, query)

        # Agregar los datos de Tipo de Movimiento.
        query = "INSERT INTO tipo_movimiento VALUES (1, 'Factura Cuenta " \
                "Corriente'), " \
                "(2, 'Contado'), " \
                "(3, 'Nota de Débito'), " \
                "(4, 'Nota de Crédito'), " \
                "(5, 'Orden de Pago'), " \
                "(6, 'Cobranzas')"
        execute_query(connection, query)

    connection.close()
    print('Tablas creadas exitosamente.')

    # Crear las claves primarias y foraneas de todas las tablas.
    create_keys()
