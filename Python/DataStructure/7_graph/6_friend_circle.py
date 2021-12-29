'''
Friend Circles
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


def dfs(matrix, node, visited):
    visited[node[0]][node[1]] = 1

    for nbr in get_neighbours(matrix, node):
        if visited[nbr[0]][nbr[1]] == 1 or matrix[nbr[0]][nbr[1]] != 1:
            continue
        dfs(matrix, nbr, visited)


def findCircleNum(matrix):
    m = len(matrix)
    visited = [[0] * m for _ in range(m)]

    result = 0

    for i in range(m):
        for j in range(m):
            if visited[i][j] == 1:
                continue

            if matrix[i][j] != 1:
                continue
            result += 1
            dfs(matrix, (i,j), visited)

    return result

'''
另外一种写法
'''

def findCircleNum2(M):
    def dfs(node):
        visited.add(node)
        for friend in range(len(M)):
            if M[node][friend] and friend not in visited:
                dfs(friend)

    circle = 0
    visited = set()
    for node in range(len(M)):
        if node not in visited:
            dfs(node)
            circle += 1
    return circle


if __name__=="__main__":
    M = [
     [1,1,0],
     [1,1,0],
     [0,0,1]]
    findCircleNum2(M)