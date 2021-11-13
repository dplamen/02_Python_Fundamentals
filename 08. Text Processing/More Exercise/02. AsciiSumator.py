first = input()
second = input()
random = input()
total = 0
if ord(first) > ord(second):
    first, second = second,  first
for ch in random:
    if ord(first) < ord(ch) < ord(second):
        total += ord(ch)
print(total)