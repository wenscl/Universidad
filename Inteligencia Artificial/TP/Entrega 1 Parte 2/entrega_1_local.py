from simpleai.search import SearchProblem, hill_climbing, hill_climbing_stochastic, beam, hill_climbing_random_restarts, simulated_annealing
from simpleai.search.viewers import BaseViewer, WebViewer
import random

inicial = tuple((nro_fila, nro_columna) for nro_fila in range (3) for nro_columna in range(10))

def cantidad_amenazas(state, indice_fila, indice_columna):
    # Calculamos la cantidad de soldados que atacan la casilla
    cant_soldados = 0
    if (indice_fila + 1, indice_columna) in state:
        cant_soldados += 1
    if (indice_fila - 1, indice_columna) in state:
        cant_soldados += 1
    if (indice_fila, indice_columna + 1) in state:
        cant_soldados += 1
    if (indice_fila, indice_columna - 1) in state:
        cant_soldados += 1
    return cant_soldados

def t2l(t):
    return list(r for r in t)

def l2t(l):
    return tuple(r for r in l)

class Hnefatafl(SearchProblem):
    def value(self, state):
        puntaje = 0
        casillas_vacias = [(fila, columna) for fila in range(10) for columna in range(10) if (fila, columna) not in state]

        for casilla_vacia in casillas_vacias:
            if cantidad_amenazas(state, casilla_vacia[0], casilla_vacia[1]) > 1:
                if casilla_vacia[0] in [0, 9] or casilla_vacia[1] in [0, 9]:
                    puntaje += 3
                else:
                    puntaje += 1

        return puntaje

    def generate_random_state(self):
        estado = []
        for i in range(30):
            while True:
                fila = random.randint(0, 9)
                columna = random.randint(0, 9)
                if (fila, columna) not in estado:
                    estado.append((fila, columna))
                    break

        return estado

    def actions(self, state):
        acciones = []
        casillas_vacias = [(fila, columna) for fila in range(10) for columna in range(10) if (fila, columna) not in state]
        for soldado in state:
            for casilla_vacia in casillas_vacias:
                acciones.append((soldado, casilla_vacia))

        return acciones

    def result(self, state, action):
        inicio_soldado, destino_soldado = action

        state = t2l(state)
        state.remove(inicio_soldado)
        state.append(destino_soldado)
        state = l2t(state)

        return state

def resolver(metodo_busqueda, iteraciones, haz, reinicios):
    problema_hnefatafl = Hnefatafl(inicial)

    if metodo_busqueda == 'hill_climbing':
        return hill_climbing(problema_hnefatafl, iterations_limit=iteraciones)
    elif metodo_busqueda == 'hill_climbing_stochastic':
        return hill_climbing_stochastic(problema_hnefatafl, iterations_limit=iteraciones)
    elif metodo_busqueda == 'beam':
        return beam(problema_hnefatafl, beam_size=haz, iterations_limit=iteraciones)
    elif metodo_busqueda == 'hill_climbing_random_restarts':
        return hill_climbing_random_restarts(problema_hnefatafl, restarts_limit=reinicios, iterations_limit=iteraciones)
    elif metodo_busqueda == 'simulated_annealing':
        return simulated_annealing(problema_hnefatafl, iterations_limit=iteraciones)

if __name__ == '__main__':
    problema = Hnefatafl(inicial)

    def imprimirtablero(resultado_imprimir, visor_imprimir):
        print 'Stats: ', visor_imprimir.stats
        print 'Tablero: '
        for num_fila in range(10):
            for num_columna in range(11):
                print '|X' if (num_fila, num_columna) in resultado_imprimir.state else '| ',
            print
        print 'Posiciones: ', resultado_imprimir.state
        print 'Puntaje: ', resultado_imprimir.value

    for i in range(2):
        # Caso 1: Busqueda de ascenso de colina, con limite de 200 iteraciones.
        print '\nCaso 1'
        # visor = BaseViewer()
        resultado = hill_climbing(problema, iterations_limit=200) #, viewer=visor)
        # imprimirtablero(resultado, visor)
        print 'Puntaje: ', resultado.value

    for i in range(2):
        # Caso 2: Busqueda en ascenso de colina, variante estocastica (hill_climbing_stochastic), con limite de 200 iteraciones.
        print '\nCaso 2'
        # visor = BaseViewer()
        resultado = hill_climbing_stochastic(problema, iterations_limit=200) #, viewer=visor)
        # imprimirtablero(resultado, visor)
        print 'Puntaje: ', resultado.value

    for i in range(2):
        # Caso 3: Busqueda de haz local, con haz de tamanio 20 y limite de 200 iteraciones.
        print '\nCaso 3'
        # visor = BaseViewer()
        resultado = beam(problema, beam_size=20, iterations_limit=200) #, viewer=visor)
        # imprimirtablero(resultado, visor)
        print 'Puntaje: ', resultado.value

    for i in range(2):
        # Caso 4: Busqueda de ascenso de colina con reinicios aleatorios, con 20 reinicios y limite de 200 iteraciones.
        print '\nCaso 4'
        # visor = BaseViewer()
        resultado = hill_climbing_random_restarts(problema, restarts_limit=20, iterations_limit=200) #, viewer=visor)
        # imprimirtablero(resultado, visor)
        print 'Puntaje: ', resultado.value

    for i in range(2):
        # Caso 5: Busqueda de temple simulado, con limite de 200 iteraciones.
        print '\nCaso 5'
        # visor = BaseViewer()
        resultado = simulated_annealing(problema, iterations_limit=200) #, viewer=visor)
        # imprimirtablero(resultado, visor)
        print 'Puntaje: ', resultado.value
