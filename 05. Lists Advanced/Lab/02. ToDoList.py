todo_notes = [''] * 10
line = input()
while line != 'End':
    importance, note = line.split('-')
    todo_notes[int(importance)-1] = note
    line = input()
print([x for x in todo_notes if x != ''])
