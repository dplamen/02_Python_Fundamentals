students = {}
n = int(input())
for i in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

students = {k: v for (k, v) in students.items() if sum(v)/len(v) >= 4.50}
for student, grade in sorted(students.items(), key=lambda x: -sum(x[1])/len(x[1])):
    print(f'{student} -> {sum(grade)/len(grade):.2f}')
