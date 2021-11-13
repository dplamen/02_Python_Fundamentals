n = int(input())
for i1 in range(n):
    for i2 in range(n):
        for i3 in range(n):
            print(chr(97 + i1) + chr(97 + i2) + chr(97 + i3))
