'''
森林里的兔子
'''

from math import ceil


def numRabbits(answers):
    dic = {}

    for ele in answers:
        dic[ele] = dic.setdefault(ele, 0) + 1

    result = 0
    for k, v in dic.items():
        k += 1
        result += ceil(v / k) * k

    return result


if __name__ == '__main__':
    answers = [1, 1, 2]
    print(numRabbits(answers))
