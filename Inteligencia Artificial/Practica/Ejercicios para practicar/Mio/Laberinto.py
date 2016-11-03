from simpleai.search import SearchProblem, astar, breadth_first

inicial = 1
meta = 21

caminos = {
    1: (9, 12),
    2: (3, 5, 6, 7),
    3: (2, 4, 8),
    4: (3, 8, 21),
    5: (2, 6),
    6: (2, 5, 9),
    7: (2, 9),
    8: (3, 4, 10),
    9: (1, 6, 7, 12),
    10: (8, 11, 15),
    11: (10),
    12: (1, 9, 14, 17),
    13: (14, 17, 19),
    14: (12, 13),
    15: (10, 16, 18),
    16: (15, 20),
    17: (12, 13, 19),
    18: (15),
    19: (13, 17, 20),
    20: (16, 19)
}

class Laberinto(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        return state == meta

    def actions(self, state):
        return caminos[state]

    def result(self, state, action):
        return action

    def heuristic(self, state):
        # No se me ocurrio otra cosa mejor.
        if state == meta:
            return 0
        elif meta in caminos[state]:
            return 1
        else:
            return 2

if __name__ == '__main__':
    problem = Laberinto(inicial)

    result = breadth_first(problem=problem, graph_search=True)
    print result.cost
    print result.path()
    print result.state

    result = astar(problem=problem, graph_search=True)
    print result.cost
    print result.path()
    print result.state
