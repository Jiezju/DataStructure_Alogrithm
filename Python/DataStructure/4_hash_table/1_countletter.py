'''
统计字母数
'''


def letterCount_(s):
    from collections import Counter
    c = Counter(x for x in s if x != ' ')

    return c


def letter_count(s):
    dic = {}

    for ele in s:
        if ele != ' ' and ele.isalpha():
            dic[ele] = dic.setdefault(ele, 0) + 1

    max_word = ''
    count = 0

    for key, val in dic.items():
        if val > count:
            count = val
            max_word = key

    return dic, max_word, count


if __name__ == '__main__':
    s = "Hello World How are you I am fine thank you and you"
    print(letterCount_(s))
