listFunc = [\ x y -> x+y, \ x y -> x*y, \ x y -> x-y]

aplica x y [] = []
aplica x y (a:b) = [a x y] ++ aplica x y b
aplicaFunciones x y = aplica x y listFunc