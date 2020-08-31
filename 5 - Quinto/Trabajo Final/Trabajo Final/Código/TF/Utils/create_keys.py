"""
    Script para crear las claves de la BD
"""

from psycopg2 import connect
from Utils.keys import dicts
from Utils.sql import execute_query
from Utils.update_order import file_list
from Website.settings import DATABASES

NAME = DATABASES['default']['NAME']
USER = DATABASES['default']['USER']
PASSWORD = DATABASES['default']['PASSWORD']
HOST = DATABASES['default']['HOST']
PORT = DATABASES['default']['PORT']
URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'


def create_primary(conn):
    # Recorrer el archivo con todas las claves.
    for tables in dicts:
        if tables['name'] in file_list:
            # Agregar claves primarias.
            if tables['pk'] is not None:
                # Una sola clave
                if not isinstance(tables['pk'], tuple):
                    query = f"ALTER TABLE {tables['name']} ADD PRIMARY KEY " \
                            f"({tables['pk']});"
                    execute_query(conn, query)
                # Más de una clave
                else:
                    query = f"ALTER TABLE {tables['name']} ADD PRIMARY KEY " \
                            f"{tables['pk']};"
                    execute_query(conn, query)


def create_foreing(conn):
    # Recorrer el archivo con todas las claves.
    for tables in dicts:
        if tables['name'] in file_list:
            # Agregar claves foraneas.
            if tables['fk'] is not None:
                # Una sola clave
                if len(tables['fk']) == 1:
                    key1, table, key2 = tables['fk'][0]
                    query = f"ALTER TABLE {tables['name']} ADD FOREIGN KEY " \
                            f"({key1}) REFERENCES {table} ({key2});"
                    execute_query(conn, query)
                # Más de una clave
                else:
                    for key in tables['fk']:
                        query = f"ALTER TABLE {tables['name']} ADD FOREIGN KEY " \
                                f"({key[0]}) REFERENCES {key[1]} ({key[2]});"
                        execute_query(conn, query)


def create_keys():
    """
    Crear claves en la BD.
    """
    # Conectarse a la BD y abrir un cursor para hacer operaciones
    with connect(URI) as connection:
        # Agregar claves primarias.
        print('Creando claves primarias...')
        create_primary(connection)

        # Agregar claves foraneas.
        print('Creando claves foraneas...')
        create_foreing(connection)

    connection.close()
    print('Claves creadas exitosamente.')
