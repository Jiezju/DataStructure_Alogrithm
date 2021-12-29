'''
LFUCache
'''

from DoubleLinkList import DoubleLinkList as dlist
from DoubleLinkList import Node


class LFUNode(Node):
    def __init__(self, key, value):
        super().__init__(key, value)
        self.freq = 1


class LFUCache:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.map = {}  # {node.key: node}
        self.freq_map = {}  # {freq: dlist}
        self.size = 0

    def __update_freq(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)

        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]

        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = dlist(10)
        self.freq_map[node.freq].append(node)

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self.__update_freq(node)
        return node.value

    def set(self, key, value):
        if self.capacity == 0:
            return
        if key in self.map:
            node = self.map[key]
            # self.freq_map[node.freq].remove(node)
            node.value = value
            self.__update_freq(node)
        else:
            if self.size == self.capacity:
                min_freq = min(self.freq_map)
                node = self.freq_map[min_freq].pop()
                del self.map[node.key]
                self.size -= 1
            lfu_node = LFUNode(key, value)
            if lfu_node.freq not in self.freq_map:
                self.freq_map[lfu_node.freq] = dlist(10)
            self.freq_map[lfu_node.freq].append(lfu_node)
            self.map[lfu_node.key] = lfu_node
            self.size += 1

    def print(self):
        print('***************************')
        for k, v in self.freq_map.items():
            print('Freq = %d' % k)
            self.freq_map[k].print()
        print('***************************')
        print()


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.set(1, 1)
    cache.print()
    cache.set(2, 2)
    cache.print()
    print(cache.get(1))
    cache.print()
    cache.set(3, 3)
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()
    cache.set(4, 4)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(3))
    cache.print()
    print(cache.get(4))
    cache.print()
