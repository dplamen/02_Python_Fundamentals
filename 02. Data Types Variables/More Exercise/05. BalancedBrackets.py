n = int(input())
balanced = True
for i in range(n):
    symbol = input()
    if symbol == '(':
        if balanced:
            balanced = False
        else:
            break
    elif symbol == ')':
        if not balanced:
            balanced = True
        else:
            balanced = False
            break
if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

