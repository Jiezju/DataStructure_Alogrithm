'''
迭代法添加节点
'''

def addIterative(proot, item):
    return _addIterative(node, item)

def _addIterative(node, item):
    if node == None:
        return Node(item)
    
    if node.value == item:
        return None
    elif node.value < item:
        node.right = _addIterative(node.right, item)
    else:
        node.left = _addIterative(node.left, item)
    
    return node


def addIterative_(proot, item):
    node = proot

    while node:
        parent = node
        if node.value > item:
            node = node.left
        else:
            node = node.right

    if parent.value >  item:
        parent.left = Node(item)
    else:
        parent.right = Node(item)

    return proot
