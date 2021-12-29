'''
给定一个单词的List，返回可以用一行键盘字母输出的单词
'''


def findWords(words):
    dic = {}
    res = []

    for ele in 'qwertyuiop':
        dic[ele] = 1
    for ele in 'asdfghjkl':
        dic[ele] = 2
    for ele in 'zxcvbnm':
        dic[ele] = 3

    for word in words:
        wordlow = word.lower()
        flag = True
        key = dic[wordlow[0]]

        for c in wordlow[1:]:
            if dic[c] != key:
                flag = False
                break

        if flag:
            res.append(word)

    return res


if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(findWords(words))
