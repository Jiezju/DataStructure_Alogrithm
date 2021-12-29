from DoubleLinkList import DoubleLinkList as dlist
from DoubleLinkList import Node


class LRUCache:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.map = {}
        self.dlist = dlist(self.capacity)

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.dlist.remove(node)
            self.dlist.append_front(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        if key in self.map:
            node = self.map[key]
            self.dlist.remove(node)
            node.value = value
            self.dlist.append_front(node)
        else:
            if self.dlist.size == self.capacity:
                node = self.dlist.remove(self.dlist.tail)
                del self.map[node.key]
            newNode = Node(key, value)
            self.map[key] = newNode
            self.dlist.append_front(newNode)

    def print(self):
        self.dlist.print()


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.set(2, 2)
    cache.print()
    cache.set(1, 1)
    cache.print()
    cache.set(3, 3)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()
