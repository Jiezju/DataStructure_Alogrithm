'''
程序接收三个参数，M，N和p，然后生成一个M * N的矩阵，
然后每一个cell有p的概率是地雷。
生成矩阵后，再计算出每一个cell周围地雷的数量。
'''

import random

def _print(board, m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if board[i][j] == -1:
                print('*', end=' ')
            else:
                print(board[i][j], end=' ')

        print()

def minesweeper(m, n, p):
    # 构建棋盘；每个cell按概率p填雷；无雷区域统计数量
    board = [[None] * (m + 2) for _ in range(n + 2)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            r = random.random()
            if r <= p:
                board[i][j] = -1
            else:
                board[i][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if board[i][j] == 0:
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if board[ii][jj] == -1:
                            board[i][j] += 1
    
    return board


if __name__ == '__main__':
    board = minesweeper(5, 5, 0.2)
    _print(board, 5, 5)
