n = int(input())
for i in range(1, n + 1):
    number = i
    sum_digits = 0
    while number:
        sum_digits += number % 10
        number = int(number / 10)
    print(f'{i} -> {sum_digits in (5, 7, 11)}')
