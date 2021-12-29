def _maxDepth(node):
    if (not node):
        return 0
    left_depth = _maxDepth(node._left)
    right_depth = _maxDepth(node._right)
    return max(left_depth, right_depth) + 1