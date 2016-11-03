from simpleai.search import SearchProblem, breadth_first, depth_first, astar, greedy

inicial = (
	['X', 'di', 2, [(1,2), (2,2)]],
	['A', 'di', 0, [(0,0), (0,1)]],
	['P', 'aa', 0, [(1,0), (2,0), (3,0)]],
	['B', 'aa', 0, [(4,0), (5,0)]],
	['Q', 'aa', 3, [(1,3), (2,3), (3,3)]],
	['R', 'di', 5, [(5,2), (5,3), (5,4)]],
	['C', 'di', 4, [(4,4), (4,5)]],
	['O', 'aa', 5, [(0,5), (1,5), (2,5)]]
)

meta = [(2,4),(2,5)]

class Autitos(SearchProblem):
	def actions(self, state):
		acciones = []
		posiciones_autos = []
		for auto in state:
			posiciones_autos.append(auto[3])

		for auto in state:
			movimiento = []
			fijo = auto[2]

			if auto[1] == 'di':
				posiciones_autos.remove(auto[3])
				# Derecha
				for parte in auto[3]:
					if parte[1] + 1 < 6 and parte[1] + 1 not in posiciones_autos:
						movimiento.append((fijo, parte[1] + 1))
				acciones.append((auto[0], movimiento))

				# Izquierda
				for parte in auto[3]:
					if parte[1] - 1 >= 0 and parte[1] - 1 not in posiciones_autos:
						movimiento.append((fijo, parte[1] - 1))
				acciones.append((auto[0], movimiento))
				posiciones_autos.append(auto[3])

			else:
				posiciones_autos.remove(auto[3])
				# Arriba
				for parte in auto[3]:
					if parte[1] - 1 >= 0 and parte[1] - 1 not in posiciones_autos:
						movimiento.append((parte[1] - 1, fijo))
				acciones.append((auto[0], movimiento))

				# Abajo
				for parte in auto[3]:
					if parte[1] + 1 < 6 and parte[1] + 1 not in posiciones_autos:
						movimiento.append((parte[1] + 1, fijo))
				acciones.append((auto[0], movimiento))
				posiciones_autos.append(auto[3])

		return acciones

	def result(self, state, action):
		auto, movimiento = action
		state = list(state)
		state[auto][3] = movimiento
		state = tuple(state)
		return state

	def cost(self, state1, action, state2):
		return len(action[1])

	def is_goal(self, state):
		auto_rojo = state[0]
		return auto_rojo[3] == meta

	def heuristic(self, state):
		auto_rojo = state[0]
		posicion = auto_rojo[3]
		return 5 - posicion[1][1]

if __name__ == '__main__':
	problema = Autitos(inicial)
	resultado = astar(problema, True)
	print resultado.state