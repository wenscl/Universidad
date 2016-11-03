from simpleai.search import (CspProblem, backtrack, min_conflicts)

slots = list('ABCDEFGHIJKLMNOPQ')

# Slots que podrian tener un modulo "Motor"
slots_con_motor = list('EFMNOPQ')

modulos_disponibles = ['Motores', 'Lasers', 'Cabinas', 'Bahias', 'Sistemas de vida extraterrestre', 'Escudos', 'Baterias']

modulos_consumidores = ['Lasers', 'Cabinas', 'Escudos', 'Sistemas de vida extraterrestre']

conexiones = [
    ('A', 'C'),
    ('A', 'B'),
    ('B', 'D'),
    ('C', 'E'),
    ('C', 'D'),
    ('E', 'G'),
    ('F', 'D'),
    ('F', 'H'),
    ('G', 'I'),
    ('G', 'H'),
    ('H', 'I'),
    ('I', 'J'),
    ('J', 'K'),
    ('K', 'L'),
    ('L', 'M'),
    ('L', 'N'),
    ('L', 'P'),
    ('P', 'O'),
    ('P', 'Q'),
]

# Los motores solo pueden ubicarse en los slots traseros o en los 4 slots laterales (no quiere decir que si o si esos slots tengan que tener motores. Pueden tener otras cosas).
# Esta restriccion se resuelve quitando del dominio el modulo "Motor" a los slots que no pueden contenerlo.
dominios = {slot: list(modulos_disponibles) if slot in slots_con_motor else list(modulos_disponibles[1:]) for slot in slots}

# Por el calor que los lasers generan al disparar, no puede haber baterias conectadas a lasers, de lo contrario podrian explotar.
def no_baterias_lasers(slots, modulos):
    return not ('Baterias' in modulos and 'Lasers' in modulos)

# Los sistemas de vida extraterrestre permiten que una cabina conectada albergue vida no humana, y por tanto si o si tienen que ubicarse conectados a cabinas.
def cabinas_sistemas(slots, modulos):
    if modulos[0] == 'Sistemas de vida extraterrestre':
        return 'Cabinas' in modulos
    return True

# Las cabinas no pueden estar conectadas a los motores, ya que el ruido que generan los mismos impediria el correcto trabajo de los pilotos.
def no_cabinas_motores(slots, modulos):
    return not ('Cabinas' in modulos and 'Motores' in modulos)

# Los escudos generan un campo electromagnetico tan fuerte, que produce interferencias con los sistemas de vida extraterrestre, y por ende no pueden estar conectados entre si.
def no_escudos_sistemas(slots, modulos):
    return not ('Escudos' in modulos and 'Sistemas de vida extraterrestre' in modulos)

# Las bahias de carga tienen que tener al menos una cabina conectada, para permitir inspecciones de seguridad.
def bahias_cabinas(slots, modulos):
    if modulos[0] == 'Bahias':
        return 'Cabinas' in modulos
    return True

# Las baterias tienen que tener al menos dos sistemas que consuman baterias conectados, para no desperdiciar energia.
# Los sistemas que consumen baterias son: Lasers, Cabinas de tripulantes, Escudos y Sistemas de vida extraterrestre.
def baterias_sistemas(slots, modulos):
    if modulos[0] == 'Baterias':
        return len([modulo for modulo in modulos if modulo in modulos_consumidores]) > 1
    return True

# No es posible instalar dos modulos iguales conectados entre si, por motivos cientificos extremadamente complicados de explicar.
def no_modulos_iguales(slots, modulos):
    return modulos[0] != modulos[1]

restricciones = []

for conexion in conexiones:
    restricciones.append((conexion, no_baterias_lasers))
    restricciones.append((conexion, no_cabinas_motores))
    restricciones.append((conexion, no_escudos_sistemas))
    restricciones.append((conexion, no_modulos_iguales))

for slot in slots:
    slot_conexiones = tuple([slot] + [x[0] if x[0] != slot else x[1] for x in conexiones if slot in x])
    restricciones.append((slot_conexiones, bahias_cabinas))
    restricciones.append((slot_conexiones, baterias_sistemas))
    restricciones.append((slot_conexiones, cabinas_sistemas))

def resolver(metodo_busqueda, iteraciones):
    problema = CspProblem(slots, dominios, restricciones)
    if metodo_busqueda == 'backtrack':
        return backtrack(problema)
    else:
        return min_conflicts(problema, iterations_limit=iteraciones)

def imprimir_lindo(result):
    for slot in result:
        print 'Slot {}: {}'.format(slot, result[slot])

if __name__ == '__main__':
    problem = CspProblem(slots, dominios, restricciones)

    resultado = backtrack(problem)
    print 'Backtrack:\n'
    imprimir_lindo(resultado)
    # print resultado

    resultado = min_conflicts(problem, iterations_limit=1000)
    print '\nMin Conflicts:\n'
    imprimir_lindo(resultado)
    # print resultado