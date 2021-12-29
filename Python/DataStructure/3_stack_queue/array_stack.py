'''
stack 实现
'''


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def is_empty(self):
        return self.stack == []

    def length(self):
        return self.size

    def push(self, val=0):
        self.stack.append(val)
        self.size += 1

    def pop(self):
        if not self.stack:
            return -1
        self.size -= 1

        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return -1

        return self.stack[-1]

    def printStack(self):
        print(self.stack)



if __name__ == '__main__':
    stack = Stack()
    stack.printStack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.printStack()
    stack.is_empty()
    print(stack.peek())
    print(stack.pop())
    stack.printStack()
    print(stack.length())
