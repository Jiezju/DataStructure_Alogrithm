'''
stack sort
'''


def sortStack(stack):
    tmpstack = []

    for i in range(len(stack)):
        temp = stack.pop()

        if not tmpstack:
            tmpstack.append(temp)
        else:
            count = 0

            while tmpstack and tmpstack[-1] > temp:
                stack.append(tmpstack.pop())
                count += 1

            tmpstack.append(temp)

            while count:
                tmpstack.append(stack.pop())
                count -= 1

    return tmpstack


def sortstack_simple(stack):
    tmpstack = []  # 辅助栈

    while stack:
        tmp = tmpstack.pop()

        # 查找 tmp 应该在的位置
        while tmpstack and tmpstack[-1] > tmp:
            stack.append(tmpstack.pop())
        tmpstack.append(tmp)

    return tmpstack


if __name__ == '__main__':
    stack = [5, 2, 3, 1]
    res = sortStack(stack)
    print(res)
