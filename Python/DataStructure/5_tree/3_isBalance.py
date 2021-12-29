def _minDepth(node):
    if (not node):
        return 0
    left_depth = _minDepth(node._left)
    right_depth = _minDepth(node._right)
    return min(left_depth, right_depth) + 1

def isBalanced():
    return (maxDepth(root) - minDepth(root)) <= 1