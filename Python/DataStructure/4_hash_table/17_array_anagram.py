'''
字谜组
'''


def groupAnagrams(strs):
    dic = {}

    for s in strs:
        key = ''.join(sorted(s))
        if key not in dic:
            dic[key] = [s]
        else:
            dic[key].append(s)

    return list(dic.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
