records = {}
line = input()
while line != 'End':
    company, employee_id = line.split(' -> ')
    if company not in records:
        records[company] = []
    if employee_id not in records[company]:
        records[company].append(employee_id)
    line = input()

records = dict(sorted(records.items(), key=lambda x: x[0]))
for k, v in records.items():
    print(k)
    for num in v:
        print(f'-- {num}')
