'''
 给一个填好的数独，验证是否正确。
'''


def sudoku(matrix):
    n = len(matrix)

    for i in range(n):
        result_row = result_col = result_block = 0
        for j in range(n):
            # check row
            tmp_row = matrix[i][j]

            if result_row & (1 << (tmp_row - 1)) == 0:
                result_row = result_row | (1 << (tmp_row - 1))
            else:
                return False

            # check col
            tmp_col = matrix[j][i]

            if result_col & (1 << (tmp_col - 1)) == 0:
                result_col = result_col | (1 << (tmp_col - 1))
            else:
                return False

            # check block
            idx_row = i // 3 * 3 + j // 3
            idx_col = i % 3 * 3 + j % 3

            tmp_block = matrix[idx_row][idx_col]

            if result_block & (1 << (tmp_block - 1)) == 0:
                result_block = result_block | (1 << (tmp_block - 1))
            else:
                return False

    return True


if __name__ == '__main__':
    matrix = [[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    print(sudoku(matrix))
