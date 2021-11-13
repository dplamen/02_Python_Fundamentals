def smallest_of_three(a, b, c):
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    return min


x = int(input())
y = int(input())
z = int(input())
print(smallest_of_three(x, y, z))
