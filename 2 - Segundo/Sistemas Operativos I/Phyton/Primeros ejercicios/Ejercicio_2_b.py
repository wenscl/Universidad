s = raw_input('Ingrese un texto: ')
cont = len(s)
i = 0
while i < cont :
        print s[:i]
	i +=1
while i >= 0 :
	print s[:i]
	i -= 1
