'''
普通迷宫
'''

def solution(matrix, start, end):
    if matrix[start[0]][start[1]] == 1 or matrix[end[0]][end[1]] == 1:
        return -1
    
    m = len(matrix)
    n = len(matrix[0])

    visited = [[0]*m for _ in range(n)]
    return dfs(matrix, start, visited, end, m, n)

def get_neighbors(node, m, n):
    x = node[0]
    y = node[1]

    candidate = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]

    for ele in candidate:
        if 0 <= ele[0] < m and 0 <= ele[1] < n:
            res.append(ele)
    return res

def dfs(matrix, node, visited, end, m, n):
    if node == end:
        return True
    else:
        visited[node[0]][node[1]] = 1

        for nbr in get_neighbors(node, m, n):
            if matrix[nbr[0]][nbr[1]] == 0 and visited[nbr[0]][nbr[1]]==0:
                if dfs(matrix, nbr, visited, end, m, n):
                    return True

        return False

'''
递归方法 二
'''

def dfs(matrix, start, dest):
    visited = [[False] * len(matrix[0]) for i in range(len(matrix))]
    return dfsHelper(matrix, start, dest, visited)
    
def dfsHelper(matrix, start, dest, visited):
    if matrix[start[0]][start[1]] == 1:
        return False
    
    if visited[start[0]][start[1]]:
        return False
    if start[0] == dest[0] and start[1] == dest[1]:
        return True
    
    visited[start[0]][start[1]] = True
    
    if (start[1] < len(matrix[0]) - 1):
        r = (start[0], start[1] + 1)
        if (dfsHelper(matrix, r, dest, visited)):
            return True
        
    if (start[1] > 0):
        l = (start[0], start[1] - 1)
        if (dfsHelper(matrix, l, dest, visited)):
            return True
        
    if (start[0] > 0):
        u = (start[0] - 1, start[1])
        if (dfsHelper(matrix, u, dest, visited)):
            return True
        
    if (start[0] < len(matrix[0]) - 1):
        d = (start[0] + 1, start[1])
        if (dfsHelper(matrix, d, dest, visited)):
            return True
            
    return False


'''
迭代方法
'''

def dfsIterative(matrix, start, dest):
    visited = [[False] * len(matrix[0]) for i in range(len(matrix))]
    stack = []
    stack.append(start)
    visited[start[0]][start[1]] = True
    
    idxs = [[0,1], [0,-1], [-1,0], [1,0]]
    
    while len(stack) != 0:
        curr = stack.pop() # vertex
        if (curr[0] == dest[0] and curr[1] == dest[1]):
            return True

        for idx in idxs:
            x = curr[0] + idx[0]
            y = curr[1] + idx[1]
            
            if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
                continue
            
            if (matrix[x][y] == 1):
                continue
                
            if (visited[x][y] == True):
                continue
            visited[x][y] = True
            stack.append((x, y))
            
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
    dest  = (4, 4)
    dfs(matrix, start, dest)