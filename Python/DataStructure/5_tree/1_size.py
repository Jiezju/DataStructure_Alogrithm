def _size(node):
    if not node:
        return 0
    return _size(node._left) + _size(node._right) + 1