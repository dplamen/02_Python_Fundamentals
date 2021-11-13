version = [int(x) for x in input().split('.')]
version[2] += 1
if version[2] > 9:
    version[2] = 0
    version[1] += 1
    if version[1] > 9:
        version[1] = 0
        version[0] += 1
result = '.'.join([str(x) for x in version])
print(result )
