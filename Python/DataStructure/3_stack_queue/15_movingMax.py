'''
滑动窗口最大值
'''


def movingMax(arr, k):
    res = []
    window = []

    for i, ele in enumerate(arr):
        if i + 1 >= k and window[0] + k <= i:
            window.pop(0)

        while window and arr[window[-1]] <= ele:
            window.pop()

        window.append(i)

        if i + 1 >= k:
            res.append(arr[window[0]])

    return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(movingMax(nums, 3))
