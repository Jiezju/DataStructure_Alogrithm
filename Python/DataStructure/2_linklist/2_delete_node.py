def delete_node(head, node):
    if node == head:
        new_head = head.next
        head = None
        return new_head
    
    pre = None
    cur = head
    while cur:
        if cur == node:
            break
        pre = cur
        cur = cur.next

    pre.next = cur.next    
    
    return head
