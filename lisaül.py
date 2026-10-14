arvude_arv = 0
summa = 0
positiivsed = 0
negatiivsed = 0
paarisarvud = 0
paaritud = 0

arv = int(input("Sisesta arv: "))

while arv != 0:
    arvude_arv += 1
    summa += arv

    if arv > 0:
        positiivsed += 1
    elif arv < 0:
        negatiivsed += 1
    else:
        pass

    if arv % 2 == 0:
        paarisarvud += 1
    else:
        paaritud += 1

    arv = int(input("Sisesta arv: "))

print("\n--- TULEMUSED ---")

if arvude_arv == 0:
    print("Ühtegi arvu ei sisestatud.")
else:
    keskmine = summa / arvude_arv

    print(f"\nSisestatud arve: {arvude_arv}")
    print(f"Summa: {summa}")
    print(f"Keskmine: {keskmine:.2f}")

    print(f"\nPositiivseid arve: {positiivsed}")
    print(f"Negatiivseid arve: {negatiivsed}")
    print(f"Paarisarve: {paarisarvud}")
    print(f"Paarituid arve: {paaritud}")