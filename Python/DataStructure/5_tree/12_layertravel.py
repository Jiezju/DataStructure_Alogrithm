'''
层次遍历
'''


def levelOrder(proot):
    queue = [proot]
    res = []

    while queue:
        tmpres = []

        for i in range(len(queue)):
            node = queue.pop(0)
            tmpres.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(tmpres)
    return res


def levelOrder_reverse(proot):
    queue = [proot]
    res = []

    while queue:
        tmp = []

        for i in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.insert(0, tmp)

    return res


def zigzagLevelOrder(proot):
    queue = [proot]
    res = []
    flag = 1
    while queue:
        tmp = []
        for i in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res += tmp[::flag]
        flag *= -1

    return res
