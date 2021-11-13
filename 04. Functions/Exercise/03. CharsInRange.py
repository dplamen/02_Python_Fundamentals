def chars_in_range(start, end):
    result = []
    for i in range(ord(start) + 1, ord(end)):
        result.append(chr(i))
    return f'{" ".join(result)}'


begin = input()
end = input()
print(chars_in_range(begin, end))
