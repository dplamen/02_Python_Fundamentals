neighborhood = [int(x) for x in input().split('@')]
line = input()
idx = 0
while line != "Love!":
    length = int(line.split()[1])
    if idx + length >= len(neighborhood):
        idx = 0
    else:
        idx += length
    if neighborhood[idx] == 0:
        print(f"Place {idx} already had Valentine's day.")
    elif neighborhood[idx] - 2 == 0:
        neighborhood[idx] = 0
        print(f"Place {idx} has Valentine's day.")
    else:
        neighborhood[idx] -= 2
    line = input()

print(f"Cupid's last position was {idx}.")
if sum(neighborhood) == 0:
    print('Mission was successful.')
else:
    print(f"Cupid has failed {len([x for x in neighborhood if x != 0])} places.")
