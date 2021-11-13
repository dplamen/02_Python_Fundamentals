initial_capacity = 255
n = int(input())
capacity = initial_capacity
for i in range(n):
    litters = int(input())
    if capacity < litters:
        print("Insufficient capacity!")
        continue
    capacity -= litters
print(initial_capacity - capacity)
