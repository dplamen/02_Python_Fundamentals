import math

numbers = [int(x) for x in input().split(', ')]
max_category = math.ceil(max(numbers)/10)
categories = {}

for i in range(1, max_category + 1):
    categories[i*10] = []

for n in numbers:
    category = math.ceil(n/10) * 10
    categories[category].append(n)

for k, v in categories.items():
    print(f"Group of {k}'s: {v}")
    