happiness = [int(x) for x in input().split()]
improvement_factor = int(input())
happiness = [3*x for x in happiness]
average_happiness = sum(happiness) / len(happiness)
score = len(list(filter(lambda x: x >= average_happiness, happiness)))
if score >= len(happiness) / 2:
    print(f"Score: {score}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {score}/{len(happiness)}. Employees are not happy!")
