'''
给定一个列表，把它分成两个列表，一个是前半部分，一个是后半部分
'''


def half(pHead):
    if not pHead:
        return -1

    spt = fpt = pHead
    while fpt and fpt.next:
        spt = spt.next
        fpt = fpt.next.next

    newhead = spt.next
    spt.next = None

    return pHead, newhead
