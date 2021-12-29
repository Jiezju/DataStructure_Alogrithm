'''
判断 bst
'''

import sys


def isBST():
    return _isBST(root, -sys.maxsize, sys.maxsize)


def _isBST(node, minValue, maxValue):
    if node is None:
        return True

    if node.value < minValue or node.value > maxValue:
        return False

    return _isBST(node.left, minValue, node.value) and _isBST(
        node.right, node.value, maxValue)
