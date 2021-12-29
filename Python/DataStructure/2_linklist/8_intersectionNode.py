'''
找到两个链表的公共节点
'''


def getIntersectionNode(phead1, phead2):
    if not phead1 and not phead2:
        return -1

    cur1 = phead1
    cur2 = phead2

    while cur1 and cur2:
        if cur1 == cur2:
            return cur1
        cur1 = cur1.next
        cur2 = cur2.next

    if cur1:
        return getIntersectionhelper(cur1, phead1, phead2)
    if cur2:
        return getIntersectionhelper(cur2, phead2, phead1)


def getIntersectionhelper(cur, longhead, shorthead):
    count = 0
    while cur:
        cur = cur.next
        count += 1

    spt = shorthead
    fpt = longhead
    for i in range(count):
        fpt = fpt.next

    while spt != fpt:
        spt = spt.next
        fpt = fpt.next

    return spt

def getIntersectionNode2(phead1, phead2):
    # 不需要计数链表长度的方法 ，让cur1和cur2走相同的距离 必然相遇在交点处
    if not phead1 or not phead2:
        return -1

    cur1 = phead1
    cur2 = phead2

    while cur1 != cur2:
        if not cur1:
            cur1 = phead2
        if not cur2:
            cur2 = phead1
        cur1 = cur1.next
        cur2 = cur2.next

    return cur1
