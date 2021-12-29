'''
Longest Increasing Path in a Matrix
'''

def is_valid(node, nbr, matrix):
    m = len(matrix)
    n = len(matrix[0])
    x = nbr[0]
    y = nbr[1]
    return x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] > matrix[
        node[0]][node[1]]

def _dfs(matrix, node, cache):
    if cache[node[0]][node[1]] != -1:
        return cache[node[0]][node[1]]

    res = 1

    for direct in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nbr = (node[0] + direct[0], node[1] + direct[1])
        if is_valid(node, nbr, matrix):
            length = 1 + _dfs(matrix, nbr, cache)
            res = max(res, length)

    cache[node[0]][node[1]] = res
    return res
        

def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])

    # 中间结果缓存
    cache = [[-1]*m for _ in range(n)]
    result = 0
    for i in range(m):
        for j in range(n):
            res = _dfs(matrix, (i,j), cache)
            result = max(res, result)
    
    return result


if __name__=="__main__":
    nums = [
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]
    longestIncreasingPath(nums)