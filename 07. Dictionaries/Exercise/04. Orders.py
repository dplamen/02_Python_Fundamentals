line = input()
orders = {}
while line != 'buy':
    product, price, quantity = line.split()
    if product not in orders:
        orders[product] = {'price': 0.00, 'quantity': 0}
    orders[product]['price'] = float(price)
    orders[product]['quantity'] += int(quantity)
    line = input()

for k, v in orders.items():
    print(f"{k} -> {v['price']*v['quantity']:.2f}")
