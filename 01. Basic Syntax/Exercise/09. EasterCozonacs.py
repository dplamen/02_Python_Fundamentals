budget = float(input())
price_flour = float(input())
price_eggs = 0.75 * price_flour
price_milk = 1.25 * price_flour

colored_eggs = 0
cozonacs = 0
cost = 0

while budget > cost:
    cost = price_flour + price_eggs + price_milk / 4
    if cost <= budget:
        cozonacs += 1
        colored_eggs += 3
        budget -= cost
        if cozonacs % 3 == 0:
            colored_eggs -= cozonacs - 2

print(f"You made {cozonacs} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
