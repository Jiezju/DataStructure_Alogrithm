'''
树的左右子树是彼此结构清晰的镜像
'''


def isFoldable(root):
    if root is None:
        return True
    return __isFoldable(root.left, root.right)


def __isFoldable(node1, node2):
    if node1 is None and node2 is None:
        return True

    if node1 is None or node2 is None:
        return False

    if node1.value == node2.value:
        return __isFoldable(node1.left, node2.right) and __isFoldable(
            node1.right, node2.left)

    return False
