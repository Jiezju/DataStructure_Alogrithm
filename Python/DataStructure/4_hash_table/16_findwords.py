'''
给定一个单词的List，返回可以用一行键盘字母输出的单词。键盘如下：
'''

LINE1 = 'qwertyuiop'
LINE2 = 'asdfghjkl'
LINE3 = 'zxcvbnm'


def findWords(words):
    result = []

    dic = {}

    for ele in LINE1:
        dic[ele] = 1

    for ele in LINE2:
        dic[ele] = 2

    for ele in LINE3:
        dic[ele] = 3

    for word in words:
        temp = word.lower()
        res = True
        oneline = dic[temp[0]]
        for letter in temp[1:]:
            if dic[letter] != oneline:
                res = False

        if res:
            result.append(word)

    return result


if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(findWords(words))
