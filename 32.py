from random import randint

salajane = randint(1, 10)
arv = 0

while arv != salajane:
    arv = int(input("Arva arv 1–10: "))

    if arv == salajane:
        print("Õige!")
    else:
        print("Vale!")