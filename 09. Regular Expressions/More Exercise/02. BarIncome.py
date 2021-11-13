import re

pattern = r'%([A-Z][a-z]+)%[^%<>|.]*<(\w+)>[^%<>|.]*\|(\d+)\|[^%<>|.\d]*(\d+(\.\d+)?)\$'
line = input()
income = 0
while line != 'end of shift':
    m = re.search(pattern, line)
    if m:
        name = m.group(1)
        product = m.group(2)
        count = int(m.group(3))
        price = float(m.group(4))
        income += count * price
        print(f'{name}: {product} - {count * price :.2f}')
    line = input()

print(f'Total income: {income:.2f}')
