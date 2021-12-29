'''
valid brackets 
'''


def isValid(s):
    stack = []
    dic = {')': '(', ']': '[', '}': '{'}

    for ele in s:
        if s not in dic:
            stack.append(s)
        else:
            if not stack:
                return False
            elif dic[ele] == stack[-1]:
                stack.pop()
            else:
                return False

    return stack == []
