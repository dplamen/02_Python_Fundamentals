numbers = [int(x) for x in input().split(', ')]
result = []
for idx, num in enumerate(numbers):
    if num % 2 == 0:
        result.append(idx)
print(result)
