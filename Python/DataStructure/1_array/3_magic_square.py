'''
九宫图
'''


def show(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


def magic_square(n):
    # init matrix
    matrix = [[None] * n for _ in range(n)]

    row = n - 1
    col = n // 2
    matrix[row][col] = 1

    for i in range(2, n * n + 1):
        new_row = (row + 1) % n
        new_col = (col + 1) % n

        if matrix[new_row][new_col] != None:
            row = (row - 1 + n) % n
            col = col
        else:
            row = new_row
            col = new_col
        matrix[row][col] = i

    
    return matrix

    


if __name__ == '__main__':
    matrix = magic_square(5)
    show(matrix)