def total_calc(product, quantity):
    menu = {'coffee': 1.50, 'coke': 1.40, 'water': 1.00, 'snacks': 2.00}
    return f'{menu[product] * quantity:.2f}'

p = input()
q = float(input())
print(total_calc(p, q))