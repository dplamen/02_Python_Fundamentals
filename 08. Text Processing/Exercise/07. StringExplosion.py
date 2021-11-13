text = input()
new_text = ''
i = 0
power = 0
while i < len(text):
    new_text += text[i]
    if text[i] == '>':
        power += int(text[i + 1])
        for j in range(i + 1, i + 1 + power):
            if j < len(text):
                if text[j] == '>':
                    break
            i += 1
            power -= 1
    i += 1
print(new_text)





