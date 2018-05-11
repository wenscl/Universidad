from Modulo1 import hola_mundo, invertir_texto, operaciones 
from Modulo2 import pot_menores, triangulo, suma_nat, suerte
    
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
