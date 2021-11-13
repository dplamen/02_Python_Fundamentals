line = input()
bakery = {}
while line != 'statistics':
    product, quantity = line.split(': ')
    if product not in bakery:
        bakery[product] = 0
    bakery[product] += int(quantity)
    line = input()

print("Products in stock:")
for p, q in bakery.items():
    print(f'- {p}: {q}')

print(f'Total Products: {len(bakery)}')
print(f'Total Quantity: {sum(bakery.values())}')
