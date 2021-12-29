'''
使用堆栈实现队列
'''


class QueueWithTwoStacks:
    def __init__(self):
        self.instack = []
        self.outstack = []
        self.size = 0

    def dequeue(self):
        if not self.outstack:
            if not self.instack:
                return -1
            while self.instack:
                self.outstack.append(self.instack.pop())
        self.size -= 1
        ans = self.outstack.pop()
        return ans

    def enqueue(self, item):
        self.instack.append(item)
        self.size += 1

    def peek(self):
        if not self.outstack:
            if not self.instack:
                return -1
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack[-1]
