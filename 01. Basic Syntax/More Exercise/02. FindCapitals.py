text = list(input())
capitals_position = []
for i in range(len(text)):
    if 65 <= ord(text[i]) <= 90:
        capitals_position.append(i)
print(capitals_position)
