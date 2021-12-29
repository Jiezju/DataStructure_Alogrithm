'''
rotate array next great
'''


def nextGreat2(nums):
    stack, r = [], [-1] * len(nums)
    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]):
            r[stack.pop()] = nums[i]
        stack.append(i)
    print(r)
    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]):
            r[stack.pop()] = nums[i]
        if stack == []:
            break
    return r


if __name__ == '__main__':
    array = [37, 6, 4, 5, 2, 25]
    print(nextGreat2(array))
