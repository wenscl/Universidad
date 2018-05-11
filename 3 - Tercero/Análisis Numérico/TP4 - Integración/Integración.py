# -*- coding: cp1252 -*-
import math

def func(f,x):
    variable = {'x': x}   
    try:
        return eval(f,{'math':math},variable)
    except SyntaxError:
        print 'Funcion mal formada'
        return None

def Trapecios(f,a,b):
    print "TRAPECIOS"
    A = (func(f,b) + func(f,a)) * (b-a)/2.0
    return "Área: %.4f\n" % A
    
def TrapeciosMultiple(f,a,b,n):
    print "TRAPECIOS MULTIPLES"
    h = (b-a)/float(n)
    var1 = 0
    for i in range(1,n,1):
        x = a + i*h
        var1 += 2 * func(f,x)
    A = h/2 * (func(f,a) + var1 + func(f,b))
    return "Área: %.4f\n" % A

def S13S(f,a,b):
    print "SIMPSON 1/3 SIMPLE"
    h = (b-a)/2.0
    A = h/3 * (func(f,a) + 4*func(f,(a+h)) + func(f,b))
    return "Área: %.4f\n" % A


def S38S(f,a,b):
    h = (b-a)/3.0
    A = 3/8.0*h*(func(f,a) + 3*func(f,(a+h)) + 3*func(f,(a+2*h)) + func(f,b))
    return A

def S13M(f,a,b,n):
    print "SIMPSON 1/3 MULTIPLE"
    h = (b-a)/float(n)
    #Ejercicio TP
    #h = 0.2
    var1 = 0
    var2 = 0
    if ((-1)**n > 0): 
        for i in range(1,n,2):
            x = a + i*h
            var1 += 4 * func(f,x)
        for i in range(2,(n-1),2):
            x = a + i*h
            var2 += 2 * func(f,x)
        A = h/3 * (func(f,a) + var1 + var2 + func(f,b))
        return "Área: %.4f\n" % A
    else:
        #S13M
        for i in range(1,(n-2),2):
            x = a + i*h
            var1 += 4 * func(f,x)
        for i in range(2,(n-3),2):
            x = a + i*h
            var2 += 2 * func(f,x)

        #S38S
        A = h/3 * (func(f,a) + var1 + var2 + func(f,(b-3*h)))
        I = A + S38S(f,(b-3*h),b)
        return "Área: %.4f\n" % I

#PARCIAL
#Ejercicio 1
"""
f = "(math.e**x)*(-0.25*x**2+1.25*x-1.14)"
a = 1.2
b = 3.8
n = 25
"""

#Ejercicio3
f = '(-x**3+x)-(x**3-4*x)'
a = 0
b = 1.58
n = 20


#print Trapecios(f,a,b)
#print TrapeciosMultiple(f,a,b,n)
print S13S(f,a,b)
print S13M(f,a,b,n)

