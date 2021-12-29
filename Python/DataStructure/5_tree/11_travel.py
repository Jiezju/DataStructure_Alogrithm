'''
travel
'''


def printPreorderIterative(proot):
    if proot is None:
        return None
    
    node = proot
    stack = []
    result = []

    while node or stack:
        while node:
            result.append(node)
            stack.append(node)
            node = node.left  
        
        leftnode = stack.pop()
        node = leftnode.right

    return result


def printInorderIterative(proot):
    if proot is None:
        return None

    node = proot
    stack = []
    res = []

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        leftnode = stack.pop()
        res.append(leftnode)
        node = leftnode.right

    return res

def printPostorderIterative(proot):
    node = proot
    stack = []
    res = []

    while stack or node:
        while node:
            res.append(node)
            stack.append(node)
            node = node.right

        leftNode = stack.pop()
        node = leftNode.left

    return res[::-1]
