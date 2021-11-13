text = input()
count = {}
for ch in text:
    if ch != ' ':
        if ch not in count:
            count[ch] = 0
        count[ch] += 1

for k, v in count.items():
    print(f'{k} -> {v}')
