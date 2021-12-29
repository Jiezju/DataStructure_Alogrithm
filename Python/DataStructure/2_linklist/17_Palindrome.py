'''
回文链表
'''

from single_list import Node


def isPalindrome(head):
    if not head:
        return -1

    spt = fpt = head

    while fpt and fpt.next:
        spt = spt.next
        fpt = fpt.next.next

    head1 = Node(0)
    head2 = Node(0)

    head1.next = head
    if fpt:
        head2.next = spt.next
    else:
        head2.next = spt

    pre = None
    cur = head

    while cur:
        tmp = cur.next
        cur.next = pre

        pre = cur
        cur = tmp

    head1.next = pre

    while head1 and head2:
        if head1.val == head2.val:
            head1 = head1.next
            head2 = head2.next
        else:
            return False

    return True
