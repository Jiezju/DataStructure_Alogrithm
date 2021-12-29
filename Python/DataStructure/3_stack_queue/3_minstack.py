'''
最小堆栈
'''


class Minstack:
    def __init__(self):
        self.instack = []
        self.minstack = []

    def push(self, item):
        self.instack.append(item)

        if not self.minstack:
            self.minstack.append(item)
        else:
            if item <= self.minstack[-1]:
                self.minstack.append(item)

    def pop(self):
        ans = self.instack.pop()

        if ans == self.minstack[-1]:
            self.minstack.pop()

        return ans

    def getMin(self):
        if not self.minstack:
            return -1
        return self.minstack[-1]
