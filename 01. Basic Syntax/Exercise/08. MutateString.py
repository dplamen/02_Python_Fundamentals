text1 = input()
text2 = input()
new = ''
for i in range(len(text1)):
    new = text2[:i+1] + text1[i+1:]
    if text1[i] != text2[i]:
        print(new) 