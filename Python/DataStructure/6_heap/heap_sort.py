'''
堆排序
'''

from heapq import heappush, heappop


def heapSort(nums):
    res = []
    data = []

    for ele in nums:
        heappush(data, ele)

    for _ in range(len(nums)):
        res.append(heappop(data))

    return res


if __name__ == '__main__':
    nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(heapSort(nums))
