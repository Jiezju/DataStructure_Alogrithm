'''
有效字谜
'''


def isAnagram1(s, t):
    dic1 = {}
    dic2 = {}

    for ele in s:
        dic1[ele] = dic1.setdefault(ele, 0) + 1
    for ele in t:
        dic2[ele] = dic2.setdefault(ele, 0) + 1

    return dic1 == dic2
