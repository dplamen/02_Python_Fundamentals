lst = [int(x) for x in input().split(', ')]
beggars = int(input())
result = []
for b in range(0, beggars):
    result.append(0)
    for i in range(b, len(lst), beggars):
        result[b] += lst[i]
print(result)
