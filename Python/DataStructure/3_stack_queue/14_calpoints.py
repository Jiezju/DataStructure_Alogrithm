'''
棒球比赛
'''


def calPoints(ops):
    stack = []

    for op in ops:
        if op.isdigit():
            stack.append(int(op))
        elif op == 'C':
            if stack:
                stack.pop()
        elif op == 'D':
            stack.append(stack[-1] * 2)
        elif op == '+':
            stack.append(stack[-1] + stack[-2])
        else:
            continue

    return sum(stack)


if __name__ == '__main__':
    ops = ["5", "2", "C", "D", "+"]
    res = calPoints(ops)
    print(res)
