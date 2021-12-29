from single_list import Node


def partition(head, x):
    lnode = Node(0)
    rnode = Node(0)

    cur = head

    lpt = lnode
    rpt = rnode

    while cur:
        if cur.val < x.value:
            lpt.next = cur
            lpt = lpt.next
        else:
            rpt.next = cur
            rpt = rpt.next

        cur = cur.next

    x.next = rnode.next
    lpt.next = x

    return lnode.next
