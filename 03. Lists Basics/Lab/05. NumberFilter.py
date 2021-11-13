filters = {'even': [], 'odd': [], 'negative': [], 'positive': []}
n = int(input())

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        filters['even'].append(number)
    else:
        filters['odd'].append(number)
    if number < 0:
        filters['negative'].append(number)
    else:
        filters['positive'].append(number)

print(filters[input()])
