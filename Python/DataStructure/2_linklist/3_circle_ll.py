'''
是否有环：判定一个链表是否存在环
'''


def has_circle(phead):
    if not phead or not phead.next:
        return False

    slowpt = fastpt = phead

    while fastpt and fastpt.next:
        slowpt = slowpt.next
        fastpt = fastpt.next.next

        if slowpt == fastpt:
            return True

    return False
