'''
 日常温度
'''


def dailyTemperatures(temperatures):
    stack = []
    result = []

    for i, ele in enumerate(temperatures):
        while stack and ele > stack[-1][0]:
            _, idx = stack.pop()
            result.append(i - idx)

        stack.append([ele, i])
    
    while stack:
        stack.pop()
        result.append(0)

    return result


if __name__ == '__main__':
    t = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(t))
