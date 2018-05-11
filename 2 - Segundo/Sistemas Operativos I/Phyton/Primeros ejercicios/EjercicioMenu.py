def hola_mundo():
    return 'Hola mundo'

def invertir_texto(texto):
    return texto[::-1]

def operaciones(numero):
    lista = [numero-2, numero+2, numero*2, numero/2, numero/2.0, numero**2]
    return lista

def pot_menores(numero, maximo):
    i = 0
    lista = []
    while numero**i < maximo:
        lista.append(str(numero**i).zfill(4))
        i += 1
    return lista
	
def triangulo(texto):
    cant = len(texto)
    i = 1
    lista = []
    while i < cant:
        lista.append(texto[:i])
        i+=1
    while i>0:
        lista.append(texto[:i])
        i -=1
    return lista
	
def suma_nat(maximo, multiplos):
    i = 1
    s = 0
    b = 0
    while i < maximo:
        for e in multiplos:
            if i%e == 0 and b == 0:
                s = s + i
                b = 1
        i += 1
        b = 0
    return s
	
def suerte(numero, minimo, maximo):
    if numero == minimo:
        return 'Suerte'
    elif numero > maximo:
        return 'Grande'
    else:
        return 'Sin suerte'
    
def menu():
    print """Elija una opcion
1- Imprimir 'Hola mundo'
2- Mostrar un texto al reves
3- Hacer operaciones con un numero
4- Mostrar las potencias de un numero menores a un maximo
5- Mostrar un triangulo creciente y decreciente de un texto
6- Mostrar la suma de los multiplos ingresados menores a un maximo
7- Preguntar un numero al usuario y ver su suerte"""
    a = raw_input('Opcion: ')
    if a == '1':
        print hola_mundo()
    elif a == '2':
        texto = raw_input('Ingrese un texto: ')
        print invertir_texto(texto)
    elif a == '3':
        numero = raw_input('Ingrese un numero: ')
        for e in operaciones(int(numero)):
            print e
    elif a == '4':
        numero = raw_input('Ingrese un numero: ')
        maximo = raw_input('Ingrese un maximo: ')
        for e in pot_menores(int(numero), int(maximo)):
            print e
    elif a == '5':
        texto = raw_input('Ingrese un texto: ')
        for e in triangulo(texto):
            print e
    elif a == '6':
        maximo = raw_input('Ingrese un maximo: ')
        numero = int(raw_input("""Ingrese los numeros que desee. La carga termina con un 0
-> """))
        multiplos = []
        while numero <> 0:
            multiplos.append(numero)
            numero = int(raw_input('-> '))
        print suma_nat(int(maximo), multiplos)        
    elif a == '7':
        numero = raw_input('Ingrese un numero: ')
        minimo = raw_input('Ingrese un minimo: ')
        maximo = raw_input('Ingrese un maximo: ')
        print suerte(int(numero), int(minimo), int(maximo))
menu()
