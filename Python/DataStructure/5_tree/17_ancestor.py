'''
二叉搜索树的第一个共同祖先
'''


def lowestCommonAncestor_binary(p, q):
    return _lowestCommonAncestor_binary(root, p, q)


def _lowestCommonAncestor_binary(node, p, q):
    if node.value < p.value and node.value < q.value:
        return _lowestCommonAncestor_binary(node.right, p, q)

    if node.value > p.value and node.value > q.value:
        return _lowestCommonAncestor_binary(node.left, p, q)

    return node


'''
普通树的两个节点的公共祖先
'''


def lowestCommonAncestor(p, q):
    return __lowestCommonAncestorHelper(root, p, q)


def __lowestCommonAncestorHelper(node, p, q):
    if node is None:
        return None

    if node == p or node == q:
        return node

    left = __lowestCommonAncestorHelper(node.left, p, q)
    right = __lowestCommonAncestorHelper(node.right, p, q)

    if left is None:
        return right

    if right is None:
        return left

    return node
