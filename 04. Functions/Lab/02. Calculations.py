def calculate(action, a, b):
    result = None
    map = {'multiply': '*', 'add': '+', 'divide': '/', 'subtract': '-'}
    result = eval(str(a) + map[action] + str(b))
    return int(result)

operator = input()
num1 = int(input())
num2 = int(input())

print(calculate(operator, num1, num2))

