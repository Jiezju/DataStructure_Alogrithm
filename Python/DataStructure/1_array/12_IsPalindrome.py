'''
 检验回文结构

• 给定一个字符串，检测其是否为回文结构。

• 只考虑字母和数字字符，不考虑大小写。

• 例如：”A man, a plan, a canal: Panama” 是回文结构，而”race a car”不是回文结构。
'''


def isPalindrome(s):
    res = ''
    s = s.lower()
    for ele in s:
        if ele.isdigit() or ele.isalpha():
            res += ele

    return res[::-1] == res


if __name__ == '__main__':
    s = 'A man, a plan, a canal: Panama'
    print(isPalindrome(s))
