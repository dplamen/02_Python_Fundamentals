text = input()
non_numbers = [x for x in text if not x.isdigit()]
numbers = [int(x) for x in text if x.isdigit()]
take = []
skip = []
for i in range(len(numbers)):
    if i % 2 == 0:
        take.append(numbers[i])
    else:
        skip.append(numbers[i])
result = ''
start_pos = 0
for i in range(int(len(numbers) / 2)):
    result += ''.join(non_numbers[start_pos:start_pos + take[i]:])
    start_pos += take[i] + skip[i]
print(result)