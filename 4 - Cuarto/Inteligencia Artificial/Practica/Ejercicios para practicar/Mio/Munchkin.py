from simpleai.search import (CspProblem, backtrack, min_conflicts)

variables = (1, 2, 3)

cartas = [
    ('A', 'Madera', 'Armadura de madera', 1, 800),
    ('A', 'Hierro', 'Armadura de hierro', 3, 1000),
    ('A', 'Acero', 'Armadura de acero', 5, 1300),
    ('W', 'Madera', 'Espada de madera', 1, 500),
    ('W', 'Hierro', 'Espada de hierro', 2, 700),
    ('W', 'Acero', 'Espada de acero', 4, 1000),
    ('W', 'Madera', 'Garrote gigante de madera', 6, 1300),
    ('P', 'Fuego', 'Pocion de fuego', 5, 1500),
    ('P', 'Hielo', 'Pocion de hielo', 2, 800),
    ('P', 'Acido', 'Pocion de acido', 3, 1200),
]

dominios= {x: cartas for x in variables}

def una_armadura(variables, valores):
    return len([x for x in valores if x[0] == 'A']) <= 1

def un_arma(variables, valores):
    return len([x for x in valores if x[0] == 'W']) <= 1

def monto(variables, valores):
    return sum([x[4] for x in valores]) <= 3000

def fuego_madera(variables, valores):
    return not (any([x for x in valores if x[1] == 'Madera']) and any([x for x in valores if x[1] == 'Fuego']))

def bonificacion(variables, valores):
    return sum([x[3] for x in valores]) >= 15

restricciones = []
#   * Solo se puede tener 1 armadura
restricciones.append(((1, 2, 3), una_armadura))
#   * Solo se puede tener 1 arma de mano (espada o garrote)
restricciones.append(((1, 2, 3), un_arma))
#   * Solo se dispone de 3000 de oro para gastar (es decir, el valor de las cartas sumadas no puede superar ese monto)
restricciones.append(((1, 2, 3), monto))
#   * No se pueden mezclar cartas de objetos de fuego con cartas de objetos de madera
restricciones.append(((1, 2, 3), fuego_madera))
#   * Se tiene que lograr un bonificador total (sumando las cartas) mayor a +15
restricciones.append(((1, 2, 3), bonificacion))

def print_resultado(resultado):
    costo_total = 0
    bonus_total = 0
    for key, value in resultado.iteritems():
        print '   * Espacio {0}: "{1}" (+{2}) - Costo: ${3}'.format(key, value[2], value[3], value[4])
        costo_total += value[4]
        bonus_total += value[3]
    print 'Costo total: ${0}'.format(costo_total)
    print 'Bonificacion total: +{0}'.format(bonus_total)

if __name__ == '__main__':
    problema = CspProblem(variables, dominios, restricciones)
    resultado = backtrack(problema)
    print 'Backtrack:'
    if resultado is not None:
        print_resultado(resultado)
    else:
        print "No se ha encontrado solucion."
    print
    resultado = min_conflicts(problema, iterations_limit=10)
    print 'min conflicts:'
    if resultado is not None:
        print_resultado(resultado)
    else:
        print "No se ha encontrado solucion."