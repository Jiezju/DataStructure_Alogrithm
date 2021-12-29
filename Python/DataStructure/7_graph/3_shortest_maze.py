'''
迷宫的最短路径
'''
import heapq

def init_distance(node, matrix, m, n):
    distance = {}
    for i in range(m):
        for j in range(n):
            if [i, j] == node:
                distance[str(node[0]) + '_' + str(node[1])] = 0
            else:
                distance[str(i) + '_' + str(j)] = 1000
    return distance

def get_neibour(node, matrix, m, n):
    idxs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    res = []
    new_x = node[0]
    new_y = node[1]
    for idx in idxs:

        while is_valid(new_x, new_y, m, n) and matrix[new_x][new_y] == 0:
            new_x += idx[0]
            new_y += idx[1]

        if [new_x - idx[0], new_y - idx[1] != node:
            res.append([new_x - idx[0], new_y - idx[1]])

    return res

def get_dis(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

def shortest_route(matrix, start, end):
    m = len(matrix)
    n = len(matrix[0])
    visited = [[0] * m for _ in range(n)]

    distance = init_distance(matrix)
    priority_queue = [(0,start)]

    while priority_queue:
        dis, node = heapq.heappop(priority_queue)
        visited[node[0]][node[1]] = 1

        if node == end:
            return dis

        for nbr in get_neighbors(node, matrix, m, n):
            if visited[nbr[0]][nbr[1]] == 0 and matrix[nbr[0]][nbr[1]] == 0:
                nbr_name = str(nbr[0]) + '_' + str(nbr[1])
                if dis + getdis(node, nbr) < distance[nbr_name]:
                    distance[nbr_name] = dis + getdis(node, nbr)
                    heapq.heappush(priority_queue, (distance[nbr_name], nbr))

'''
贪心算法
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
