words = input().split()
searched = input()
found = []
for word in words:
    if word == word[::-1]:
        found.append(word)
print(found)
print(f'Found palindrome {found.count(searched)} times')
