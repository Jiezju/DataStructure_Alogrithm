'''
删除倒数第N个节点：删除一个链表中的倒数第N个节点
'''


def removeN(pHead, n):
    if not pHead:
        return -1

    firstpt = pHead
    for i in range(n):
        if firstpt.next:
            firstpt = firstpt.next
        else:
            return -1

    secondpt = pHead

    while firstpt:
        firstpt = firstpt.next
        secondpt = secondpt.next

    return secondpt
