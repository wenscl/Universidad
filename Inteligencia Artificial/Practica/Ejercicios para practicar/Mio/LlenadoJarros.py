from simpleai.search import SearchProblem, breadth_first, astar, greedy
from simpleai.search.viewers import WebViewer

inicial = (0, 0, 0, 4)

meta = (1, 1, 1, 1)

def capacidad(jarro, litros):
    return jarro + 1 - litros

# def t2l(tupla):
#     return tuple(tuple(x) for x in tupla)
#
# def l2t(lista):
#     return list(list(x) for x in lista)

class CaballoPintura(SearchProblem):
    def cost(self, state1, action, state2):
        return action[0] + 1

    def is_goal(self, state):
        return state == meta

    def actions(self, state):
        acciones = []
        for jarro_origen in range(4):
            for jarro_destino in range(4):
                if state[jarro_origen] > 0 and capacidad(jarro_destino, state[jarro_destino]) > 0:
                    acciones.append((jarro_origen, jarro_destino))

        return acciones

    def result(self, state, action):
        jarro_origen, jarro_destino = action
        litros_origen, litros_destino = state[jarro_origen], state[jarro_destino]
        litros = min(litros_origen, capacidad(jarro_destino, litros_destino))

        state = list(state)
        state[jarro_origen] -= litros
        state[jarro_destino] += litros
        state = tuple(state)
        return state

    def heuristic(self, state):
        # Heuristica: Cantidad de jarros vacios
        jarros_vacios = 0
        if 0 in state:
            jarros_vacios += 1

        return jarros_vacios


if __name__ == '__main__':
    problema = CaballoPintura(inicial)

    #resultado = astar(problema, viewer=WebViewer())
    resultado = astar(problema, graph_search=True)

    print 'Estado meta:'
    print resultado.state
    print 'Camino:'
    print len(resultado.path())
    for accion, estado in resultado.path():
        print 'Movimiento', accion
        print 'Llegue a', estado
