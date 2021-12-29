'''
Pacific Atlantic Water Flow
'''


def is_valid(x, y, matrix):
    m = len(matrix)
    n = len(matrix[0])
    return x >= 0 and x < m and y >= 0 and y < n


def dfs(matrix, node, visited):
    visited.add(node)

    for direct in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        new_x = node[0] + direct[0]
        new_y = node[1] + direct[1]

        if isValid(new_x, new_y, matrix):
            if matrix[new_x][new_y] >= matrix[node[0]][node[1]]:
                if (new_x, new_y) not in visited:
                    dfs(matrix, (new_x, new_y), visited)


def pacificAtlantic_dfs(matrix):
    pacific = set()
    atlantic = set()
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dfs(matrix, (i, j), pacific)
            if i == m - 1 or j == n - 1:
                dfs(matrix, (i, j), atlantic)

    return list(pacific & atlantic)

'''
另一种解法
'''

def pacificAtlantic(matrix):

    if not matrix: return []
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    m = len(matrix)
    n = len(matrix[0])
    p_visited = [[False for _ in range(n)] for _ in range(m)]

    a_visited = [[False for _ in range(n)] for _ in range(m)]
    result = []

    for i in range(m):
        # p_visited[i][0] = True
        # a_visited[i][n-1] = True
        dfs(matrix, i, 0, p_visited, m, n)
        dfs(matrix, i, n-1, a_visited, m, n)
    for j in range(n):
        # p_visited[0][j] = True
        # a_visited[m-1][j] = True
        dfs(matrix, 0, j, p_visited, m, n)
        dfs(matrix, m-1, j, a_visited, m, n)

    for i in range(m):
        for j in range(n):
            if p_visited[i][j] and a_visited[i][j]:
                result.append([i,j])
    return result


def dfs(matrix, i, j, visited, m, n):
    # when dfs called, meaning its caller already verified this point 
    visited[i][j] = True
    for dir in [(1,0),(-1,0),(0,1),(0,-1)]:
        x, y = i + dir[0], j + dir[1]
        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
            continue
        dfs(matrix, x, y, visited, m, n)

'''
非递归形式
'''       
from collections import deque
def pacificAtlantic(matrix):
    if not matrix: return []
    m, n = len(matrix), len(matrix[0])
    def bfs(reachable_ocean):
        q = deque(reachable_ocean)
        while q:
            (i, j) = q.popleft()
            for (di, dj) in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= di+i < m and 0 <= dj+j < n and (di+i, dj+j) not in reachable_ocean \
                    and matrix[di+i][dj+j] >= matrix[i][j]:
                    q.append( (di+i,dj+j) )
                    reachable_ocean.add( (di+i, dj+j) )
        return reachable_ocean         
    pacific  =set ( [ (i, 0) for i in range(m)]   + [(0, j) for j  in range(1, n)]) 
    atlantic =set ( [ (i, n-1) for i in range(m)] + [(m-1, j) for j in range(n-1)]) 
    return list( bfs(pacific) & bfs(atlantic) )
