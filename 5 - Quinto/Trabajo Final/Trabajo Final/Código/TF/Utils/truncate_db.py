"""
    Script para limpiar los datos de la BD.
"""

from psycopg2 import connect
from Utils.sql import execute_query
from Utils.update_order import file_list
from Website.settings import DATABASES

NAME = DATABASES['default']['NAME']
USER = DATABASES['default']['USER']
PASSWORD = DATABASES['default']['PASSWORD']
HOST = DATABASES['default']['HOST']
PORT = DATABASES['default']['PORT']
URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'


def truncate():
    """
    Truncar los datos de la BD para poder actualizarla.
    """
    # Conectarse a la BD.
    with connect(URI) as connection:
        # Truncar los datos de todas las tablas.
        for file in file_list:
            file_name, extension = file.lower().split('.')
            query = f"TRUNCATE {file_name} cascade;"
            execute_query(connection, query)

    connection.close()
