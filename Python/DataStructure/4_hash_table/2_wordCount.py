'''
统计单词数
'''


def wordCount(s):

    dic = {}

    words = s.split(' ')
    for word in words:
        dic[word] = dic.setdefault(word, 0) + 1

    return dic


if __name__ == '__main__':
    s = "Hello World How are you I am fine thank you and you"
    print(wordCount(s))
