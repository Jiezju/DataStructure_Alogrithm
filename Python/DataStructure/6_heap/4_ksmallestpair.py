'''
找到加和值最小的k对数
'''
import heapq


def kSmallestPairs(nums1, nums2, k):
    heap = []

    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j], i, j))

    for i in range(k):
        push(i, 0)

    pairs = []

    while heap and len(pairs) < k:
        _, i, j = heapq.heappop(heap)
        pairs.append((nums1[i], nums2[j]))
        push(i, j + 1)
    return pairs


if __name__ == '__main__':
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    print(kSmallestPairs(nums1, nums2, 2))
