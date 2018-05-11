inicial = [[b],[a,c],[]]

meta = [[],[],[c,b,a]]

def cost(state1, action, state2):
	return 1
	
def is_goal(state):
	return state == meta
	
def actions(state):
	acciones = []
	
	for x in state:
		if len(x) > 0:
			ultima_pieza = x[-1]
			for y in state:
				if x != y:
					acciones.append((x, y, ultima_pieza))
					
	return acciones

def result(state, action):
	origen, destino, pieza = action
	state[destino].append(pieza)
	state[origen].remove(pieza)
	return state

	