number = float(input())
if number == 0:
    print('zero')
elif number < 0:
    if number < - 1000000:
        print('large negative')
    elif number < -1:
        print('negative')
    else:
        print('small negative')
else:
    if number > 1000000:
        print('large positive')
    elif number > 1:
        print('positive')
    else:
        print('small positive')

