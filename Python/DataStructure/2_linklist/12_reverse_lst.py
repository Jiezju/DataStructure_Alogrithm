'''
反转一个链表
'''


def reverse(head):
    if not head:
        return -1

    pre = None
    cur = head

    while cur:
        tmp = cur.next
        cur.next = pre

        pre = cur
        cur = tmp

    return pre
