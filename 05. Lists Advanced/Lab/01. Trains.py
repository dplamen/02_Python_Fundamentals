n = int(input())
lst = [0] * n
line = input()
while line != 'End':
    command = line.split()[0]
    if command == 'add':
        people = int(line.split()[1])
        lst[-1] += people
    elif command == 'insert':
        idx = int(line.split()[1])
        people = int(line.split()[2])
        lst[idx] += people
    elif command == 'leave':
        idx = int(line.split()[1])
        people = int(line.split()[2])
        lst[idx] -= people
    line = input()

print(lst)
