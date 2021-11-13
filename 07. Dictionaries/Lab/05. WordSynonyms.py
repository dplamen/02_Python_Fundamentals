n = int(input())
dct = {}
for i in range(n):
    word = input()
    synonym = input()
    if word not in dct:
        dct[word] = []
    dct[word].append(synonym)

for k, v in dct.items():
    print(f'{k} - {", ".join(v)}')
