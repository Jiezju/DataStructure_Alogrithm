'''
list stack
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = next


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def length(self):
        return self.size

    def push(self, val):
        newNode = Node(val)
        self.size += 1
        if not self.head:
            self.head = newNode
            return
        newNode.nxt = self.head
        self.head = newNode

    def pop(self):
        if not self.head:
            return -1
        node = self.head
        self.head = self.head.nxt
        self.size -= 1

        return node.val

    def peek(self):
        if self.head:
            return self.head.val
        else:
            return -1

    def print(self):
        if not self.head:
            return -1

        cur = self.head

        while cur:
            print(cur.val)
            cur = cur.nxt

if __name__ == '__main__':
    stack = Stack()
    print(stack.size)
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    # stack.print()
    print(stack.pop())
    print(stack.pop())
    # stack.print()

