def dfs(matrix, x, y, visited):
    # Check for out-of-bounds or if the cell is not a '1' or already visited
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] == '0' or visited[x][y]:
        return
    
    # Mark the current cell as visited
    visited[x][y] = True
    
    # Explore all four directions
    dfs(matrix, x+1, y, visited)  # down
    dfs(matrix, x-1, y, visited)  # up
    dfs(matrix, x, y+1, visited)  # right
    dfs(matrix, x, y-1, visited)  # left

def count_blocks(matrix):
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1' and not visited[i][j]:
                dfs(matrix, i, j, visited)
                count += 1  # Increase count for each connected component found
    return count

# Input
n = int(input())
matrix = []
for _ in range(n):
    row = input().split()
    matrix.append(row)

# Solve
print(count_blocks(matrix))

