cuadrado:: Integer -> Integer
cuadrado x = x*x


suma x y = x + y

-- Agrega 1 a la suma
suma1 = suma 1

menor:: (Integer,Integer) -> Integer
menor (x,y) = if x <= y then x else y


-- factorial
--OJO si pongo facR 0 = 1 abajo entonces para el caso facR 0 se va a tildar todo!!
facR 0 = 1
facR n = n * facR (n - 1)
facNR n = product[1..n]

-- incremento en 1
incr :: Int -> Int
incr n = n + 1

-- concatenar : funcion que devuelve una función que devuelve un string
concatena :: String -> String -> String 
concatena s1 s2 = s1 ++ s2

-- Si llamo a la función concatenaParcial con hola me devuelve "mundohola"
concatenaParcial :: String -> String
concatenaParcial = concatena "mundo"

-- tupla, no tengo aplicacion parcial. (s1,s2) es un unico parametro
concatenau :: (String, String) -> String
concatenau (s1, s2) = s1 ++ s2

-- funcion que toma un argumento y usa el argumento para generar una funcion parcialmente aplicada 
concatenap s1 = (s1 ++)

-- cuenta cuantas palabras hay en una oración separada por espacios
wordCount = length . words

-- PATTERN MATCHING
-- encuentro elementos dentro de una lista
primero (x,y) = x
segundo (x,y) = y
prim (x, _) = x
seg(_, y) = y
-- encuentro cabecera de una lista (primero)
cab (x:xs) = x
-- devuelve la lista sin cabecera
cola (x:xs) = xs


--    5 : [] agrego el 5 a una lista.
--    1:2:3:4:[] agrega primero el 4 y genera una lista, después agrega 3:[4] y así...

-- hacemos una funcion que sume sin el sum automatico
-- suma lista es una func recursiva asiq se tiene que llamar a si misma
suma_lista [] = 0
suma_lista (n:otra_lista) = n + suma_lista otra_lista


-- lista de funciones anónimas
listFunc = [\x y -> x + y,\x y -> x - y,\x y -> x * y,\x y -> x / y]

-- ejercicio 1
aplica x y [] = []
aplica x y (cab:cola) = cab x y : aplica x y cola
aplicar x y = aplica x y listFunc
