stock = input().split(', ')
line = input()
while line != 'Craft!':
    if line.split(' - ')[0] == 'Collect':
        item = line.split(' - ')[1]
        if item not in stock:
            stock.append(item)
    elif line.split(' - ')[0] == 'Drop':
        item = line.split(' - ')[1]
        if item in stock:
            stock.remove(item)
    elif line.split(' - ')[0] == 'Combine Items':
        old_item, new_item = line.split(' - ')[1].split(':')
        if old_item in stock:
            stock.insert(stock.index(old_item) + 1, new_item)
    elif line.split(' - ')[0] == 'Renew':
        item = line.split(' - ')[1]
        if item in stock:
            stock.remove(item)
            stock.append(item)
    line = input()

print(f"{', '.join(stock)}")
