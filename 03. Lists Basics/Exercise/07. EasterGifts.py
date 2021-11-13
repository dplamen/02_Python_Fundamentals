gifts = input().split()
command = input()
while command != 'No Money':
    if command.startswith('OutOfStock'):
        order, gift = command.split()
        for k in range(len(gifts)):
            if gifts[k] == gift:
                gifts[k] = 'None'
    elif command.startswith('Required'):
        order, gift, index = command.split()
        index  = int(index)
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif command.startswith('JustInCase'):
        order, gift = command.split()
        gifts[-1] = gift

    command = input()

result = ' '.join([x for x in gifts if x != 'None'])
print(result)