from simpleai.search import SearchProblem, breadth_first, depth_first, astar, greedy
from simpleai.search.viewers import WebViewer

inicial = ((0, 0),)

def puede_ir(posicion0, posicion1, state):
    return (posicion0 < 8 and posicion0 >= 0) and (posicion1 < 8 and posicion1 >= 0) and (posicion0, posicion1) not in state

class Tour_caballero(SearchProblem):
    def cost(self, state1, accion, state2):
        return 1

    def is_goal(self, state):
        return len(state) == 64

    def actions(self, state):
        acciones = []
        fila, columna = state[-1]

        if puede_ir(fila + 1, columna + 2, state):
            acciones.append((fila + 1, columna + 2))
        if puede_ir(fila - 1, columna + 2, state):
            acciones.append((fila - 1, columna + 2))
        if puede_ir(fila + 2, columna + 1, state):
            acciones.append((fila + 2, columna + 1))
        if puede_ir(fila - 2, columna + 1, state):
            acciones.append((fila - 2, columna + 1))
        if puede_ir(fila + 2, columna - 1, state):
            acciones.append((fila + 2, columna - 1))
        if puede_ir(fila - 2, columna - 1, state):
            acciones.append((fila - 2, columna - 1))
        if puede_ir(fila + 1, columna - 2, state):
            acciones.append((fila + 1, columna - 2))
        if puede_ir(fila - 1, columna - 2, state):
            acciones.append((fila - 1, columna - 2))

        return acciones

    def result(self, state, action):
        state = list(state)
        state.append(action)
        state = tuple(state)
        return state

    def heuristic(self, state):
        return 64 - len(state)

if __name__ == '__main__':
    problema = Tour_caballero(inicial)
    resultado = astar(problema, True)
    print 'State: ', resultado.state
    print 'Depth: ', resultado.depth
    print 'Cost: ', resultado.cost