'''
成对交换节点
'''

from single_list import Node


def swapPairs(head):
    if not head:
        return -1

    newNode = Node(0)
    newNode.next = head

    pre = newNode
    cur = pre.next
    tmp = cur.next

    while cur and cur.next:
        pre.next = tmp
        cur.next = tmp.next.next
        tmp.next = cur

        pre = cur
        cur = cur.next

    return newNode.next
