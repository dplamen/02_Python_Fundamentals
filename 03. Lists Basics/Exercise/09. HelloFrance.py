items = input().split('|')
budget = float(input())
new_prices = []
profit = 0
for i in range(len(items)):
    type, price = items[i].split('->')
    price = float(price)
    if budget < price:
        continue
    if type == 'Clothes' and price <= 50.00:
        new_prices.append(1.40 * price)
        budget -= price
    elif type == 'Shoes' and price <= 35.00:
        new_prices.append(1.40 * price)
        budget -= price
    elif type == 'Accessories' and price <= 20.50:
        new_prices.append(1.40 * price)
        budget -= price

result = ' '.join([f'{x:.2f}' for x in new_prices])
print(result)
print(f'Profit: {sum(new_prices)*2/7:.2f}')
if budget + sum(new_prices) >= 150.00:
    print("Hello, France!")
else:
    print("Not enough money.")
