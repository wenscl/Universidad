from psycopg2 import connect
from Utils.sql import execute_query


def drop_db():
    """
    Eliminar BD.
    """
    connection = connect(dbname='postgres',
                         user='postgres',
                         host='localhost',
                         password='1684')

    with connection:
        connection.autocommit = True
        execute_query(connection, "DROP DATABASE tf;")
