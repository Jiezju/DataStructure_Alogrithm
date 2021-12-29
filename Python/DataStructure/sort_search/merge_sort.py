'''
归并排序
'''


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    leftnums = merge_sort(nums[:mid])
    rightnums = merge_sort(nums[mid:])

    return merge(leftnums, rightnums)


def merge(leftnums, rightnums):
    left = right = 0
    result = []

    while left < len(leftnums) and right < len(rightnums):
        if leftnums[left] < rightnums[right]:
            result.append(leftnums[left])
            left += 1
        else:
            result.append(rightnums[right])
            right += 1

    result += leftnums[left:]
    result += rightnums[right:]

    return result


if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 99]
    print(merge_sort(l))
