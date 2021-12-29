'''
reverse string
'''


def reverseString(string):
    stack = []
    for s in string:
        stack.append(s)

    res = []
    while stack:
        res.append(stack.pop())

    return ''.join(res)


def isPalindrome(string):
    return string == reverseString(string)


if __name__ == '__main__':
    string = 'hello'
    res = reverseString(string)
    print(res)
    print(isPalindrome(string))
