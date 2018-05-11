import random
from datetime import datetime

for x in range(4000):
    productId = random.randint(1, 25)
    
    idLote = random.randint(1, 3000)
    
    idPais = random.randint(2, 20)    
    
    month = random.randint(1, 8)
    day = random.randint(1, 28)
    date = datetime(2017, month, day)

    kilogramos = random.uniform(5, 60)

    tupla = (productId, idLote, idPais, date.strftime('%Y-%m-%d'), format(kilogramos, '.2f'))

    print('{},'.format(tupla))