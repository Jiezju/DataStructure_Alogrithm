'''
给定两个二叉树，如果它们在结构上相同，由具有相同值的节点组成则返回true 
'''


def sameTree(proot1, proot2):
    return _sameTree(proot1, proot2)


def _sameTree(node1, node2):
    if node1 is None and node2 is None:
        return True

    if node1 is None or node2 is None:
        return False

    if node1 is not None and node2 is not None:
        return _sameTree(node1.left, node2.left) and _sameTree(
            node1.right, node2.right
        ) and ode1.left == node2.left and node1.right == node2.right

    return False
