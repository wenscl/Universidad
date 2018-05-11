# -*- coding: utf-8 *-*

__autores__ = [
    ["Camila Kopech", "camii_kopech@hotmail.com"],
    ["Wendy Sclerandi", "weenscl@hotmail.com"]
]

"""Funciones codificadas por los alumnos de la cátedra"""


def FIFO(actual, listos, tiempo, quantum):
    if actual == None or actual.fin():
        proximo = tiempo + 1
        pproximo = None
        for p in listos: #buscar el proceso a ejecutar siguiente
            if not p.fin() and p.inicio <= tiempo and p.inicio < proximo:
                proximo = p.inicio
                pproximo = p
        if pproximo != None: #ejecutar el siguiente y hacer esperar los demas
            pproximo.ejecutar()
            for p in listos:   
                if p.inicio <= tiempo and not p.fin() and p != pproximo:
                    p.esperar()
            return pproximo
    else: #si el proceso actual no termino su ciclo los demas esperan
        actual.ejecutar() 
        for p in listos:
            if p.inicio <= tiempo and not p.fin() and p != actual :
                p.esperar()
        return actual 
        
def SJN(actual, listos, tiempo, quantum):
    if actual == None or actual.fin():
        proximo = tiempo + 1
        pproximo = None
        dmenor = 1000
        for p in listos: #buscar el proceso de menor duracion
            if not p.fin() and p.inicio <= tiempo and p.inicio < proximo and p.duracion < dmenor:
                proximo = p.inicio
                pproximo = p
                dmenor = p.duracion
        if pproximo != None: #ejecutar el siguiente y hacer esperar a los demas
            pproximo.ejecutar()
            for p in listos:   
                if p.inicio <= tiempo and not p.fin() and p != pproximo:
                    p.esperar()
            return pproximo
    else: #si el proceso actual no termino su ciclo los demas esperan
        actual.ejecutar() 
        for p in listos:
            if p.inicio <= tiempo and not p.fin() and p != actual:
                p.esperar()
        return actual 

def SRT(actual, listos, tiempo, quantum):
    if actual != None:
        dmenor = 1000
        proximo = tiempo + 1
        pproximo = None
        for p in listos: #buscar el proceso de menor tiempo restante de ejecucion
            if not p.fin() and p.inicio <= tiempo and p.inicio < proximo and p.duracion < dmenor:
                dmenor = p.duracion
                proximo = p.inicio
                pproximo = p
        if pproximo != None: #ejecutar el siguiente y hacer esperar a los demas
            pproximo.ejecutar()
            for p in listos:   
                if p.inicio <= tiempo and not p.fin() and p != pproximo :
                    p.esperar()
            return pproximo
        else:
            actual.ejecutar()
            return actual
    else: #si no hay procesos en ejecucion, buscar el que se debe ejecutar
        dmenor = 1000
        for p in listos:
            if p.inicio <= tiempo and not p.fin() and p.duracion < dmenor:
                dmenor = p.duracion
                pproximo = p
        pproximo.ejecutar()
        return pproximo

def RoundRobin(actual, listos, tiempo, quantum):
    if actual == None or actual.quantum == 0 or actual.fin(): #reemplazar el tiempo de inicio para saber el tiempo en que el proceso volvio a entrar en la cola
        if actual != None and actual.quantum == 0 and not actual.fin():
            actual.inicio = tiempo
        proximo = tiempo
        for p in listos: #buscar el proceso siguiente a ejecutar
            if not p.fin() and p.inicio <= proximo:
                if (p.procesado == 0 and p.inicio == proximo) or (p.inicio < proximo):
                    proximo = p.inicio
                    actual = p
        if actual != None: #inicializar el quantum y la ejecucion del proceso
            actual.quantum = quantum
            actual.ejecutar()
            actual.quantum -= 1
            for p in listos:   
                if p.inicio <= tiempo and not p.fin() and p != actual:
                    p.esperar()
            return actual 
    else: #si el proceso actual no termino su quantum los demas esperan
        actual.ejecutar()
        actual.quantum -= 1
        for p in listos:   
            if p.inicio <= tiempo and not p.fin() and p != actual:
                p.esperar()
        return actual

def HRN(actual, listos, tiempo, quantum):
    raise NotImplementedError
