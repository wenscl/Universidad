# -*- coding: cp1252 -*-
import numpy as np
from numpy.linalg import *

class Solucion:
    def __init__(self):
        self.incognitas = None
    def imprimir(self):
        for i in range(len(self.incognitas)):
            print "X" + str(i+1) + ": " + str(self.incognitas[i])
            
def GJ(m):
    print "GAUSS JORDAN\n"
    S = Solucion()
    F = m.shape[0]
    C = m.shape[1]
    if ((F == (C-1)) and (0 in m.diagonal())):
        return "verifique los datos"
    else:
        for f in range(F):
            m[f] = m[f] / m[f,f] #Normalizar.
            for f2 in range(F):
                if (f != f2):
                    m[f2] = m[f2] - m[f2,f]*m[f] #Nueva fila.
        print m
        S.incognitas = m[:,-1]
        return S

#funcion para ver si es DD
def GS(m,iteraciones=100):
    print "GAUSS SEIDEL\n"
    S = Solucion()
    F = m.shape[0]
    C = m.shape[1]
    if ((F == (C-1)) and (0 in m.diagonal())):
        return "Verifique los datos"
    else:
        mi = m[:,:-1] #Matriz de los coeficientes.
        mr = m[:,-1] #Términos independientes.
        xsol = np.zeros(F) #Primer solución.
        xsolant = np.full((F),None)
        c = 0
        while (c < iteraciones) and (not np.allclose(xsol,xsolant)"Compara si dos valores son parecidos"):
            c += 1
            xsolant = np.copy(xsol)
            for i in range(F):
                xfila = np.concatenate((mi[i,:i],mi[i,i+1:]),axis=1)
                xvalor = np.concatenate((xsol[:i],xsol[i+1:]), axis=1)
                xsol[i] = (mr[i]-(sum(xfila*xvalor)))/mi[i,i]
        print m
        S.incognitas = xsol
        return S

m = np.array(([400.01,100.02,100.03,0,5470.1], [0,-140.1,0,100.2,-110.09], [-100.1,0,620.03,-100.04,0], [0,200.05,50.2,400.08,8500.01]), dtype=float)
a = GJ(m)
print
a.imprimir()
print "\n"
b = GS(m)
print
b.imprimir()
