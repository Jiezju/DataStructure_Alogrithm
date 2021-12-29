'''
找到消失的元素
给定长度为n的数组，元素为1-n之间的数字，出现一次或者多次，找到没有出现在数组中的元素
'''


def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    res = []
    for i, num in enumerate(nums):
        if num > 0:
            res.append(i+1)

    return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(nums))
