'''
第一种：传入图的格式G
'''


def dfs(node, visited):
    visited.add(node)

    for node in node.adjcents():
        if node not in visited:
            dfs(node, visited)


def nums_connected(G):
    visited = set()
    num = 0

    for node in G:
        if node not in visited:
            dfs(node, visited)
            num += 1

    return nums


'''
入图的矩阵形式 4连通 为1
'''


def neibours(i, j):
    return [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]  # 四连通


def dfs(node, matrix, visited):
    visited.add(node)

    for nod in neibours(i, j):
        if matrix[nod[0]][nod[1]] == 1 and nod not in visited:
            dfs(nod, matrix, visited)


def nums_connected(matrix):
    m = len(matrix)
    n = len(matrix[0])
    visited = [[0] * (m + 2) for _ in range(n + 2)]

    num = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                dfs([i, j], matrix, visited)
                num += 1

    return num
