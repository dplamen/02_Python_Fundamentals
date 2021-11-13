import math
n = int(input())
prime = True
if n != 2 and n % 2 == 0:
    prime = False
for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
        prime = False
print(prime)
