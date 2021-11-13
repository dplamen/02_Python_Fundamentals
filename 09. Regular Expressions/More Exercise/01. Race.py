import re

line = input().split(', ')
racers = {}
for racer in line:
    if racer not in racers:
        racers[racer] = 0

text = input()
while text != 'end of race':
    name = ''.join(re.findall(r'[a-zA-Z]', text))
    distance = sum([int(x) for x in re.findall(r'[0-9]', text)])
    text = input()
    if name in racers:
        racers[name] += distance

racers = sorted(racers.items(), key=lambda x: -x[1])
print(f'1st place: {racers[0][0]}')
print(f'2nd place: {racers[1][0]}')
print(f'3rd place: {racers[2][0]}')
