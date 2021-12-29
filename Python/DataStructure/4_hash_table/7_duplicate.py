'''
包含冗余
'''


def containsDuplicate(nums):
    return len(nums) != len(set(nums))


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(containsDuplicate(nums))
