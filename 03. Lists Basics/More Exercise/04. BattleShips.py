n = int(input())
field = []
for i in range(n):
    field.append([int(x) for x in input().split()])
attacks = input().split()

count = 0
for attack in attacks:
    row = int(attack.split('-')[0])
    col = int(attack.split('-')[1])
    if field[row][col] > 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            count += 1
print(count)
