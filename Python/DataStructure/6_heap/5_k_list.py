'''
合并k个有序列表
'''

import heapq


def mergeKLists(lists):  # lists存放的是k个链表的头节点
    phead = Node(0)
    cur = phead

    heap = []

    for node in lists:
        heapq.heappush(heap, (node.value, node))

    while len(heap) > 0:
        _, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.value, node.next))

    return phead
