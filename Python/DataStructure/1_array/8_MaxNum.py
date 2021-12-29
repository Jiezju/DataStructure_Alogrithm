'''
最大数
给定一个数组，数组里有一个数组有且只有一个最大数，
判断这个最大数是否是其他数的两倍或更大。
如果存在这个数，则返回其index，否则返回-1。
'''


def largest_twice(nums):
    # 找到最大和第二大数　是否满足条件
    large = second = 0
    index = 0
    for i, num in enumerate(nums):
        if num > large:
            second = large
            large = num
            index = i
        elif num > second:
            second = num
    if large > 2 * second:
        return index
    return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 8, 3, 2, 1]
    result = largest_twice(nums)
    print(result)
