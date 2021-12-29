'''
快乐数（happy number）有以下的特性：在给定的进位制下，该数字所有数位(digits)的平方和，得到的新数再次求所有数位的平方和，如此重复进行，最终结果必为1
'''


def isHappy(n):
    visited = set()

    while n not in visited:
        visited.add(n)
        n = sum([int(i)**2 for i in str(n)])
    return n == 1


if __name__ == '__main__':
    n = 19
    print(isHappy(n))
