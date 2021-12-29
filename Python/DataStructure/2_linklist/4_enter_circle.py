'''
环的开始：给定一个循环链表，找到环的入口节点
'''


def CircleEnter(phead):
    if not phead or not phead.next:
        return False

    slowpt = fastpt = phead

    while fastpt and fastpt.next:
        slowpt = slowpt.next
        fastpt = fastpt.next.next

        if slowpt == fastpt:
            break

    if fastpt is None or fastpt.next is None:
        return None

    slowpt = phead

    while slowpt != fastpt:
        slowpt = slowpt.next
        fastpt = fastpt.next

    return slowpt
