keys = [int(x) for x in input().split()]
line = input()
while line != 'find':
    new_string = ''
    for i in range(len(line)):
        new_string += chr(ord(line[i]) - keys[i % len(keys)])
    treasure  = new_string.split('&')[1]
    coordinates = new_string.split('<')[1].split('>')[0]
    print(f'Found {treasure} at {coordinates}')
    line = input()
