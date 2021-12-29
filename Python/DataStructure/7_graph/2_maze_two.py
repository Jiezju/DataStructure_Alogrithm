'''
迷宫搜索，直到撞墙返回：更改获取邻近节点的方法
'''

def maze_sol(matrix, start, end):
    m = len(matrix)
    n = len(matrix[0])

    visited = [[0]*m for _ in range(n)]
    return dfs(matrix, start, end, visited, m, n)


# 最大的不同
def get_neibour(matrix, node, m, n):
    idxs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    res = []

    for idx in idxs:
        new_x = node[0]
        new_y = node[1]

        while 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] == 0:
            new_x += idx[0]
            new_y += idx[1]
        
        if [new_x - idx[0], new_y - idx[1]] != node:
            res.append([new_x - idx[0], new_y - idx[1]])

    return res


def dfs(matrix, node, end, visited, m, n):
    if node == end:
        return True
    else:
        visited[node[0]][node[1]] = 1

        for nbr in get_neighbours(matrix, node, m, n):
            if visited[nbr[0]][nbr[1]] != 1 and matrix[nbr[0]][nbr[1]] !=1:
                if dfs(matrix, nod, visited, m, n):
                    return True

        return False


'''
另一种方法
'''

def dfs2(matrix, start, dest):
    visited = [[False] * len(matrix[0]) for i in range(len(matrix))]
    return dfsHelper2(matrix, start, dest, visited)
    
def dfsHelper2(matrix, start, dest, visited):
    if matrix[start[0]][start[1]] == 1:
        return False
    
    if visited[start[0]][start[1]]:
        return False
    if start[0] == dest[0] and start[1] == dest[1]:
        return True
    
    visited[start[0]][start[1]] = True
    
    r = start[1] + 1
    l = start[1] - 1
    u = start[0] - 1
    d = start[0] + 1
    
    while (r < len(matrix[0]) and matrix[start[0]][r] == 0):  ##  right
        r += 1
    x = (start[0], r - 1)
    if (dfsHelper2(matrix, x, dest, visited)):
        return True

    while (l >= 0 and matrix[start[0]][l] == 0):  ##  left
        l -= 1
    x = (start[0], l + 1)
    if (dfsHelper2(matrix, x, dest, visited)):
        return True
    
    while (u >= 0 and matrix[u][start[1]] == 0): ##  up
        u -= 1
    x = (u + 1, start[1])
    if (dfsHelper2(matrix, x, dest, visited)):
        return True
        
    while (d < len(matrix) and matrix[d][start[1]] == 0): ##  down
        d += 1
    x = (d - 1, start[1])
    if (dfsHelper2(matrix, x, dest, visited)):
        return True
            
    return False

if __name__=="__main__":
    matrix = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    dest  = (3, 2)
    dfs2(matrix, start, dest)