'''
交换对应的左右节点
'''

def mirror():
    _mirror(_root)

def _mirror(node):
    if node is None:
        return

    node.left, node.right = node.right, node.left

    _mirror(node.left)
    _mirror(node.right)
