'''
反转链表II

从位置m到n反转一个链表
'''


def reverseBetween(head, m, n):
    if not head:
        return -1

    tmphead = head

    for i in range(m):
        tmphead = tmphead.next

    cur = tmphead.next
    pre = None
    for i in range(n - m + 1):
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp

    tmphead.next.next = cur
    tmphead.next = pre

    return head
