'''
第n个丑数
'''

import heapq


def is_uglyNumber(num):
    seq = [2, 3, 5]

    for t in seq:
        while num % t == 0:
            num //= t

    return num == 1


def Nth_UglyNum(n):
    q2, q3, q5 = [2], [3], [5]

    ugly = 1
    for u in heapq.merge(q2, q3, q5):
        if n == 1:
            return ugly
        if u > ugly:
            ugly = u
            n -= 1
            q2 += [u * 2]
            q3 += [u * 3]
            q5 += [u * 5]


if __name__ == '__main__':
    print(Nth_UglyNum(10))
