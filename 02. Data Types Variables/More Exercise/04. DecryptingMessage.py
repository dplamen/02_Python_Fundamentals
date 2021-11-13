key = int(input())
n = int(input())
message = ''
for i in range(n):
    message += chr(ord(input()) + key)
print(message)
