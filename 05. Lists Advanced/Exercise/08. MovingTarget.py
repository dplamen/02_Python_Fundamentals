def in_range(lst, index):
    return 0 <= index < len(lst)


targets = [int(x) for x in input().split()]
line = input()
while line.split()[0] != 'End':
    command, value1, value2 = line.split()
    idx = int(value1)
    if command == 'Shoot':
        power = int(value2)
        if in_range(targets, idx):
            targets[idx] -= power
            if targets[idx] <= 0:
                targets.remove(targets[idx])
    elif command == 'Add':
        value = int(value2)
        if in_range(targets, idx):
            targets.insert(idx, value)
        else:
            print('Invalid placement!')
    elif command == 'Strike':
        radius = int(value2)
        if in_range(targets, idx - radius) and in_range(targets, idx + radius):
            targets = targets[:idx - radius] + targets[idx + radius + 1:]
        else:
            print('Strike missed!')
    line = input()

result = '|'.join([str(x) for x in targets])
print(result)
