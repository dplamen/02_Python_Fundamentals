words = input().split()
result = []
words_count = {}
for word in words:
    if word.lower() not in words_count:
        words_count[word.lower()] = 0
    words_count[word.lower()] += 1

for w, c in words_count.items():
    if c % 2 != 0:
        result.append(w)
print(f'{" ".join(result)}')
