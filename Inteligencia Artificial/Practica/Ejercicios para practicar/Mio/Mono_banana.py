from simpleai.search import SearchProblem, breadth_first, depth_first, astar, greedy
from simpleai.search.viewers import BaseViewer
import random

inicial = (random.randint(0, 19), random.randint(0, 19))

bananas = tuple(random.sample(range(0, 19), 5))

class Mono_banana(SearchProblem):
    def cost(self, state1, action, state2):
        return 1 if len(action) == 1 else 2

    def is_goal(self, state):
        return state[0] == state[1] and state[0] in bananas

    def actions(self, state):
        acciones = []
        pos_mono, pos_silla = state

        if pos_mono < 20:
            acciones.append((pos_mono + 1, pos_silla))
            if (pos_mono + 1 == pos_silla and pos_silla + 1 != 20) or (pos_mono - 1 == pos_silla and pos_mono + 1 != 20):
                acciones.append((pos_mono + 1, pos_silla + 1))

        if pos_mono > 0:
            acciones.append((pos_mono - 1, pos_silla))
            if (pos_mono - 1 == pos_silla and pos_silla - 1 != 0) or (pos_mono + 1 == pos_silla and pos_mono - 1 != 0):
                acciones.append((pos_mono - 1, pos_silla - 1))

        return acciones

    def result(self, state, action):
        return action

    def heuristic(self, state):
        distancias = []
        pos_mono, pos_silla = state
        for banana in bananas:
            distancias.append(abs(abs(pos_mono - pos_silla) - banana))

        return min(distancias)

if __name__ == '__main__':
    problema = Mono_banana(inicial)
    resultado = astar(problema, True)

    print 'Mono:', inicial[0]
    print 'Silla:', inicial[1]
    print 'Bananas:', bananas
    print 'Resultado:', resultado.state
