fire = input().split('#')
water = int(input())
effort = 0
results = []
for i in range(len(fire)):
    type_fire, value_cell = fire[i].split(' = ')

    if water - int(value_cell) < 0:
        continue

    if type_fire == 'High' and not 81 <= int(value_cell) <= 125:
        continue
    elif type_fire == 'Medium' and not 51 <= int(value_cell) <= 80:
        continue
    elif type_fire == 'Low' and not 1 <= int(value_cell) <= 50:
        continue
    water -= int(value_cell)
    effort += 0.25 * int(value_cell)
    results.append(int(value_cell))

print('Cells:')
for result in results:
    print(f' - {result}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(results)}')