# -*- coding: utf-8 *-*

__autores__ = [
    ["Nombre Apellido", "email@email.com"],
    ["Nombre Apellido", "email@email.com"]
]

"""Funciones codificadas por los alumnos de la cátedra"""


def FIFO(actual, listos, tiempo, quantum):
    if actual == None or actual.fin():
        sig = tiempo+1
        procsig = None
        for p in listos:
            if not p.fin() and p.inicio <= tiempo and p.inicio < sig:
                sig = p.inicio
                procsig = p
        if procsig != None:
            procsig.ejecutar()
            for p in listos:   
                if p.inicio <= tiempo and not p.fin() and p != procsig :
                    p.esperar()
            return procsig
    else:
        actual.ejecutar() 
        for p in listos:
            if p.inicio <= tiempo and not p.fin() and p != actual :
                p.esperar()
        return actual
    
def SJN(actual, listos, tiempo, quantum):
    if actual == None or actual.fin():
        sig = tiempo+1
        procsig = None
        duracionmen = 1000
        for p in listos:
            if not p.fin() and p.inicio <= tiempo and p.inicio < sig and p.duracion < duracionmen:
                duracionmen = p.duracion
                sig = p.inicio
                procsig = p
        if procsig != None:
            procsig.ejecutar()
            for p in listos:   
                if p.inicio <= tiempo and not p.fin() and p != procsig :
                    p.esperar()
            return procsig
    else:
        actual.ejecutar() 
        for p in listos:
            if p.inicio <= tiempo and not p.fin() and p != actual :
                p.esperar()
        return actual
    
def SRT(actual, listos, tiempo, quantum):
    if actual != None:
        duracionmen = 1000
        sig = tiempo+1
        procsig = None
        for p in listos:
            if not p.fin() and p.inicio <= tiempo and p.inicio < sig and p.duracion < duracionmen:
                duracionmen = p.duracion
                sig = p.inicio
                procsig = p
        if procsig != None:
            procsig.ejecutar()
            for p in listos:   
                if p.inicio <= tiempo and not p.fin() and p != procsig :
                    p.esperar()
            return procsig
        else:
            actual.ejecutar()
            return actual
    else:
        duracionmen = 1000
        for p in listos:
            if p.inicio <= tiempo and not p.fin() and p.duracion < duracionmen:
                duracionmen = p.duracion
                procsig = p
        procsig.ejecutar()
        return procsig
    
def RoundRobin(actual, listos, tiempo, quantum):
    if actual == None or actual.quantum == 0 or actual.fin():
        procsig = None
        sig = tiempo + 1
        for p in listos:
            if not p.fin() and p.inicio <= tiempo and p.inicio < sig and p != actual:
                sig = p.inicio
                procsig = p
        if procsig != None:
            procsig.quantum = quantum - 1
            procsig.ejecutar()
            for p in listos:   
                if p.inicio <= tiempo and not p.fin() and p != actual:
                    p.esperar()
        return procsig 
    else:
        for p in listos:   
            if p.inicio <= tiempo and not p.fin() and p != actual:
                p.esperar()
        actual.quantum = actual.quantum - 1
        actual.ejecutar()
        return actual
  


def HRN(actual, listos, tiempo, quantum):
    raise NotImplementedError
