'''
砖墙
'''


def leastBricks(walls):
    dic = {}

    for wall in walls:
        for i in range(1, len(wall)):
            dic[sum(wall[:i])] = dic.setdefault(sum(wall[:i]), 0) + 1

    templst = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    return len(walls) - templst[0][1]


if __name__ == '__main__':
    walls = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2],
             [1, 3, 1, 1]]
    print(leastBricks(walls))

