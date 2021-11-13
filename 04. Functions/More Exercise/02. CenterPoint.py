import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

d1 = (x1**2 + y1**2)**0.5
d2 = (x2**2 + y2**2)**0.5
print((math.floor(x1), math.floor(y1)) if d1 <= d2 else (math.floor(x2), math.floor(y2)))
