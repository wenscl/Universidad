def pot_menores(numero, maximo):
    i = 0
    lista = []
    while numero**i < maximo:
        lista.append(str(numero**i).zfill(4))
        i += 1
    return lista
	
def triangulo(texto):
    cant = len(texto)
    i = 1
    lista = []
    while i < cant:
        lista.append(texto[:i])
        i+=1
    while i>0:
        lista.append(texto[:i])
        i -=1
    return lista
	
def suma_nat(maximo, multiplos):
    i = 1
    s = 0
    b = 0
    while i < maximo:
        for e in multiplos:
            if i%e == 0 and b == 0:
                s = s + i
                b = 1
        i += 1
        b = 0
    return s
	
def suerte(numero, minimo, maximo):
    if numero == minimo:
        return 'Suerte'
    elif numero > maximo:
        return 'Grande'
    else:
        return 'Sin suerte'
