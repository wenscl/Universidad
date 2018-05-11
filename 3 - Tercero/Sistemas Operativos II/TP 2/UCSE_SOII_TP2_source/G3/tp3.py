# -*- coding: utf-8 -*-
from catedra import Algoritmo


class Optimo(Algoritmo):

    def colocar(self, pagina, paginas=None):
        super(Optimo, self).colocar(pagina, paginas)  # Dejar esta línea
        
        existe = False
        for marco in self.marcos:
            if (marco.valor == pagina):
                existe = True
        if (existe == True):
            for marco in self.marcos:
                marco.apuntado = False

        bandera = 0        
        i = 0
        while (i < len(self.marcos)) and (bandera == 0) :
            if (existe == False) and (self.marcos[i].apuntado):
                self.marcos[i].valor = pagina
                self.marcos[i].apuntado = False
                bandera = 1
            if (bandera == 1) or (existe == True):
                if (i == (len(self.marcos) - 1)) or (self.marcos[(len(self.marcos)-1)].valor != None):
                    puntero = 0
                    valor = None
                    for marco in self.marcos:
                        p = len(self.llamadas)+1
                        pos = None
                        while (p <= len(paginas)) and (pos == None):
                            if (marco.valor == paginas[p-1]):
                                pos = p-1
                            p += 1
                        if ((puntero != None) and (pos > puntero)) or (pos == None):
                            puntero = pos
                            valor = marco.valor
                    for marco in self.marcos:
                        if (marco.valor == valor):
                            marco.apuntado = True
                else:
                    m = 0
                    encuentra = False
                    while (not encuentra):
                        if (self.marcos[m].valor == None):
                            self.marcos[m].apuntado = True
                            encuentra = True
                        m +=1
                bandera = 1
            i += 1

class LRU(Algoritmo):
    
    def colocar(self, pagina, paginas=None):
        super(LRU, self).colocar(pagina, paginas)  # Dejar esta línea

        existe = False
        valorExiste = None
        for marco in self.marcos:
            if (marco.valor == pagina):
                existe = True
                valorExiste = marco.valor
                
        bandera = 0
        i = 0
        while (i < len(self.marcos)) and (bandera == 0):
            if (existe == False) and (self.marcos[i].apuntado):
                self.marcos[i].valor = pagina
                self.marcos[i].apuntado = False
                bandera = 1
            elif (existe == True) and (valorExiste == self.marcos[i].valor):
                self.marcos[i].apuntado = False
                bandera = 1
            if (bandera == 1):
                if (i == (len(self.marcos) - 1)) or (self.marcos[(len(self.marcos)-1)].valor != None):
                    puntero = 100
                    valor = None
                    for marco in self.marcos:
                        p = 0
                        pos = 0
                        while (p < len(self.llamadas)):
                            if (marco.valor == self.llamadas[p]):
                                pos = p
                            p += 1
                        if (pos < puntero):
                            puntero = pos
                            valor = self.llamadas[pos]
                    for marco in self.marcos:
                        if (marco.valor == valor):
                            marco.apuntado = True
                elif (self.marcos[i+1].valor == None):
                    self.marcos[i+1].apuntado = True
            i += 1
            
class FIFO(Algoritmo):

    def colocar(self, pagina, paginas=None):
        super(FIFO, self).colocar(pagina, paginas)  # Dejar esta línea

        existe = False
        for marco in self.marcos:
            if (marco.valor == pagina):
                existe = True
                
        if not existe:
            bandera = 0
            i = 0
            while (i < len(self.marcos)) and (bandera == 0):
                if (self.marcos[i].apuntado):
                    self.marcos[i].valor = pagina
                    self.marcos[i].apuntado = False
                    bandera = 1
                    if (i == (len(self.marcos) - 1)):
                        self.marcos[0].apuntado = True
                    else:
                        self.marcos[i+1].apuntado = True
                i += 1

class Reloj(Algoritmo):
    
    def colocar(self, pagina, paginas=None):
        super(Reloj, self).colocar(pagina, paginas)  # Dejar esta línea

        existe = False
        for marco in self.marcos:
            if (marco.valor == pagina):
                if(marco.bit == False):
                    marco.bit = True
                existe = True
                
        if not existe:
            bandera = 0
            i = 0
            while (i < len(self.marcos)) and (bandera == 0):
                if (self.marcos[i].apuntado):
                    while (self.marcos[i].bit):
                        self.marcos[i].bit = False
                        self.marcos[i].apuntado = False
                        if (i == (len(self.marcos) - 1)):
                            i = 0
                            self.marcos[i].apuntado = True
                        else:
                            i += 1
                            self.marcos[i].apuntado = True
                    self.marcos[i].valor = pagina
                    self.marcos[i].apuntado = False
                    bandera = 1
                    if (i == (len(self.marcos) - 1)):
                        self.marcos[0].apuntado = True
                    else:
                        self.marcos[i+1].apuntado = True
                i += 1
