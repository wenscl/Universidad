# -*- coding: utf-8 *-*

"""Librería con clases para los TPs de SO I en UCSE DAR

>>> raise BloquearException("Error al bloquear")
Traceback (most recent call last):
...
BloquearException: Error al bloquear

>>> p = Proceso(0, 'P0', 2, 5)
>>> print p
0 - -->
>>> p
<Proceso: 0 - -->>
>>> p.listo()
>>> p.esperar()
>>> p.ejecutar()
>>> p.bloquear()
>>> p.estadisticas()
{'historia': ['-->', '   ', 'ESP', 'EJE'], 'espera': 1, 'ejecutado': 1}
"""


class BloquearException(Exception):
    """Exception para bloqueo de Procesos

    >>> raise BloquearException("Error al bloquear")
    Traceback (most recent call last):
    ...
    BloquearException: Error al bloquear
    """
    pass


class Proceso(object):
    """Representación de un proceso del sistema operativo

    >>> p = Proceso(1, 'P1', 0, 10)
    >>> print p
    1 - -->
    >>> p
    <Proceso: 1 - -->>
    >>> p.listo()
    >>> p.ejecutar()
    >>> p.esperar()
    >>> p.bloquear()
    Traceback (most recent call last):
    ...
    BloquearException: Un proceso solo se puede bloquear estando en ejecucion
    >>> p.ejecutar()
    >>> p.bloquear()
    >>> for k, v in p.estadisticas().items():
    ...     print "%s: %s" % (k, v)
    historia: ['-->', '   ', 'EJE', 'ESP', 'EJE']
    espera: 1
    ejecutado: 2
    """

    def __init__(self, id=None, nombre=None, inicio=None, duracion=None):
        """Inicialización del objeto"""
        self.id = id
        self.nombre = nombre
        self.inicio = inicio
        self.duracion = duracion
        self.procesado = 0
        self.estado = '-->'
        self.espera = 0
        self.historia = []
        self.quantum = None

    def __unicode__(self):
        """Representación unicode del objeto"""
        return u"%s - %s" % (self.id, self.estado)

    def __str__(self):
        """Representación string del objeto"""
        return unicode(self)

    def __repr__(self):
        """Representación genérica del objeto"""
        return u"<Proceso: %s>" % str(self)

    def __cambiar_estado(self, nuevo_estado):
        """Asigna el nuevo estado y guarda el anterior en la historia"""
        self.historia.append(self.estado)
        self.estado = nuevo_estado

    def ejecutar(self):
        """Cambia el estado a ejecución e incrementa el contador"""
        self.__cambiar_estado('EJE')
        self.procesado += 1

    def esperar(self):
        """Cambia el estado a espera e incrementa el contador"""
        self.__cambiar_estado('ESP')
        self.espera += 1

    def listo(self):
        """Cambia el estado a listo"""
        self.__cambiar_estado('   ')

    def bloquear(self):
        """Cambia el estado a bloqueado si es posible"""
        if self.estado != 'EJE':
            err = "Un proceso solo se puede bloquear estando en ejecucion"
            raise BloquearException(err)
        self.__cambiar_estado('BLQ')

    def estadisticas(self):
        """Retorna las estadísticas del proceso"""
        return {
            'ejecutado': self.procesado,
            'espera': self.espera,
            'historia': self.historia
        }

    def fin(self):
        """Retorna verdadero si el proceso ha finalizado su ejecución"""
        if self.procesado >= self.duracion and self.estado != 'FIN':
            self.terminar()
        return self.procesado >= self.duracion

    def terminar(self):
        """Cambia el estado a Finalizado"""
        self.__cambiar_estado('FIN')


if __name__ == '__main__':
    # Si ejecuto el módulo realizo los tests
    import doctest
    doctest.testmod(report=True, verbose=True, exclude_empty=True)
