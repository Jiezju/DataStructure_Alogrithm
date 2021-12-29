'''
按照词频对字符进行排序
'''


def frequencySort(s):
    dic = {}

    for ele in s:
        dic[ele] = dic.setdefault(ele, 0) + 1

    # print(dic.items())

    templst = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    result = ''

    for ele in templst:
        result += ele[0] * ele[1]

    return result


if __name__ == '__main__':
    s = "cccaaa"
    print(frequencySort(s))
