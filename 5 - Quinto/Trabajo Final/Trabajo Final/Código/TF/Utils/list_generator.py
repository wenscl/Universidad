import os

from Utils.tps_path import PATH


def list_generator():
    """
    Generar una lista con los archivos.
    """
    file_list = os.listdir(PATH)
    file_list = [x for x in file_list if x.endswith((".tps", ".TPS", "Tps"))]
    file_list.sort(key=str.lower)

    print(file_list)

    return file_list
