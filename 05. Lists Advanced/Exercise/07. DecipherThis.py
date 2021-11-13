text = input().split()

new_text = []
for word in text:
    char_index = 0
    for i in range(len(word)):
        if not word[i].isdigit():
            char_index = i
            break
    new_word = chr(int(word[:char_index]))
    new_word += word[-1]
    new_word += word[char_index + 1:-1]
    if char_index + 1 < len(word):
        new_word += word[char_index]
    new_text.append(new_word)

result = ' '.join(new_text)
print(result)
