# -*- coding: utf-8 -*-
from G3 import Optimo, LRU, FIFO, Reloj


class Prueba(object):

    def __init__(self, marcos, paginas):
        self.marcos = marcos  # Cantida de marcos a utilizar
        self.paginas = paginas  # Listado de páginas a procesar


def main():
    pruebas = [
        # Conjunto de pruebas obligatorio
        Prueba(3, [1, 2, 5, 3, 8, 5, 4, 2, 8, 3, 7, 1]),
        Prueba(4, [2, 5, 3, 4, 7, 6, 3, 8, 1, 3, 6, 2]),
        Prueba(3, [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]),
        Prueba(4, [8, 3, 2, 2, 2, 2, 1, 5, 3, 8, 2, 7]),
        Prueba(3, [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3, 4]),
    ]

    for prueba in pruebas:
        print "*" * 80
        print u"  Páginas: %s" % prueba.paginas
        for algoritmo in [Optimo, LRU, FIFO, Reloj]:
            try:
                a = algoritmo(prueba.marcos)
                print "\nEjecutando %s" % a
                print "-" * 80
                for p in prueba.paginas:
                    a.colocar(p, prueba.paginas)
                a.visualizar_historia()
            except NotImplementedError:
                print "Algoritmo no implementado"
        print "\n"


if __name__ == '__main__':
    main()
