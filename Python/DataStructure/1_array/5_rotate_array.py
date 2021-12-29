'''
给一个n×n的数组，旋转90度。
'''


def show_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


def rotate1(matrix):
    # 交换对角线 然后每行逆序
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            if i != j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix


def rotate2(matrix):
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - 1 - first

        for i in range(first, last):
            offset = i - first

            # top left
            tmp = matrix[first][i]

            # bottom left
            matrix[first][i] = matrix[last - offset][first]

            # bottom right
            matrix[last - offset][first] = matrix[last][last - offset]

            # top right
            matrix[last][last - offset] = matrix[i][last]

            # top left
            matrix[i][last] = tmp

    return matrix


if __name__ == '__main__':
    matrix = [[i * 5 + j for j in range(5)] for i in range(5)]
    show_matrix(matrix)
    matrix = rotate2(matrix)
    show_matrix(matrix)
