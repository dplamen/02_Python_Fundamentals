line = input().split()

total = 0
for el in line:
    text = el.strip()
    first_letter = text[0]
    second_letter = text[-1]
    number = int(text[1:-1])
    if first_letter.isupper():
        number /= ord(first_letter) - 64
    else:
        number *= ord(first_letter) - 96
    if second_letter.isupper():
        number -= ord(second_letter) - 64
    else:
        number += ord(second_letter) - 96
    total += number

print(f'{total:.2f}')
