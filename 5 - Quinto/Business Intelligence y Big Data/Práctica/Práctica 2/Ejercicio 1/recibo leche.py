import random
from datetime import datetime

for x in range(15000):
    # "IdPlanta", "IdTambo", "Fecha", "Kilogramos", "Grasa_Butirometrica", "Solidos_Totales"
    idPlanta = random.randint(1, 5438)

    idTambo = random.randint(1, 10000)

    month = random.randint(1, 8)
    day = random.randint(1, 28)
    date = datetime(2017, month, day)

    kilogramos = random.uniform(10, 50)

    porcentaje_grasa = random.randint(10, 13)
    grasa = kilogramos * porcentaje_grasa / 100

    solidos_totales = kilogramos * 15 / 100

    tupla = (idPlanta, idTambo, date.strftime('%Y-%m-%d'), format(kilogramos, '.2f'), format(grasa, '.2f'), format(solidos_totales, '.2f'))

    print('{},'.format(tupla))