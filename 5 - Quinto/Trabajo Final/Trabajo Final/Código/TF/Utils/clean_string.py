import unicodedata


def clean_string(string):
    """
        Eliminar acentos de los datos.
    """
    strings = [unicodedata.normalize('NFKD', s).encode('ASCII',
                                                       'ignore').decode()
               for s in string]

    return list(set(strings))
