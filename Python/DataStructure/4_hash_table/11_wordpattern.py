'''
单词模式
'''


def wordPattern(pattern, s):
    slist = s.split()
    dic = {}

    for ele1, ele2 in zip(pattern, slist):
        if ele1 in dic:
            if dic[ele1] != ele2:
                return False
        else:
            dic[ele1] = ele2

    return True


def wordPattern(pattern, s):
    dic = {}
    slist = s.split()

    for ele1, ele2 in zip(pattern, slist):
        if ele1 not in dic or ele2 not in dic:
            dic[ele1] = ele2
            dic[ele2] = ele1
        else:
            if dic[ele1] != ele2 or dic[ele2] != ele1:
                return False

    return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(wordPattern(pattern, s))
