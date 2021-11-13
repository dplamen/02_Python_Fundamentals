line = input()
while line != 'end':
    reversed_word = line[::-1]
    print(f'{line} = {reversed_word}')
    line = input()
