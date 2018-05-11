--ejercicio4
filtro f l = [x | x <- l, f x]

--ejercicio 5
numero n l = [x | x <- l, x < n] ++ [n] ++ [x | x <- l, x >= n]
otraforma x lista = filtro (x>) lista ++ [x] ++ filtro (x<=) lista

--ejercicio6 || Es una lista que tiene listas
funDesc ll = [x | l1 <- ll, x <- l1]

--ejercicio8
