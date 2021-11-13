def odd_even_sum(number):
    even_sum = 0
    odd_sum = 0
    while number:
        digit = number % 10
        if digit % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
        number = number // 10

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


n = int(input())
print(odd_even_sum(n))
