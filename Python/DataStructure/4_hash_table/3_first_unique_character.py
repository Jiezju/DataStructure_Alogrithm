'''
一个字符串中的首个独特的字
'''


def firstUniqChar(s):
    dic = {}

    for ele in s:
        dic[ele] = dic.setdefault(ele, 0) + 1

    for idx, ele in enumerate(s):
        if dic[ele] == 1:
            return idx

    return -1

def firstUniqChar2(s):
    letters='abcdefghijklmnopqrstuvwxyz'
    index=[s.index(l) for l in letters if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1


if __name__ == '__main__':
    s = "ifitdoesnotexist"
    print(firstUniqChar(s))
