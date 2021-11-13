energy = 100
coins = 100
events = input().split('|')
f = True
for event in events:
    type, number = event.split('-')
    if type == 'rest':
        if energy + int(number) > 100:
            gain = 100 - energy
            energy = 100
        else:
            gain = int(number)
            energy += int(number)
        print(f"You gained {gain} energy.")
        print(f"Current energy: {energy}.")
    elif type == 'order':
        if energy - 30 >= 0:
            coins += int(number)
            energy -= 30
            print(f"You earned {int(number)} coins.")
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins - int(number) <= 0:
            print(f"Closed! Cannot afford {type}.")
            f = False
            break
        coins -= int(number)
        print(f"You bought {type}.")

if f:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')

