text = input()
new_text = text[0]
for ch in text:
    if ch != new_text[-1]:
        new_text += ch
print(new_text)