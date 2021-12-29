'''
反转字符串
'''


def reverse_(s, case):
    if case == 1:
        ls = list(s)
        ls.reverse()
        return ''.join(ls)
    elif case == 2:
        ls = list(s)
        return ''.join(ls[::-1])
    else:
        ls = list(s)
        left = 0
        right = len(ls) - 1
        while left < right:
            ls[left], ls[right] = ls[right], ls[left]
            left += 1
            right -= 1

        return ''.join(ls)


if __name__ == '__main__':
    s = "hello"
    case = 3
    t = reverse_(s, case)
    print(t)
