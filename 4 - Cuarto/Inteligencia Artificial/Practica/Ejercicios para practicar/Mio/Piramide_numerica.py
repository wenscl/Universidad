from simpleai.search import (CspProblem, backtrack, min_conflicts)
import itertools

variables = list('ABCDEFGHIJ')

dominios = {variable: range(1, 51) for variable in variables}
dominios['A'] = [48]
dominios['G'] = [5]
dominios['H'] = [8]
dominios['J'] = [3]

def Suma(variables, valores):
    return valores[0] == valores[1] + valores[2]

def distintos(variables, valores):
    return valores[0] != valores[1]

restricciones = []

for variable1, variable2 in itertools.combinations(variables, 2):
    restricciones.append(((variable1, variable2), distintos))

restricciones.append((('A', 'B', 'C'), Suma))
restricciones.append((('B', 'D', 'E'), Suma))
restricciones.append((('C', 'E', 'F'), Suma))
restricciones.append((('D', 'G', 'H'), Suma))
restricciones.append((('E', 'H', 'I'), Suma))
restricciones.append((('F', 'I', 'J'), Suma))

if __name__ == '__main__':
    problema = CspProblem(variables, dominios, restricciones)
    resultado = backtrack(problema)
    print resultado

    resultado = min_conflicts(problema, iterations_limit=500)
    print resultado