'''
找到中间节点

    - size未知

    - 只对链表循环一次
'''
from single_list import Node, LinkList


def FindMedian(phead):
    if not phead or not phead.next:
        return -1

    slowpt = fastpt = phead

    while fastpt and fastpt.next:
        slowpt = slowpt.next
        fastpt = fastpt.next.next

    return slowpt


if __name__ == '__main__':
    node = Node(val=0)
    llist = LinkList(node)
    llist.append(1)
    llist.headinsert(-1)
    llist.insert(1, 3)
    llist.append(2)
    llist.travel()
    node = FindMedian(llist.head)
    print(node.val)
