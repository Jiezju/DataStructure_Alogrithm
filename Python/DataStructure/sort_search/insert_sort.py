'''
插入排序
'''


def insert_sort(nums):
    n = len(nums)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums


if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 99]
    print(insert_sort(l))
