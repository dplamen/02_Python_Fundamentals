animals = input().split(', ')
count = 0
for i in range(len(animals) - 1, -1, -1):
    if animals[i] == 'wolf':
        if count == 0:
            print('Please go away and stop eating my sheep')
        else:
            print(f"Oi! Sheep number {count}! You are about to be eaten by a wolf!")
    count += 1
