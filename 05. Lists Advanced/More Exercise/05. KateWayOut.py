def find_pos(mat, symbol):
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == symbol:
                return r, c


def in_range(mat, r, c):
    if 0 <= r < len(mat):
        if 0 <= c < len(mat[0]):
            return True
    return False


rows = int(input())
maze = []
for i in range(rows):
    maze.append(list(input()))

row, col = find_pos(maze, 'k')
count = 1
success = False
while True:
    maze[row][col] = 'X'
    if in_range(maze, row + 1, col):
        row += 1
        if maze[row][col] == ' ':
            count += 1
            continue
        else:
            row -= 1
    else:
        success = True
        break
    if in_range(maze, row - 1, col):
        row -= 1
        if maze[row][col] == ' ':
            count += 1
            continue
        else:
            row += 1
    else:
        success = True
        break
    if in_range(maze, row, col - 1):
        col -= 1
        if maze[row][col] == ' ':
            count += 1
            continue
        else:
            col += 1
    else:
        success = True
        break
    if in_range(maze, row, col + 1):
        col += 1
        if maze[row][col] == ' ':
            count += 1
            continue
        else:
            col -= 1
    else:
        success = True
        break

    print('Kate cannot get out')
    break

if success:
    print(f'Kate got out in {count} moves')
