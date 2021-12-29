'''
从有序链表中删除重复元素
'''


def deleteDuplicates(head):
    if not head:
        return -1

    cur = head
    nxt = cur.next

    while cur and cur.next:
        while nxt and cur.val == nxt.val:
            nxt = nxt.next

        cur.next = nxt

        cur = cur.next

    return head
