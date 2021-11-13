courses = {}
line = input()
while line != 'end':
    course_name, student_name = line.split(' : ')
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    line = input()

for key, value in sorted(courses.items(), key=lambda x: -len(x[1])):
    print(f'{key}: {len(value)}')
    for item in sorted(value):
        print(f'-- {item}')
