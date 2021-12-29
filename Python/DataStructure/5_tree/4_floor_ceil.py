'''
查找floor ceil
'''


def floor(key):
    return _floor(root, key)


def _floor(node, key):
    if node is None:
        return None

    if node.value == key:
        return node

    if node.value > key:
        return _floor(node.left, key)

    t = _floor(node.right, key)

    if t:
        return t

    return node


def ceil(key):
    return _ceil(root, key)


def _ceil(node, key):
    if node is None:
        return None

    if node.value == key:
        return node

    if node.value < key:
        return _ceil(node.right, key)

    t = _ceil(node.left, key)

    if t:
        return t

    return node
