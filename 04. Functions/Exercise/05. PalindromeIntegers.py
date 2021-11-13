def is_palindrome(text):
    original = list(text)
    reverse = []
    while original:
        reverse.append(original.pop())
    return list(text) == reverse


numbers = input().split(', ')
for n in numbers:
    print(is_palindrome(n))
