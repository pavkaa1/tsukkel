parool = "qwerty"

for katse in range(3):
    sisestus = input("Sisesta parool: ")

    if sisestus == parool:
        print("Ligipääs lubatud!")
        break
else:
    print("Ligipääs blokeeritud!")