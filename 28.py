import random

vise = 1
summa = 0

while vise <= 10:
    tulemus = random.randint(1, 6)
    print(f"{vise}. vise: {tulemus}")
    summa += tulemus
    vise += 1

print("Visete summa:", summa)
print("Keskmine tulemus:", summa / 10)