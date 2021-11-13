line = input()
resources = {}
while line != 'stop':
    quantity = int(input())
    if line not in resources:
        resources[line] = 0
    resources[line] += quantity
    line = input()

for k,v in resources.items():
    print(f'{k} -> {v}')
