arv = 0
kokku = 0

while True:
    hind = float(input("Sisesta hind: "))

    if hind == 0:
        break

    arv += 1
    kokku += hind

print("Tooteid:", arv)
print("Kokku: {kokku:.2f} €")