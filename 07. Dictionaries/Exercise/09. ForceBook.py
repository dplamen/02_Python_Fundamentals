def check_values(dictionary, seek):
    for k, v in dictionary.items():
        for item in v:
            if item == seek:
                return k, v.index(item)
    return False


line = input()
force_book = {}
while line != "Lumpawaroo":
    if '|' in line:
        side, user = line.split(' | ')
        if not check_values(force_book, user):
            if side not in force_book:
                force_book[side] = []
            force_book[side].append(user)
    elif '->' in line:
        user, side = line.split(' -> ')
        if check_values(force_book, user):
            if side in force_book:
                force_book[check_values(force_book, user)[0]].remove(user)
                force_book[side].append(user)
        else:
            if side not in force_book:
                force_book[side] = []
            force_book[side].append(user)
        print(f"{user} joins the {side} side!")
    line = input()

force_book = dict(sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])))
for k, v in force_book.items():
    if len(v) > 0:
        print(f'Side: {k}, Members: {len(v)}')
        for item in sorted(v):
            print(f'! {item}')
