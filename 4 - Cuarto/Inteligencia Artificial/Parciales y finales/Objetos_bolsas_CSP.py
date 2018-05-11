from simpleai.search import CspProblem, backtrack
import itertools

#Variables
bolsas = (1, 2)

PESO_MAX = 10

#Dominios
objetos = [5, 2, 8, 4]
dominios = {}
for bolsa in bolsas:
    lista_dominio = []
    for index in range(1, len(objetos)):
        for combinacion in itertools.combinations(objetos, index):
            lista_dominio.append(combinacion)
    dominios[bolsa] = lista_dominio

#Restricciones
restricciones = []

#Los objetos de cada bolsa no pueden superar el peso maximo
def no_supera_peso_max(variables, valores):
    return sum([x for y in valores for x in y]) <= PESO_MAX

restricciones.append(((bolsas[0],), no_supera_peso_max)) #Unaria
restricciones.append(((bolsas[1],), no_supera_peso_max)) #Unaria

#Los objetos no deben repetirse
def no_repetidos(variables, valores):
    return not len([x for x in valores[0] if x in valores[1]]) > 0

restricciones.append(((bolsas[0], bolsas[1]), no_repetidos)) #Binaria (aunque por ser las unicas dos, capaz se considera global)

#Todos los objetos deben estar en una bolsa
def estan_todos(variables, valores):
    return len(valores[0]) + len(valores[1]) == len(objetos)

restricciones.append(((bolsas[0], bolsas[1]), estan_todos)) #Binaria (aunque por ser las unicas dos, capaz se considera global)

if __name__ == '__main__':
    problema = CspProblem(bolsas, dominios, restricciones)
    resultado = backtrack(problema)
    print resultado
