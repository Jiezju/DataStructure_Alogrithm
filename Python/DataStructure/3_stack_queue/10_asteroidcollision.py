'''
asteroidCollision
'''


def asteroidCollision(asteroids):
    stack = []

    for ele in asteroids:
        if stack and ele < 0 < stack[-1]:
            if stack[-1] <= -ele:
                stack.pop()
        else:
            stack.append(ele)

    return stack


if __name__ == '__main__':
    asteroids = [5, 10, -5]
    res = asteroidCollision(asteroids)
    print(res)
