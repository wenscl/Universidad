import random
from datetime import datetime

for x in range(4000):
    idAlmacenOrigen = random.randint(1, 5438)
    idAlmacenDestino = random.randint(1, 5438)
    
    while idAlmacenDestino == idAlmacenOrigen:
        idAlmacenDestino = random.randint(1, 5438)
    
    month = random.randint(1, 8)
    day = random.randint(1, 28)
    date = datetime(2017, month, day)
    
    kilogramos = random.uniform(5, 60)

    productId = random.randint(1, 25)

    idLote = random.randint(1, 3000)

    tupla = (idAlmacenOrigen, idAlmacenDestino, date.strftime('%Y-%m-%d'), format(kilogramos, '.2f'), productId, idLote)

    print('{},'.format(tupla))    