events = ['coding', 'dog', 'cat', 'movie']
line = input()
coffee = 0
while line != 'END':
    if line.lower() in events:
        if line.islower():
            coffee += 1
        else:
            coffee += 2
    if coffee > 5:
        break
    line = input()

if coffee <= 5:
    print(coffee)
else:
    print('You need extra sleep')
