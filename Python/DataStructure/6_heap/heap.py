'''
MaxHeap
'''


class MaxHeap:
    def __init__(self, capacity=0):
        self._capacity = capacity
        self._count = 0
        self._data = [None] * capacity

    def isEmpty(self):
        return self._count == 0

    def size(self):
        return self._count

    def add(self, item):
        if self._count >= self._capacity:
            return -1

        self._data[self._count] = item
        self._shift_up(self._count)
        self._count += 1

    def _shift_up(self, index):
        while index >= 1 and self._data[index] > self._data[(index - 1) // 2]:
            self._data[index], self._data[(index - 1) //
                                          2] = self._data[(index - 1) //
                                                          2], self._data[index]
            index = (index - 1) // 2

    def popMax(self):
        if self._count <= 0:
            return -1

        res = self._data[0]
        self._data[0] = self._data[self._count - 1]
        self._shift_down(0)
        self._count -= 1
        return res

    def _shift_down(self, index):
        while 2 * index + 1 < self._count:
            k = 2 * index + 1
            if k + 1 < self._count and self._data[k + 1] > self._data[k]:
                k += 1
            if self._data[index] > self._data[k]:
                break
            self._data[k], self._data[index] = self._data[index], self._data[k]
            index = k


if __name__ == '__main__':
    heap = MaxHeap(5)
    heap.add(1)
    heap.add(2)
    heap.add(3)
    heap.add(4)
    heap.add(5)
    for i in range(5):
        print(heap.popMax())
