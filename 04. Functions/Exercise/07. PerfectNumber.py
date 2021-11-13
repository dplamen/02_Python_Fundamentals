def is_perfect(n: int) -> bool:
    divisors = []
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            divisors.append(i)
    return n > 0 and n == sum(divisors)


number = int(input())
if is_perfect(number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
