from DoubleLinkList import DoubleLinkList as dlist
from DoubleLinkList import Node


class FIFOCache:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.map = {}
        self.dlist = dlist(capacity)

    def get(self, key):
        if key not in self.map:
            return -1
        else:
            node = self.map[key]
            return node.value

    def set(self, key, value):
        if self.capacity == 0:
            return

        if key in self.map:
            node = self.map[key]
            self.dlist.remove(node)
            node.value = value
            self.dlist.append(node)
        else:
            if self.dlist.size == self.capacity:
                node = self.dlist.pop()
                del self.map[node.key]
            node = Node(key, value)
            self.map[node.key] = node
            self.dlist.append(node)

    def print(self):
        self.dlist.print()


if __name__ == '__main__':
    cache = FIFOCache(2)
    cache.set(1, 1)
    cache.print()
    cache.set(2, 2)
    cache.print()
    print(cache.get(1))
    cache.set(3, 3)
    cache.print()
    print(cache.get(2))
    cache.print()
    cache.set(4, 4)
    cache.print()
    print(cache.get(1))
