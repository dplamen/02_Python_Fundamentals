n = int(input())
cells = []
cell = 1
while n > 0:
    if n > 2 * cell**2:
        cells.append(2 * cell**2)
        n -= 2 * cell**2
        cell += 1
    else:
        cells.append(n)
        break
print(cells)