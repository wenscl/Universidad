# -*- coding: cp1252 -*-
import math

class Solucion:
    def __init__(self, raiz=None, error=None, iteraciones=0, estado=None):
        self.raiz= raiz
        self.error= error
        self.iteraciones= iteraciones
        self.estado= estado

        
    def actualizar(self, raiz, error, estado):
        self.raiz= raiz
        self.error= error
        self.estado= estado
        
    def imprimir(self):
        print """================\n=== SOLUCION ===\n================"""
        print '%-20s %-4s' % ('Mensaje de salida: ', estados[self.estado])
        if (self.estado != 5 and self.estado != None):
            print '%-20s %-4s' % ('Raiz encontrada: ', '%.6f' % self.raiz)
            print '%-20s %-4s' % ('Error: ',  '%.6f' % self.error)
            print '%-20s %-4d' % ('Iteraciones: ', self.iteraciones)
        print '\n'

##########################################################################################
##########################################################################################
def funcion(f,x):
    variable = {'x': x}   
    try:
        return eval(f,{'math':math},variable)
    except SyntaxError:
        print 'Funcion mal formada'
        return None

        
def Biseccion(f,xi, xd, tolerancia, iteraciones):
    solucion = Solucion()
    if funcion(f,xi) * funcion(f,xd) < 0:
        xrant = 0
        while solucion.estado is None: #Mientras no se encuentre la raíz.
            xr = (xi + xd) / 2.0 
            solucion.iteraciones += 1
            if abs(funcion(f,xr)) < tolerancia:
                solucion.actualizar(xr, funcion(f,xr), 0) #xr es raíz.
            else:
                error = abs((xr - xrant) / xr)
                if error < tolerancia:
                    solucion.actualizar(xr, error, 4)
                elif solucion.iteraciones == iteraciones:
                    solucion.actualizar(None, None, 3) #Se alcanzó las iteraciones máximas.
                else:
                    xrant = xr
                    
            if (funcion(f,xi) * funcion(f,xr)) < 0:
                xd = xr
            else:
                xi = xr
 
    elif abs(funcion(f,xi)) < tolerancia:
        # la raiz es xi
        solucion.actualizar(xi, abs(funcion(f,xi)), 1)
    elif abs(funcion(f,xd)) < tolerancia:
        # la raiz es xd
        solucion.actualizar(xd, abs(funcion(f,xd)), 2)
    elif funcion(f,xi) * funcion(f,xd) > 0:
        solucion.actualizar(None, None, 5) #El intervalo no contiene a la raíz.
        
    return solucion

##########################################################################################
##########################################################################################

def ReglaFalsa(f, xi, xd, tolerancia=0.0001, iteraciones=100):
    solucion= Solucion()
    if funcion(f,xi) * funcion(f,xd) < 0:
        xrant = 0        
        while solucion.estado is None:
            xr = (funcion(f,xd)*xi - funcion(f,xi)*xd)/(funcion(f,xd) - funcion(f,xi)) 
            solucion.iteraciones += 1
            if abs(funcion(f,xr)) < tolerancia:
                solucion.actualizar(xr, funcion(f,xr), 0)
            else:
                error = abs((xr - xrant) / xr)

                if error < tolerancia:
                    solucion.actualizar(xr, error, 4)
                elif solucion.iteraciones == iteraciones:
                    solucion.actualizar(None, None, 3)
                else:
                    xrant = xr
                    
            if (funcion(f,xi) * funcion(f,xr)) < 0:
                xd = xr
            else:
                xi = xr
    
    elif abs(funcion(f,xi)) < tolerancia:
        # la raiz es xi
        solucion.actualizar(xi, abs(funcion(f,xi)), 1)
    elif abs(funcion(f,xd)) < tolerancia:
        # la raiz es xd
        solucion.actualizar(xd, abs(funcion(f,xd)), 2)
    elif funcion(f,xi) * funcion(f,xd) > 0:
        solucion.actualizar(None, None, 5)
            
    return solucion

##########################################################################################
##########################################################################################

def Secante(f, x0, x1,  tolerancia=0.0001, iteraciones=100):
    solucion = Solucion()
    while solucion.estado is None:
        xr = (funcion(f,x1)*x0 - funcion(f,x0)*x1)/(funcion(f,x1) - funcion(f,x0))
        solucion.iteraciones += 1
        if abs(funcion(f,xr)) < tolerancia:
            solucion.actualizar(xr, funcion(f,xr), 0)
        else:
            error = abs((xr - x1)/xr)
            if error < tolerancia:
                solucion.actualizar(xr, error, 4)
            elif solucion.iteraciones == iteraciones:
                solucion.actualizar(None, None, 3)
            else:
                x0 = x1
                x1 = xr

    return solucion

##########################################################################################
##########################################################################################

def Tangente(f, xi, tolerancia= 0.0001, iteraciones= 100):
    def df(f,x):
        return ( funcion(f,(x +0.00001))- funcion(f, x))/ 0.00001
    solucion = Solucion()
    while solucion.estado is None:
            xr = xi - funcion(f,xi)/df(f,xi)
            solucion.iteraciones += 1
            if abs(funcion(f,xr)) < tolerancia:
                solucion.actualizar(xr, funcion(f,xr), 0)
            else:
                error = abs((xr - xi) / xr)

                if error < tolerancia:
                    solucion.actualizar(xr, error, 4)
                elif solucion.iteraciones == iteraciones:
                    solucion.actualizar(None, None, 3)
                else:
                    xi=xr
                    
    return solucion

##########################################################################################
##########################################################################################

def PuntoFijo():
    solucion = Solucion()

    return solucion

estados = {0: 'Se encontro la raiz de la funcion.',
           1: 'La raiz de la funcion es xi.',
           2: 'La raiz de la funcion es xd.',
           3: 'Alcanzo iteraciones maximas.',
           4: 'La diferencia en iteraciones seguidas menor a la tolerancia.',
           5: 'No se puede garantizar que la raiz este entre [xi,xd].',
           6: 'La derivada en un punto de xr = 0',
           None: 'Sin solucion.'}

