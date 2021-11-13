seeked_words = ["sand", "water", "fish", "sun"]
text = input().lower()
count = 0
for word in seeked_words:
    count += text.count(word)
print(count)
