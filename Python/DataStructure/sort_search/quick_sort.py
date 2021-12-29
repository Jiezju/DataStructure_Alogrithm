'''
快排
'''


def quickSort(nums, first, last):
    if first >= last:
        return

    pivot = nums[first]
    low = first
    high = last

    while low < high:
        while low < high and pivot < nums[high]:
            high -= 1
        nums[low] = nums[high]

        while low < high and pivot > nums[low]:
            low += 1
        nums[high] = nums[low]

    nums[low] = pivot

    quickSort(nums, first, low - 1)
    quickSort(nums, low + 1, last)

    return nums


if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 99]
    print(quickSort(l, 0, len(l) - 1))
