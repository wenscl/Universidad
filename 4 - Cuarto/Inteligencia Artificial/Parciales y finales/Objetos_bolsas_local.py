from simpleai.search import SearchProblem, hill_climbing, hill_climbing_stochastic, beam, hill_climbing_random_restarts, simulated_annealing
from simpleai.search.viewers import WebViewer
import random

bolsas = ((5,),(2,),(8,),(4,))

class Objetos_bolsas(SearchProblem):
    def value(self, state):
        return (5 * len([x for x in state if any(x)])) * (-1)

    def actions(self, state):
        acciones = []

        for indice1, bolsa1 in enumerate(state):
            for objeto in bolsa1:
                for indice2, bolsa2 in enumerate(state):
                    if bolsa1 != bolsa2 and sum(bolsa2, objeto) <= 10:
                        acciones.append((objeto, indice1, indice2))

        return acciones

    def result(self, state, action):
        objeto, origen, destino = action
        state = list(list(x) for x in state)
        state[destino].append(objeto)
        state[origen].remove(objeto)
        state = tuple(tuple(x) for x in state)

        return state

    def generate_random_state(self):
        indice1 = random.randint(0, 3)
        indice2 = random.randint(0, 3)
        indice3 = random.randint(0, 3)
        indice4 = random.randint(0, 3)
        state = [[], [], [], []]
        state[indice1].append(5)
        state[indice2].append(2)
        state[indice3].append(8)
        state[indice4].append(4)

        return tuple(tuple(x) for x in state)

if __name__ == '__main__':
    problem = Objetos_bolsas(bolsas)
    result = hill_climbing_stochastic(problem, iterations_limit=500)

    #result = beam(problem, beam_size=10, iterations_limit=20)

    bolsas = tuple(tuple(x) for x in result.state)

    print "Bolsas: {0}".format([x for x in bolsas if any(x)])

    print "Valor: {0}".format(result.value)
