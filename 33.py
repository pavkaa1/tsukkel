from random import randint

salajane = randint(1, 100)
arv = 0

while arv != salajane:
    arv = int(input("Arva arv 1–100: "))

    if arv < salajane:
        print("Salajane arv on suurem.")
    elif arv > salajane:
        print("Salajane arv on väiksem.")
    else:
        print("Õige!")