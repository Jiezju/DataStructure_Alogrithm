'''
给一个m×n的矩阵，如果有一个元素为0，则把该元素对应的行与列所有元素全部变成0。
'''
def _print(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


def zero(matrix):
    # 统计存在0的行和列
    m = len(matrix)
    n = len(matrix[0])

    # 统计出现的数组
    rows = [0] * m
    cols = [0] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                # 标记
                rows[i] = 1
                cols[j] = 1

    for i in range(m):
        for j in range(n):
            if rows[i] == 1 or cols[j] == 1:
                matrix[i][j] = 0

    return matrix

if __name__ == '__main__':
    matrix = [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    matrix = zero(matrix)
    _print(matrix)
