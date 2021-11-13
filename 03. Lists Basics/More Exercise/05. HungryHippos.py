def in_range(m, r, c):
    if 0 <= r < len(m):
        if 0 <= c < len(m[0]):
            return True
    return False


n = int(input())
mat = []
for i in range(n):
    mat.append(input().split())

