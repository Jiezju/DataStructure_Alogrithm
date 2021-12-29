'''
用插入排序对一个链表做排序
'''
from single_list import Node


def InsertSort(phead):
    if not phead:
        return False
    dummy = Node(0)
    dummy.next = phead
    cur = phead

    while cur:
        pre = dummy

        while pre.next and pre.next.val < cur.val:
            pre = pre.next

        if pre == cur:
            cur = cur.next
        else:
            tmp = cur.next
            pre.next.next = tmp
            cur.next = pre.next
            pre.next = cur
            cur = tmp

    return dummy.next
