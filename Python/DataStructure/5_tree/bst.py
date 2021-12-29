'''
BinarySearchTree
'''


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def size(self):
        return self._size(self._root)

    def maxDepth(self):
        return self._maxDepth(self._root)

    def isEmpty(self):
        return self._root is None

    def search(self, key):
        return self._search(self._root, key)

    def insert(self, key):
        return self._insert(self._root, key)

    def preOrder(self):
        return self._preOrder(self._root)

    def inOrder(self):
        return self._inOrder(self._root)

    def postOrder(self):
        return self._postOrder(self._root)

    def _postOrder(self, node):
        if node is None:
            return
        
        self._postOrder(node.left)
        self._postOrder(node.right)
        print(node.value)

    def _inOrder(self, node):
        if node is None:
            return

        self._inOrder(node.left)
        print(node.value)
        self._inOrder(node.right)

    def _preOrder(self, node):
        if node is None:
            return None

        print(node.value)
        self._preOrder(node.left)
        self._preOrder(node.right)

    def _search(self, node, key):
        if node is None:
            return None

        if node.key == key:
            return node
        elif node.key < key:
            return self._search(node.right, key)
        else:
            return self._search(node.left, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if node.key == key:
            return -1
        elif node.key > key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        return node

    def _size(self, node):
        if node is None:
            return 0

        return self._size(node.left) + 1 + self._size(node.right)

    def _maxDepth(self, node):
        if node is None:
            return 0

        return 1 + max(self._maxDepth(node.left), self._maxDepth(node.right))
