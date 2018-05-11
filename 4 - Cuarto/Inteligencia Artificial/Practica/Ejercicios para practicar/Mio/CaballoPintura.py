from simpleai.search import breadth_first, SearchProblem, astar, greedy
from simpleai.search.viewers import WebViewer

inicial = (0, 0)

posibles = ((x, y) for x in range(3) for y in range(4))

movimientos = ((+2, +1), (+2, -1), (-2, +1), (-2, -1), (+1, -2), (+1, +2), (-1, -2), (-1, +2))

def se_puede_mover(fila_actual, columna_actual):
    casillas_posibles = []
    for x in movimientos:
        fila, columna = x
        if (fila_actual + fila, columna_actual + columna) in posibles:
            casillas_posibles.append((fila_actual + fila, columna_actual + columna))

    return casillas_posibles

class CaballoPintura(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        return state == posibles

    def actions(self, state):
        acciones = []
        pintados = state

        for fila_casilla in range(4):
            for columna_casilla in range(3):
                if (fila_casilla, columna_casilla) not in pintados:
                    casillas = se_puede_mover(fila_casilla, columna_casilla)
                    acciones.append(((fila_casilla, columna_casilla), casillas))

        return acciones

    def result(self, state, action):
        casilla_actual, casilla_destino = action
        state = list(state)
        state.append(casilla_destino)
        state = tuple(state)

        return state

    def heuristic(self, state):
        count = 0
        for fila in range(3):
            for columna in range(4):
                if (fila, columna) not in state:
                    count += 1

        return count


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
