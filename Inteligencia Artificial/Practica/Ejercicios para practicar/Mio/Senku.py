from simpleai.search import SearchProblem, breadth_first, depth_first, astar, greedy
from simpleai.search.viewers import ConsoleViewer

no_casillas = (
    (0, 0), (0, 1), (0, 5), (0, 6),
    (1, 0), (1, 1), (1, 5), (1, 6),
    (5, 0), (5, 1), (5, 5), (5, 6),
    (6, 0), (6, 1), (6, 5), (6, 6),
    (3, 3),
)

inicial = tuple((x,y) for x in range(7) for y in range(7) if (x,y) not in no_casillas)

def hay_ficha(tupla0, tupla1, state):
    return tupla0 in state and tupla1 not in state

class Senku(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        return len(state) == 1

    def actions(self, state):
        acciones = []

        for tupla in state:
            if hay_ficha((tupla[0] + 1, tupla[1]), (tupla[0] - 1, tupla[1]), state):
                acciones.append((tupla, (tupla[0] + 1, tupla[1]), (tupla[0] - 1, tupla[1])))
            if hay_ficha((tupla[0] - 1, tupla[1]), (tupla[0] + 1, tupla[1]), state):
                acciones.append((tupla, (tupla[0] - 1, tupla[1]), (tupla[0] + 1, tupla[1])))
            if hay_ficha((tupla[0], tupla[1] + 1), (tupla[0], tupla[1] + 1), state):
                acciones.append((tupla, (tupla[0], tupla[1] + 1), (tupla[0], tupla[1] + 1)))
            if hay_ficha((tupla[0], tupla[1] - 1), (tupla[0], tupla[1] - 1), state):
                acciones.append((tupla, (tupla[0], tupla[1] - 1), (tupla[0], tupla[1] - 1)))

        return acciones

    def result(self, state, action):
        actual, atras, adelante = action
        state = list(state)
        state.append(adelante)
        state.remove(atras)
        state.remove(actual)
        state = tuple(state)

        return state

    def heuristic(self, state):
        return len(state) - 1

if __name__ == '__main__':
    problema = Senku(inicial)
    resultado = astar(problema, True)
    print resultado.state