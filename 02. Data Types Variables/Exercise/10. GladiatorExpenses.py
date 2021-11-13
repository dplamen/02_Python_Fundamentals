lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

equipment = {'helmet': 0, 'sword': 0, 'shield': 0, 'armor': 0}
for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        equipment['helmet'] += helmet
    if i % 3 == 0:
        equipment['sword'] += sword
    if i % 6 == 0:
        equipment['shield'] += shield
    if i % 12 == 0:
        equipment['armor'] += armor

expenses = 0
for v in equipment.values():
    expenses += v
print(f"Gladiator expenses: {expenses:.2f} aureus")


