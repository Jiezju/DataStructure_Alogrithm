'''
BST查找Key
'''

def getIterative(key, root):
    node = root

    while node:
        if node.value == key:
            return node
        elif node.value < key:
            node = node.left
        else:
            node = node.right

    return None
