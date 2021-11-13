def index_max(lst):
    for idx in range(len(lst)):
        if lst[idx] == max(lst):
            return idx


population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())
for i in range(len(population)):
    difference = minimum_wealth - population[i]
    idx_max = index_max(population)
    if difference > 0:
        difference2 = population[idx_max] - difference
        if difference2 < 0:
            continue
        else:
            population[i] += difference
            population[idx_max] -= difference
    else:
        continue

if any([True for x in population if x < minimum_wealth]):
    print('No equal distribution possible')
else:
    print(population)

