import re
names = []
spend_money = 0
pattern = r'>>(?P<item>\w+)<<(?P<price>\d+[\.]?\d+)!(?P<quantity>\d+)'
string = input()
while string != 'Purchase':
    matches = re.finditer(pattern, string)
    for match in matches:
        names.append(match.group('item'))
        spend_money += float(match.group('price')) * int(match.group('quantity'))
    string = input()


print("Bought furniture:")
if names:
    print('\n'.join(names))
print(f'Total money spend: {spend_money:.2f}')
