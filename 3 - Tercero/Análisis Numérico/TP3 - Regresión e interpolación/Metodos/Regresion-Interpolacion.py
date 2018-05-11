# -*- coding: cp1252 -*-
import numpy as np
import SistemaEcuaciones as se

#TP3
"""
#Ejercicio 1
x = np.array(([-3,0.5,1,2,5]), dtype = float)
y = np.array(([-7.5,-2.25,-1.5,0,4.5]), dtype = float)
"""

#Ejercicio 2
x = np.array(([-1,0,2,3,5,6]), dtype = float)
y = np.array(([6,4,1,1,2,5]), dtype = float)

"""
#Ejercicio 3 - urbana
x = np.array(([0,2,3,4,6,10]), dtype = float)
y = np.array(([36,32,30,29,28,26]), dtype = float)
"""
"""
#Ejercicio 3 - suburbana
x = np.array(([0,2,3,4,6,10]), dtype = float)
y = np.array(([4,8.5,9.5,10,11,14]), dtype = float)
"""

def lineal(x,y):
    print "LINEAL\n"
    n = x.shape[0] #Cantidad de puntos
    sx = sum(x)
    sy = sum(y)
    sxy = sum(x*y)
    sx2 = sum(x**2)
    a1 = (n*sxy - sx*sy) / (n*sx2 - sx**2)
    a0 = sy/n - (a1 * sx/n)
    st = 0
    sr = 0
    func = "%s * x + %s" % (a1,a0)
    for i in range(n):
        st = st + (y[i] - sy/n)**2
        sr = sr + (y[i] - eval(func,{},{'x' : x[i]}))**2
    r = (((st - sr) /  st) ** (0.5)) * 100
    print "Coeficiente de correlación: %.3f" % (r)
    return "y= %.3f x + %.3f" % (a1,a0) + "\n"

print lineal(x,y)
print


def polinomial(x,y):
    print "POLINOMIAL\n"
    n = x.shape[0] #Cantidad de puntos
    grado = None
    while grado < 1:
        try:
            grado = int(raw_input("Ingrese el grado de la funcion: "))
        except ValueError:
            print "El valor ingresado no es valido. Intente nuevamente."
    s = se.Solucion()
    m = np.zeros((grado+1, grado+2))
    sx = sum(x)
    sy = sum(y)
    for i in range(n):
        for j in range(0, grado+1):
            for k in range(0, grado+1):
                m[j,k] = m[j,k] + x[i]**(k+j)
            m[j,(grado+1)] = m[j,(grado+1)] + (y[i]*(x[i]**j))
    s = se.GJ(m)
    st = 0
    sr = 0
    func = ""
    for i in range(len(s.incognitas)-1,-1,-1):
        func = func + " + " + str(s.incognitas[i]) + "*x**" + str(grado)
        grado -= 1
    
    for i in range(n):
        st = st + (y[i] - sy/n)**2
        sr = sr + (y[i] - eval(func,{},{'x' : x[i]}))**2
    r = (((st - sr) /  st) ** (0.5)) * 100
    print "\nCoeficiente de correlación: %.3f" % (r)
    
    func = "y = " + func
    return func + "\n"

print polinomial(x,y)
print


def lagrange(x,y):
    print "LAGRANGE\n"
    n = x.shape[0] #Cantidad de puntos
    X = float(raw_input("Ingrese el valor a interpolar: "))
    grado = n - 1
    s = 0
    for i in range(n):
        sa = 1
        sb = 1
        for j in range(n):
            if i != j:
                sa = sa * (X - x[j])
                sb = sb * (x[i] - x[j])
        s += y[i] * sa/sb
    return s

print lagrange(x,y)

