'''
simplify path
'''


def simplifyPath(path):
    pathlst = path.split('/')
    tmp = []

    for ele in pathlst:
        if ele == '..':
            if tmp:
                tmp.pop()
            else:
                return -1
        elif ele == '.' or ele == '':
            continue
        else:
            tmp.append(ele)
    if len(tmp) == 0:
        return '/'

    result = ['/' + i for i in tmp]

    return ''.join(result)


if __name__ == '__main__':
    res = simplifyPath("/a/./b/../../c/")
    print(res)
