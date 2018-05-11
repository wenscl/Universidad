from datetime import datetime, timedelta
import random
 
year = 2017
for x in range(3000):
    month = random.randint(1, 8)
    day = random.randint(1, 28)

    date = datetime(year, month, day)
    date2 = datetime(year, month, day) + timedelta(days=270)

    tupla = (x + 1, date.strftime('%Y-%m-%d'), date2.strftime('%Y-%m-%d'))
    print('{},'.format(tupla))