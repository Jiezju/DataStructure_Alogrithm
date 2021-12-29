'''
01 Matrix

这是一个多起点的最短路径问题，往往都会使用 bfs
非矩阵往往要用到 dijstra
'''

def bfs(matrix):
    m = len(matrix)
    n = len(matrix[0])

    queue = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                queue.append((i,j))
            else:
                matrix[i][j] = 1000

    while queue:
        node = queue.pop(0)

        for direct in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x = node[0] + direct[0]
            y = node[1] + direct[1]

            z = 1 + matrix[node[0]][node[1]]

            if x >= 0 and x < m and y >= 0 and y < m and matrix[x][y] > z:
                matrix[x][y] = z
                queue.append((x,y))

    return matrix
