# -*- coding: utf-8 *-*

"""Librería con funciones para los TPs de SO I en UCSE DAR

>>> class P():
...     pass
>>> d = {'Atributo': 'Valor', 'Atributos': 'Valores'}
>>> o = dict2object(P, d)
>>> o.Atributo
'Valor'
>>> o.Atributos
'Valores'
"""

import json
import os
from clases import Proceso


def dict2object(Clase, datos):
    """Crea un objeto desde un diccionario

    Recibe una "Clase" para instanciar y un diccionario con los datos a cargar
    en el objeto.

    >>> class P():
    ...     pass
    >>> d = {'Atributo1': 'Valor1', 'Atributo2': 'Valor2'}
    >>> o = dict2object(P, d)
    >>> o.Atributo1
    'Valor1'
    >>> o.Atributo2
    'Valor2'
    """
    o = Clase()
    for k, v in datos.items():
        setattr(o, k, v)

    return o


def load_from_json(filename):
    if os.path.isfile(filename):
        procesos = []
        d = json.load(open(filename, 'r'))
        for k, v in d.items():
            procesos.append(dict2object(Proceso, v))
        return procesos
    else:
        raise Exception("El archivo solicitado no existe")


if __name__ == '__main__':
    # Si ejecuto el módulo realizo los tests
    import doctest
    doctest.testmod(report=True, verbose=True, exclude_empty=True)
