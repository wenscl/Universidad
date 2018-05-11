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
    S = Solucion()
    F = m.shape[0]
    C = m.shape[1]
    if ((F == (C-1)) and (0 in m.diagonal())):
        return "verifique los datos"
    else:
        for f in range(F):
            m[f] = m[f]/m[f,f]
            for f2 in range(F):
                if (f != f2):
                    m[f2] = m[f2] - m[f2,f]*m[f]
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
        mi = m[:,:-1]
        mr = m[:,-1]
        xsol = np.zeros(F)
        xsolant = np.full((F),None)
        c = 0
        while (c<iteraciones) and (not np.allclose(xsol,xsolant, rtol=0.01)):
            c += 1
            xsolant = np.copy(xsol)
            for i in range(F):
                xfila = np.concatenate((mi[i,:i],mi[i,i+1:]),axis=1)
                xvalor = np.concatenate((xsol[:i],xsol[i+1:]), axis = 1)
                xsol[i] = (mr[i]-(sum(xfila*xvalor)))/mi[i,i]
        print m
        S.incognitas = xsol
        return S
m = np.array(([1,1,1,1,96], [0.25,0.3333333,0.5,0.5,31], [1,1,-10,0,0], [1,1,1,-15,0]), dtype=float)

if __name__=="__main__":
    a = GJ(m)
    print
    a.imprimir()
    print "\n"
    b = GS(m)
    print
    b.imprimir()
