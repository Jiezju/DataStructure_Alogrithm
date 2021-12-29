''''
Max Area of Island
'''

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def is_vaid(matrix, x, y):
    m = len(matrix)
    n = len(matrix[0])

    return x >= 0 and y >= 0 and x < m and y < n


def get_neighbours(matrix, node):
    for direct in directions:
        new_x = node[0] + direct[0]
        new_y = node[1] + direct[1]
        if is_vaid(matrix, new_x, new_y):
            yield [new_x, new_y]

def dfs(grid, node, visited, area):
    visited[node[0]][node[1]] = 1
    area += 1

    for nbr in get_neighbours(grid, node):
        if not visited[nbr[0]][nbr[1]] and grid[nbr[0]][nbr[1]]:
            dfs(grid, nbr, visited, area)


def maxAreaOfIsland(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[0] * n for _ in range(m)]

    max_area = 0
    
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 1:
                continue
            if grid[i][j] == 0:
                continue

            local_area = 0
            dfs(grid, (i,j), visited, local_area)
            max_area = max(max_area, local_area)

    return max_area

'''
另一种方法
'''

def maxAreaOfIsland(grid):
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and grid[i][j]:
            grid[i][j] = 0
            return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
        return 0

    result = 0
    for x in range(m):
        for y in range(n):
            if grid[x][y]:
                result = max(result, dfs(x, y))
    return result

if __name__=="__main__":
    matrix = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]

    maxAreaOfIsland(matrix)
