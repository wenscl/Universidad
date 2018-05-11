from simpleai.search import (SearchProblem,
                             uniform_cost,
                             breadth_first,
                             depth_first,
                             astar,
                             )

inicial = (
    (5, 2, 8, 4),
    (),
)

peso = 10
costo = 5

class Bolsas_Problem(SearchProblem):
    def cost(self, state, action, state2):
        return costo if len(state[1]) != len(state2[1]) else 0

    def is_goal(self, state):
        return len(state[0]) == 0

    def actions(self, state):
        acciones = []
        objetos_restantes, bolsas = state
        for objeto in objetos_restantes:
            acciones.append((objeto, len(bolsas)))
            for indice, bolsa in enumerate(bolsas):
                if sum(bolsa) + objeto <= peso:
                    acciones.append((objeto, indice))

        return acciones

    def result(self, state, action):
        objeto, num_bolsa = action
        objetos_restantes, bolsas = state
        objetos_restantes = list(objetos_restantes)
        bolsas = list(list(x) for x in bolsas)
        objetos_restantes.remove(objeto)
        if num_bolsa == len(bolsas):
            bolsas.append([objeto])
        else:
            bolsas[num_bolsa].append(objeto)
        bolsas = tuple(tuple(x) for x in bolsas)

        return tuple(objetos_restantes), bolsas

if __name__ == '__main__':
    problema = Bolsas_Problem(inicial)
    result_breadth_first = breadth_first(problema, True)
    result_depth_first = depth_first(problema, True)
    result_astar = astar(problema, True)
    result_uniform_cost = uniform_cost(problema, True)

    def imprimir_acciones(resultado):

        for accion, estado in resultado.path():
            if accion is not None:
                print '\tAccion: colocar objeto {0} en la bolsa {1}'.format(accion[0], accion[1])
        print '\tEstado Final: ', resultado.state, '\n'

    print "Uniform Cost:"
    imprimir_acciones(result_uniform_cost)
    print "Breadth First:"
    imprimir_acciones(result_breadth_first)
    print "Depth First:"
    imprimir_acciones(result_depth_first)
    print "A*:"
    imprimir_acciones(result_astar)
