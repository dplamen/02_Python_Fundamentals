def output(dictionary, separator):
    for key, value in dictionary.items():
        print(f"{key} {separator} {value}")


line = input()
submissions = {}
while line != "exam finished":
    if line.split('-')[1] == 'banned':
        username = line.split('-')[0]
        if username in submissions:
            submissions['x' + username] = submissions[username]
            del submissions[username]
    else:
        username, language, points = line.split('-')
        if username not in submissions:
            submissions[username] = {}
        if language not in submissions[username]:
            submissions[username][language] = []
        submissions[username][language].append(int(points))
    line = input()

print('Results:')
results = {}
for k, v in submissions.items():
    average = 0
    for k1, v1 in v.items():
        average += max(v1)
    if not k.startswith('x'):
        results[k] = int(average / len(v))
results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
output(results, '|')
print('Submissions:')
results2 = {}
for k, v in submissions.items():
    for k1, v1 in v.items():
        if k1 not in results2:
            results2[k1] = 0
        results2[k1] += len(v1)
results2 = dict(sorted(results2.items(), key=lambda x: (-x[1], x[0])))
output(results2, '-')
