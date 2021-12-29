'''
DoubleLinkList
'''


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return '{}:{}'.format(self.key, self.value)

    def __repr__(self):
        return '{}:{}'.format(self.key, self.value)


class DoubleLinkList:
    def __init__(self, capacity=0xffff):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def __add_head(self, node):
        if not self.head:
            self.head = self.tail = node
            self.head.prev = None
            self.head.next = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None

        self.size += 1

    def __add_tail(self, node):
        if not self.tail:
            self.head = self.tail = node
            self.tail.next = None
            self.tail.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

        self.size += 1

    def __del_tail(self):
        if not self.tail:
            return
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = self.next = None

    def __del_head(self):
        if not self.head:
            return

        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = self.next = None

    def __remove(self, node):
        if not node:
            node = self.tail
        if node == self.tail:
            self.__del_tail()
        elif node == self.head:
            self.__del_head()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1

        return node

    def pop(self):
        return self.__remove(self.tail)

    def append(self, node):
        return self.__add_tail(node)

    def append_front(self, node):
        return self.__add_head(node)

    def remove(self, node):
        return self.__remove(node)
