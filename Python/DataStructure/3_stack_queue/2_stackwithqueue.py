'''
使用队列实现堆栈
'''


class StackwithQ:
    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, item):
        self.size += 1
        self.queue.append(item)

        for i in range(self.size - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        if not self.queue:
            return -1
        self.size -= 1
        ans = self.queue.pop(0)
        return ans

    def peek(self):
        if not self.queue:
            return -1

        for i in range(self.size - 1):
            self.queue.append(self.queue.pop(0))

        return self.queue[0]
