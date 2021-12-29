'''
前K大元素
'''

from heapq import heappush, heappop


def nlargest(nums, k):
    data = []
    res = []

    for ele in nums:
        heappush(data, -ele)

    for _ in range(k):
        res.append(-heappop(data))

    return res


def nthlargest(nums, k):
    heap = []

    for ele in nums:
        heappush(heap, ele)
        if len(heap) > k:
            heappop(heap)

    return heap[0]


if __name__ == '__main__':
    li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
    print(nlargest(li1, 4))
    print(nthlargest(li1, 4))
