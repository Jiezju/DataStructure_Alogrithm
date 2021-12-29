'''
array queue
'''

class queue:
    capacity = 10
    def __init__(self):
        self.queue = [None] * queue.capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def length(self):
        return self.size

    def enqueue(self, item):
        if self.size == len(self.queue):
            self.resize()
        
        pos = (self.front + self.size) % len(self.queue)
        self.queue[pos] = item
        self.size += 1

    def resize(self):
        queue.capacity *= 2
        old = self.queue
        self.queue = [None] * queue.capacity
        walk = self.front
        for i in range(self.size):
            self.queue[i] = old[walk]
            walk = (walk + 1) % self.size
        self.front = 0

    def dequeue(self):
        if self.is_empty():
            return -1

        ans = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        self.size -= 1

        return ans
    
    def peek(self):
        return self.queue[self.front]

if __name__ == '__main__':
    q = queue()
    print(q.is_empty())
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.length())
    ana = q.dequeue()
    print(ana)
    print(q.peek())
