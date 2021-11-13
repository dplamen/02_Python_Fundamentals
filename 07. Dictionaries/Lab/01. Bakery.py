text = input().split()
dictionary = {}
for i in range(0, len(text), 2):
    dictionary[text[i]] = int(text[i + 1])
print(dictionary)
