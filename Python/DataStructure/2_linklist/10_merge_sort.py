'''
归并排序
'''

from single_list import Node


def merge_sort(head):
    if not head.next or not head:
        return head

    # 二分链表
    spt = fpt = head

    while fpt and fpt.next:
        spt = spt.next
        fpt = fpt.next.next
    newhead = spt.next
    spt.next = None

    lefthead = merge_sort(head)
    righthead = merge_sort(newhead)

    return merge(lefthead, righthead)


def merge(head1, head2):
    left = head1
    right = head2
    res = Node(0)
    while left and right:
        if left.val < right.val:
            res.next = left
            left = left.next
        else:
            res.next = right
            right = right.next

    res.next = left
    res.next = right

    return res.next
