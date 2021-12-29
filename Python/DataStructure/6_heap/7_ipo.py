'''
管理你的项目（IPO）
'''

import heapq


def findMaximizedCapital(k, W, Profits, Capital):
    heap = []
    current_w = W

    for i in range(k):
        for index, ele in enumerate(Capital):
            if ele <= current_w:
                heapq.heappush(heap, (-Profits[index], ele))
        profit, ele = heapq.heappop(heap)
        current_w -= profit
    return current_w


if __name__ == '__main__':
    k = 2
    W = 0
    Profits = [1, 2, 3]
    Capital = [0, 1, 1]

    print(findMaximizedCapital(k, W, Profits, Capital))
