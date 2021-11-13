def is_valid(name):
    if not 3 <= len(name) <= 16:
        return False
    for ch in name:
        if not (ch.isalnum() or ch in ('-', '_')):
            return False
    return True

names = input().split(', ')
[print(x) for x in names if is_valid(x)]
