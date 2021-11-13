quantity = int(input())
days = int(input())
ornament = 2
skirt = 5
garlands = 3
lights = 15
total_cost = 0
spirit = 0
for d in range(1, days + 1):
    if d % 11 == 0:
        quantity += 2
    if d % 2 == 0:
        total_cost += ornament * quantity
        spirit += 5
    if d % 3 == 0:
        total_cost += (skirt + garlands) * quantity
        spirit += 13
    if d % 5 == 0:
        total_cost += lights * quantity
        spirit += 17
        if d % 3 == 0:
            spirit += 30
    if d % 10 == 0:
        spirit -= 20
        total_cost += skirt + garlands + lights
if d % 10 == 0:
    spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")
