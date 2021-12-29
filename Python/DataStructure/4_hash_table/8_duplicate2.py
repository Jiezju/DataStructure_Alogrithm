'''
给定的整型Array和整数k：试找出是否存在两个独特的索引i,j，使得num[i] = num[j]且i和j之间的距离小于k
'''


def containsNearbyDuplicate(nums, k):
    dic = {}

    for i, ele in enumerate(nums):
        if ele in dic and dic[ele] - i < k:
            return [dic[ele], i]
        dic[ele] = i

    return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 3]
    print(containsNearbyDuplicate(nums, 3))
