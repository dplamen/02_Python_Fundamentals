size = int(input())
days = int(input())
coins = 0
for d in range(1, days + 1):
    if d % 10 == 0:
        size -= 2
    if d % 15 == 0:
        size += 5

    coins += 50 - 2 * size

    if d % 3 == 0:
        coins -= 3 * size
    if d % 5 == 0:
        coins += 20 * size
    if d % 15 == 0:
        coins -= 2 * size

print(f"{size} companions received {int(coins/size)} coins each.")
