from simpleai.search import SearchProblem, breadth_first, depth_first, astar, greedy
from simpleai.search.viewers import BaseViewer

soldados = (
    (0,0), (0,2), (0,4), (0,6),
    (1,4),
    (2,0),
    (3,1), (3,6), (3,7), (3,9),
    (4,0), (4,7), (4,8),
    (5,4), (5,9),
    (6,0), (6,5), (6,9),
    (7,0), (7,7),
    (8,2), (8,4), (8,9),
    (9,1), (9,4), (9,6), (9,7)
)

def esta_amenazado(indice_fila, indice_columna):
    # Verificamos que el espacio no este amenazado por mas de 1 soldado
    cant_soldados = 0
    if (indice_fila + 1, indice_columna) in soldados:
        cant_soldados += 1
    if (indice_fila - 1, indice_columna) in soldados:
        cant_soldados += 1
    if (indice_fila, indice_columna + 1) in soldados:
        cant_soldados += 1
    if (indice_fila, indice_columna - 1) in soldados:
        cant_soldados += 1
    return cant_soldados > 1

def puede_ir(indice_fila, indice_columna):
    # Verificamos que el espacio al que se quiere mover el Rey este vacio y sin amenaza
    if (indice_fila, indice_columna) not in soldados:
        return not esta_amenazado(indice_fila, indice_columna)
    else:
        return False

class Hnefatafl(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        fila_rey, col_rey = state

        # Si el Rey se encuentra en algun borde y no se halla amenazado por mas de un soldado, el estado es meta
        return fila_rey == 0 or fila_rey == 9 or col_rey == 0 or col_rey == 9

    def actions(self, state):
        acciones = []

        fila_rey, col_rey = state

        # Agregamos las coordenadas de las casillas a las que el Rey puede moverse
        if puede_ir(fila_rey - 1, col_rey):
            acciones.append((fila_rey - 1, col_rey))
        if puede_ir(fila_rey + 1, col_rey):
            acciones.append((fila_rey + 1, col_rey))
        if puede_ir(fila_rey, col_rey - 1):
            acciones.append((fila_rey, col_rey - 1))
        if puede_ir(fila_rey, col_rey + 1):
            acciones.append((fila_rey, col_rey + 1))

        return acciones

    def result(self, state, action):
        return action

    def heuristic(self, state):
        fila_rey, col_rey = state

        # Retornamos la distancia a la casilla mas cercana que sea un destino posible (que este vacia y no este amenazada por mas de un soldado)
        return min([abs(x-fila_rey) + abs(y-col_rey)
                     for x in range(10) for y in range(10)
                     if (x in [0, 9] or y in [0, 9]) and ((x, y) not in soldados and not esta_amenazado(x, y))])

def resolver(metodo_busqueda, posicion_rey, controlar_estados_repetidos):
    problem = Hnefatafl(posicion_rey)
    result = None
    if metodo_busqueda == 'breadth_first':
        # ejecutar el metodo de busqueda en amplitud
        result = breadth_first(problem, graph_search=controlar_estados_repetidos)
    elif metodo_busqueda == 'depth_first':
        # ejecutar el metodo de busqueda en profundidad
        result = depth_first(problem, graph_search=controlar_estados_repetidos)
    elif metodo_busqueda == 'astar':
        # ejecutar el metodo A*
        result = astar(problem, graph_search=controlar_estados_repetidos)
    elif metodo_busqueda == 'greedy':
        # ejecutar el metodo de busqueda avara
        result = greedy(problem, graph_search=controlar_estados_repetidos)

    return result

def imprimir_stats(visor_usado, resultado_problema):
    estadisticas = []
    for x in visor_usado.stats:
        estadisticas.append('{0}: {1}'.format(x, visor_usado.stats[x]))
    estadisticas.append('Profundidad: {0}'.format(resultado_problema.depth))
    estadisticas.append('Costo: {0}'.format(resultado_problema.cost))

    print 'Resultado: {0}'.format(resultado_problema.state)
    print estadisticas[0], '\n', estadisticas[3], '\n', estadisticas[4], '\n', estadisticas[2], '\n'

if __name__ == '__main__':
    problema_hnefatafl = Hnefatafl((5,3))

    # Caso 1: Busqueda en amplitud, en arbol, partiendo con el rey en la posicion (5, 3).
    # visor = BaseViewer()
    # print 'Caso 1:'
    # imprimir_stats(visor, breadth_first(problema_hnefatafl, graph_search=False, viewer=visor))

    # Caso 2: Busqueda en amplitud, en grafo, partiendo con el rey en la posicion (5, 3).
    visor = BaseViewer()
    print 'Caso 2:'
    imprimir_stats(visor, breadth_first(problema_hnefatafl, graph_search=True, viewer=visor))

    # Caso 3: Busqueda en profundidad, en arbol, partiendo con el rey en la posicion (5, 3).
    # visor = BaseViewer()
    # print 'Caso 3:'
    # imprimir_stats(visor, depth_first(problema_hnefatafl, graph_search=False, viewer=visor))

    # Caso 4: Busqueda en profundidad, en grafo, partiendo con el rey en la posicion (5, 3).
    visor = BaseViewer()
    print 'Caso 4:'
    imprimir_stats(visor, depth_first(problema_hnefatafl, graph_search=True, viewer=visor))

    # Caso 5: Busqueda avara, en arbol, partiendo con el rey en la posicion (5, 3).
    # visor = BaseViewer()
    # print 'Caso 5:'
    # imprimir_stats(visor, greedy(problema_hnefatafl, graph_search=False, viewer=visor))

    # Caso 6: Busqueda avara, en grafo, partiendo con el rey en la posicion (5, 3).
    visor = BaseViewer()
    print 'Caso 6:'
    imprimir_stats(visor, greedy(problema_hnefatafl, graph_search=True, viewer=visor))

    # Caso 7: Busqueda A*, en arbol, partiendo con el rey en la posicion (5, 3).
    visor = BaseViewer()
    print 'Caso 7:'
    imprimir_stats(visor, astar(problema_hnefatafl, graph_search=False, viewer=visor))

    # Caso 8: Busqueda A*, en grafo, partiendo con el rey en la posicion (5, 3).
    visor = BaseViewer()
    print 'Caso 8:'
    imprimir_stats(visor, astar(problema_hnefatafl, graph_search=True, viewer=visor))
