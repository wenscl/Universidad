# -*- coding: utf-8 *-*

"""TP 1 - Sistemas Operativos I - UCSE DAR"""

import json
import os
from copy import deepcopy
from funciones import dict2object, load_from_json
from optparse import OptionParser


def ejecutar(algoritmos, procesos):
    # Resultados de la ejecución
    ejecuciones = {a.__name__: None for a in algoritmos}

    for algoritmo in _algoritmos:
        _procs = [deepcopy(c) for c in procesos]  # Copio los procesos
        ciclos = -1  # Inicializo en -1 para que el 1er tiempo sea 0
        actual = None
        try:
            while any([not c.fin() for c in _procs]) and ciclos < 100:
                ciclos += 1
                actual = algoritmo(actual, _procs, ciclos, QUANTUM)
                # Actualizo la historia para los que no procesan ni esperan
                for p in _procs:
                    if len(p.historia) == ciclos and not p.fin():
                        p.listo()
            _procs.sort(key=lambda x: x.id)
            ejecuciones[algoritmo.__name__] = _procs
        except NotImplementedError:
            ejecuciones[algoritmo.__name__] = None

    return ejecuciones


if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-w", "--web",
                      action="store_true", dest="use_web", default=False,
                      help="Start a web visualizator")
    parser.add_option("-c", "--catedra",
                      action="store_true", dest="catedra", default=False,
                      help="Load catedra module")
    (options, args) = parser.parse_args()

    if options.use_web:
        # Cargar app Flask para cargar JSON y mostrar resultados
        pass
    else:
        if options.catedra:
            from catedra import FIFO, SJN, SRT, RoundRobin, HRN, __autores__
        else:
            from alumno import FIFO, SJN, SRT, RoundRobin, HRN, __autores__
        _algoritmos = [FIFO, SJN, SRT, RoundRobin, HRN, ]
        QUANTUM = 2

        # Cargo los datos de los procesos a ejecutar desde el archivo data.json
        procesos = load_from_json("data.json")

        # Alumnos
        print "*" * 80
        for a in __autores__:
            print "%s <%s>" % tuple(a)
        print

        # Ejecuto los algoritmos
        ejecs = ejecutar(_algoritmos, procesos)
        for a in _algoritmos:
            print a.__name__
            if ejecs[a.__name__] is not None:
                for p in ejecs[a.__name__]:
                    print "%5s:" % p.id,
                    for e in p.historia:
                        print e.center(5, ' '),
                    print
                print
            else:
                print "    * No implementado *\n"
        print "*" * 80
