year = int(input())
while True:
    year += 1
    year_trns = list(str(year))
    if len(year_trns) == len(set(year_trns)):
        print(year)
        break
