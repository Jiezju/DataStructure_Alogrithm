'''
寻找枢纽序号

• 给定一个整数数组，试写一个函数返回此数组的枢纽序号。

• 枢纽序号的定义为：此元素左边所有元素之和与此元素右边所有元素之和相等的元素序号。

• 若不存在满足此条件的元素，返回 -1。如果有多个元素满足此条件，返回数列最左的枢纽元素的序号。
'''


def FindHub(nums):
    leftsum = 0
    rightsum = sum(nums[1:])

    n = len(nums)

    for i in range(1, n):
        leftsum += nums[i - 1]
        rightsum -= nums[i]
        if leftsum == rightsum:
            return i

    return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 3, 2, 1]
    print(FindHub(nums))
