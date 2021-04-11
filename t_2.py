import time

t = time.time()

dct = {}
for x in range(1000000):
    dct[x] = x**2

with open(f'{str(time.strftime("%H-%M-%S %d-%m-%Y"))}.txt', 'w', encoding='utf-8') as f:
    f.write(str(time.time() - t))
