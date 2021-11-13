numbers = [int(x) for x in input().split()]
n = int(input())
for i in range(n):
    numbers.remove(min(numbers))
print(f"{', '.join([str(x) for x in numbers])}")
