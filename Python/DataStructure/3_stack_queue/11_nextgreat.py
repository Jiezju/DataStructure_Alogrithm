'''
下一个大元素
'''


def nextGreat_(nums):

    stack = []
    dic = {}

    for ele in nums:
        while stack and ele > stack[-1]:
            temp = stack.pop()
            dic[temp] = ele

        stack.append(ele)

    while stack:
        temp = stack.pop()
        dic[temp] = -1

    return dic


if __name__ == '__main__':
    nums = [6, 4, 5, 2, 25]
    print(nextGreat_(nums))
