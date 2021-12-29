'''
从有序链表中完全删除重复元素
'''

from single_list import Node


def deleteDuplicates2(head):
    dummy = pre = Node(0)
    dummy.next = head

    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next

            head = head.next
            pre.next = head

        else:
            pre = pre.next
            head = head.next

    return dummy.next
