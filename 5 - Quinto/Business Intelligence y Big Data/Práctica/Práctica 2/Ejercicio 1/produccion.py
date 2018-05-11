import random

for x in range(10000):
    productId = random.randint(1, 25)

    idLote = random.randint(1, 3000)

    idPlanta = random.randint(1, 5438)
    
    idAlmacen = random.randint(1, 5438)

    kilogramos = random.uniform(5, 60)

    kilogramos_leche = kilogramos - random.uniform(1, 3)

    tupla = (productId, idLote, idPlanta, idAlmacen, format(kilogramos, '.2f'), format(kilogramos_leche, '.2f'))

    print('{},'.format(tupla))    