import math


def distance_center(x1, y1, x2, y2):
    d1 = (x1 ** 2 + y1 ** 2) ** 0.5
    d2 = (x2 ** 2 + y2 ** 2) ** 0.5
    if d1 <= d2:
        return f'{(math.floor(x1), math.floor(y1))}{(math.floor(x2), math.floor(y2))}'
    return f'{(math.floor(x2), math.floor(y2))}{(math.floor(x1), math.floor(y1))}'


def length_line(x1, y1, x2, y2):
    return ((y2 - y1)**2 + (x2 - x1)**2)**0.5


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

line1 = length_line(x1, y1, x2, y2)
line2 = length_line(x3, y3, x4, y4)

if line1 >= line2:
    print(distance_center(x1, y1, x2, y2))
else:
    print(distance_center(x3, y3, x4, y4))
