raha = 1000
aasta = 0

while raha < 2000:
    raha = raha * 1.05
    aasta += 1

print(f"Eesmärk täitub {aasta} aastaga.")
print(f"Kontol on {raha:.2f} eurot.")