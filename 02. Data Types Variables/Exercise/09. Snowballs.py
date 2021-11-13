from sys import maxsize
n = int(input())
max_value = - maxsize
output = ''
for i in range(n):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = (snow / time) ** quality
    if value > max_value:
        max_value = value
        output = f'{snow} : {time} = {value:.0f} ({quality})'
print(output)
