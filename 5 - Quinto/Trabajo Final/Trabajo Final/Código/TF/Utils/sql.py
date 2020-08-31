"""
Funciones para ejecutar querys en la BD.
"""


def execute_query(connection, query):
    """
    Ejecutar query para crear una tabla.
    """
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query)


def select(connection, query):
    """
    Ejecutar query para hacer un select sobre una tabla.
    """
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

