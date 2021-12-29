'''
在一个string中找到所有的有效字谜
Input: s: "cbaebabacd" p: "abc"

Output: [0, 6]
'''


def findAnagrams(s, p):
    result = []
    m = len(p)
    n = len(s)

    if n < m:
        return result

    # 使用数组表示字典
    shash = [0] * 123
    phash = [0] * 123

    for ele in p:
        phash[ord(ele)] += 1

    for ele in s[:m - 1]:
        shash[ord(ele)] += 1

    # 遍历结果
    for i in range(m - 1, n):
        shash[ord(s[i])] += 1
        if i - m >= 0:
            shash[ord(s[i - m])] -= 1

        if shash == phash:
            result.append(i - m + 1)

    return result


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s, p))
