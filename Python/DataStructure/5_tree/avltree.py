'''
平衡树判定：
任何节点的两个子树高度最多相差1

'''


def _maxDepth(node):
    if node is None:
        return 0
    return 1 + max(_maxDepth(node.left), _maxDepth(node.right))


def AVLvalid():
    return _AVLvalid(root)


def _AVLvalid(node):
    if node is None:
        return True

    if abs(_maxDepth(node.left) - _maxDepth(node.right)) > 1:
        return False

    return _AVLvalid(node.left) and _AVLvalid(node.right)
