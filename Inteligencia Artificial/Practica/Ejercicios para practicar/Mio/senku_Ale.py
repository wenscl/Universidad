from simpleai.search import SearchProblem, astar

no_casillas = [
    (0, 0), (0, 1), (0, 5), (0, 6),
    (1, 0), (1, 1), (1, 5), (1, 6),
    (5, 0), (5, 1), (5, 5), (5, 6),
    (6, 0), (6, 1), (6, 5), (6, 6),
]

# INICIAL = tuple([(x, y) for x in range(7) for y in range(7) if (x, y) not in no_casillas and (x, y) != (3, 3)])
INICIAL = ((3,1), (3,0),(3,3),(3,5))

class Senku_Problem(SearchProblem):
    def cost(self, state, action, state2):
        return 1

    def is_goal(self, state):
        return len(state) == 1

    def actions(self, state):
        acciones = []
        casillas_vacias = [(x, y) for x in range(7) for y in range(7) if (x, y) not in state and (x, y) not in no_casillas]
        for casilla in casillas_vacias:
            fila_casilla, columna_casilla = casilla
            #accion arriba
            if (fila_casilla - 1, columna_casilla) in state and (fila_casilla - 2, columna_casilla) in state:
                acciones.append(((fila_casilla - 1, columna_casilla), (fila_casilla - 2, columna_casilla), casilla))
            # accion abajo
            if (fila_casilla + 1, columna_casilla) in state and (fila_casilla + 2, columna_casilla) in state:
                acciones.append(((fila_casilla + 1, columna_casilla), (fila_casilla + 2, columna_casilla), casilla))
            # accion izquierda
            if (fila_casilla, columna_casilla - 1) in state and (fila_casilla, columna_casilla - 2) in state:
                acciones.append(((fila_casilla, columna_casilla - 1), (fila_casilla, columna_casilla - 2), casilla))
            # accion derecha
            if (fila_casilla, columna_casilla + 1) in state and (fila_casilla, columna_casilla + 2) in state:
                acciones.append(((fila_casilla, columna_casilla + 1), (fila_casilla, columna_casilla + 2), casilla))

        return acciones

    def result(self, state, action):
        ficha1, ficha2, espacio = action
        state = list(state)
        state.remove(ficha1)
        state.remove(ficha2)
        state.append(espacio)

        return tuple(state)

    def heuristic(self, state):
        return len(state) - 1

    def state_representation(self, state):
        estado = "  0 1 2 3 4 5 6\n"
        for fila in range(7):
            estado += str(fila) + ' '
            for columna in range(7):
                if (fila, columna) in state:
                    estado += "O "
                elif (fila, columna) not in no_casillas:
                    estado += "- "
                else:
                    estado += "  "
            estado += "\n"
        return estado

if __name__ == '__main__':
    problem = Senku_Problem(INICIAL)
    result = astar(problem, graph_search=True)
    for action, state in result.path():
        if action is not None:
            print 'Accion: Mover la ficha en {0} a {1}'.format(str(action[1]), str(action[2]))
        else:
            print 'Accion: Ninguna'
        print 'Tablero:\n{0}\n'.format(problem.state_representation(state))