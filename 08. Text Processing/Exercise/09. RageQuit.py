text = input()
new_text = ''
unique = []
i = 0
letters = ''
while i < len(text):
    number = ''
    if text[i].isdigit():
        number += text[i]
        if i + 1 < len(text):
            if text[i+1].isdigit():
                number += text[i+1]
                i += 1
        number = int(number)
        new_text += number * letters
        letters = ''
    else:
        if text[i].upper() not in unique:
            unique.append(text[i].upper())
        letters += text[i].upper()
    i += 1

print(f'Unique symbols used: {len(unique)}')
print(new_text)