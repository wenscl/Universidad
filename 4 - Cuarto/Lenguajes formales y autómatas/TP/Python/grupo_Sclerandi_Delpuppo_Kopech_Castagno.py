reglas = []
select = []
first = []
follow = []
select = []
cadena = []
esLL1 = True
bandera = None
recursion = False

def setear_gramatica(gramatica):
    global reglas
    global cadena
    global first
    global follow
    global select
    global esLL1
    global bandera
    global recursion
    
    #dividir gramatica en lineas
    lineas = gramatica.splitlines() 
    reglas = []
    c = 0

    #dividir las reglas en antes y despues del igual
    for linea in lineas:
        c += 1 #numero de regla
        simbolos = linea.split()
        antes = simbolos[0]
        despues = simbolos[2:]
        reglas.append((c,antes,despues))

    ################################ RECURSION A IZQUIERDA ################################
    for regla in reglas:
        if regla[1] == regla[2][0]:
            esLL1 = False
            recursion = True
        
    ################################ FACTOR COMUN ################################
    bandera = 0
    for regla in reglas:
        for regla1 in reglas:
            if regla[0] != regla1[0] and regla[1] == regla1[1]:
                if not regla1[2][0].isupper():
                    if regla1[2][0] == regla[2][0]:
                        bandera = 1
        if bandera == 1:
            bandera = 0
            esLL1 = False
            
    ################################ FIRST ################################

    first = []
    lista_aux = []
    cadena = []
    
    def concatenar_first(regla,fi):
        bandera = None
        for Fi in first:
            if regla[0] == Fi[0]: #busco la regla
                if fi[2][0] not in Fi[2]: #agrego first solo si no estaba
                    cadena.append(fi[2][0])
                bandera = 1
        if not bandera == 1: #para guardar el primer first y que ande lo de arriba
            cadena.append(fi[2][0])
        return cadena        
    
    def encontrar_sig(regla):
        global recursion
        for regla_sig in reglas:
            if recursion == False and regla[2][0] == regla_sig[1]:
                if not regla_sig[2][0].isupper(): #encontro un terminal? concateno
                    lista_aux.append(regla_sig)
                else:
                    encontrar_sig(regla_sig)
        return lista_aux
    
    def encontrar_first(regla):
        final = []
        if not regla[2][0].isupper(): #terminal de una
            first.append((regla[0],regla[1],[regla[2][0]]))
        else: #derivar hasta encontrar los first
            fi = encontrar_sig(regla)
            for cada_regla in fi:
                #acumulo los first para agregarlos a la lista todos juntos
                final = concatenar_first(regla,cada_regla)
            cadena = list(set(final))
            first.append((regla[0],regla[1],cadena)) #agrego los first a la lista

    for regla in reglas:
        encontrar_first(regla)
        cadena = []
        lista_aux = []
    
    ################################ FOLLOW ################################

    follow = []
    cadena_Follow = []
    def buscar_Fi(NT,regla):
        for Fi in first:
            if NT == Fi[1]:
                cadena_Follow.extend(Fi[2])
        if 'lambda' in cadena_Follow:
            cadena_Follow.remove('lambda')
            buscar_Fo(regla)
            

    def buscar_Fo(regla):
        band = 0
        for Fo in follow:
            if regla[1] == Fo[0]:
                cadena_Follow.extend(Fo[1])
                band = 1
        if band == 0:
            encontrar_Fo(regla)
        return cadena_Follow

    cadena_New = []

    def encontrar_Fo(regla):
        bandera = 0
        varFo = None
        
        #para el distinguido
        if regla[0] == 1:
            cadena_Follow.append('$')
            
        for regla1 in reglas:
            if regla[1] in regla1[2]: #buscar la regla en la que aparece el NT para los Follow
                for simbolo in regla1[2]:
                    if varFo == regla[1]:
                        if not simbolo[0].isupper():
                            cadena_Follow.append(simbolo)
                        else:
                            buscar_Fi(simbolo,regla1)
                        bandera = 1
                    varFo = simbolo
                if bandera == 0:
                    if varFo != regla1[1]: #buscar los Follow solo si es de otro NT
                        buscar_Fo(regla1)
                varFo = None

        for e in cadena_Follow:
            if e not in cadena_New:
                cadena_New.append(e)


    for regla in reglas:
        b = 0
        for Fo in follow:
            if regla[1] == Fo[0]:
                b = 1
        if b == 0:
            encontrar_Fo(regla)
            follow.append((regla[1],cadena_New))
            cadena_Follow = []
            cadena_New = []

    ################################ SELECT ################################
    select = []
    for Fi in first:
        cadena.extend(Fi[2])
        if 'lambda' in Fi[2]:
            cadena.remove('lambda')
            for Fo in follow:
                if Fi[1] == Fo[0]:
                    cadena.extend(Fo[1])
        select.append((Fi[0],Fi[1],cadena))
        cadena = []
    
    #ver si son diyuntos
    for Se in select:
        for Se1 in select:
            if Se1[0] != Se[0] and Se1[1] == Se[1]:
                for simbolo in Se[2]:
                    if simbolo in Se1[2]:
                        esLL1 = False
                    
    reglas_esperadas = []
    
    #formar reglas esperadas
    for regla in reglas:
        regla1 = str(regla[1]) + ' :'
        for elemento in regla[2]:
            regla1 += ' ' + str(elemento)
        for Se in select:
            if regla[0] == Se[0]:
                reglas_esperadas.append((regla1,set(Se[2])))
    return (reglas_esperadas, esLL1)

def evaluar_cadena(cadena):
    global reglas
    global select
    global follow
    NT = []
    tokens = cadena.split()
    tokens.append('$')
    pila = [reglas[0][1]]
    for Fo in follow:
        NT.append(Fo[0])
    reglas_NT = []

    elemento = tokens[0]
    tokens = tokens[1:]
    while len(pila) > 0:
        reglas_NT = []
        item = pila.pop()
        despues = ""
        if item in NT:
            for regla in reglas:
                if item == regla[1]:
                    reglas_NT.append(regla)
            for regla in reglas_NT:
                for Se in select:
                    if Se[0] == regla[0]:
                        if elemento in Se[2]:
                            despues = regla[2]
            if len(despues) == 0:
                return False
            if "lambda" not in despues:
                despues = despues[::-1]
                pila.extend(despues)
        elif elemento == item:
            elemento = tokens[0]
            tokens = tokens[1:]
        else:
            return False
    if len(tokens) == 0:
        return True
    else:
        return False