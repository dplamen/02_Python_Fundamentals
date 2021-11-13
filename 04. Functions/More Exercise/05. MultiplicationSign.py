def sign_check(*numbers):
    count_positive = 0
    for i in numbers:
        if i == 0:
            return 'zero'
        count_positive += (1 if i > 0 else 0)
    if count_positive % 2 == 0:
        return 'negative'
    return 'positive'


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(sign_check(num1, num2, num3))
