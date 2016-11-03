import itertools

from simpleai.search import (CspProblem, backtrack, 
                             MOST_CONSTRAINED_VARIABLE, 
                             LEAST_CONSTRAINING_VALUE, 
                             HIGHEST_DEGREE_VARIABLE)

reinas = ['r' + str(numero) for numero in range(8)]

dominios = {reina: range(8) for reina in reinas}


def no_atacarse(variables, values):
    reina_a, reina_b = variables
    fila_a, fila_b = values
    columna_a = int(reina_a[1])
    columna_b = int(reina_b[1])

    # misma fila?
    if fila_a == fila_b:
        return False

    # en diagonal?
    if abs(columna_a - columna_b) == abs(fila_a - fila_b):
        return False

    return True



restricciones = []


for reina_a, reina_b in itertools.combinations(reinas, 2):
    restricciones.append(
        ((reina_a, reina_b), no_atacarse)
    )


if __name__ == '__main__':
    problema = CspProblem(reinas, dominios, restricciones)

    resultado = backtrack(problema)
    print resultado

    for fila in range(8):
        for reina in reinas:
            if resultado[reina] == fila:
                print '|*',
            else:
                print '| ',
        print
        print '-' * 40
