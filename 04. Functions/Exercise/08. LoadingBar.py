def loading_bar(number):
    result = str(number) + '% '
    if number == 100:
        result += 'Complete!\n'
    result += '['
    for i in range(1, 11):
        if i <= int(number / 10):
            result += '%'
        else:
            result += '.'
    result += ']' + '\n'
    if number < 100:
        result += 'Still loading...'
    return result


n = int(input())
print(loading_bar(n))
