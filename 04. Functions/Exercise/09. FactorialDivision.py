def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


a = factorial(int(input()))
b = factorial(int(input()))
print(f'{a/b:.2f}')
