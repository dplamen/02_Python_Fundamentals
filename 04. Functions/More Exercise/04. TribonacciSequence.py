def tribonacci(num):
    if num == 1:
        return '1'
    if num == 2:
        return '1 1'
    if num == 3:
        return '1 1 2'
    result = [1, 1, 2]
    for i in range(num-3):
        result.append(sum(result[-3:]))
    return ' '.join([str(x) for x in result])


n = int(input())
print(tribonacci(n))
