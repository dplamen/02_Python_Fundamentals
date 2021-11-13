text = input()
for i in range(len(text)):
    if text[i] == ':' and text[i+1] != ' ':
        print(text[i: i+ 2])
