'''
宝石和石头
'''


def numJewelsInStones(J, S):
    js = set(J)

    res = 0
    for ele in S:
        if ele in js:
            res += 1

    return res


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J, S))
