text1, text2 = input().split()

total = 0
if len(text1) <= len(text2):
    for i in range(len(text1)):
        total += ord(text1[i]) * ord(text2[i])
    for j in range(i+1, len(text2)):
        total += ord(text2[j])
else:
    for i in range(len(text2)):
        total += ord(text1[i]) * ord(text2[i])
    for j in range(i+1, len(text1)):
        total += ord(text1[j])

print(total)
