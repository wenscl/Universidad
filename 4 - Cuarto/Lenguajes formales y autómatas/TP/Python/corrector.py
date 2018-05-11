import sys
import importlib
import json

pruebas = json.load(open('pruebas.json', 'rt'))
g = importlib.import_module(sys.argv[1])

for i, prueba in enumerate(pruebas[:]):
    print("="*80)
    print("Prueba %d" % i)
    reglas_esperadas = prueba['reglas_esperadas']
    es_ll1_esperado = prueba['es_ll1_esperado']
    cadenas_a_evaluar = prueba['cadenas_a_evaluar']

    gramatica = str('\n'.join([x for x, e in reglas_esperadas]))
    reglas, es_ll1 = g.setear_gramatica(gramatica)

    if es_ll1_esperado == es_ll1:
        print("es_ll1 Correcto")
    else:
        print("es_ll1 incorrecto")

    if (es_ll1_esperado and (es_ll1_esperado == es_ll1)):
        reglas_a_validar = {str(k): set(map(str, v)) for k, v in reglas_esperadas}

        reglas_correctas = True
        for regla, select in reglas:
            if regla not in reglas_a_validar:
                print("Regla no esperada: {}, Selects: {}".format(regla, select))
                reglas_correctas = False
            else:
                if select != reglas_a_validar[regla]:
                    print("El conjunto select de la linea '{}' es incorrecto".format(regla))
                    print("Se esperaba: {} se recibio {}".format(reglas_a_validar[regla], select))
                    reglas_correctas = False
                del reglas_a_validar[regla]

        if len(reglas_a_validar) > 0:
            reglas_correctas = False
            print("Las siguientes reglas no se recibieron:")
            for regla, select in reglas_a_validar.items():
                print("Regla: {:<20} Select: {}".format(regla, select))

        if reglas_correctas:
            print("Todas las reglas y los conjuntos select se calcularon correctamente")

        for cadena, res_esperado in cadenas_a_evaluar:
            res = g.evaluar_cadena(cadena)
            if res == res_esperado:
                print("Cadena: '{}' evaluada correctamente".format(cadena))
            else:
                print("Cadena: '{}' evaluada incorrectamente".format(cadena))
    else:
        print("Nada mas para validar en esta prueba")
    print("="*80)
