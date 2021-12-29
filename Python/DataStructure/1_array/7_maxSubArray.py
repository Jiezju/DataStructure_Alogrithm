'''
最长连续子串
给一个只包含0和1的数组，找出最长的全是1的子数组。

Example:

Input: [1,1,0,1,1,1]

Output: 3
'''


def find_consecutive_ones(nums):
    global_max = local_max = 0
    for i in nums:
        if i == 1:
            local_max += 1
        else:
            local_max = 0
        global_max = max(global_max, local_max)

    return global_max


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1]
    result = find_consecutive_ones(nums)
    print(result)
