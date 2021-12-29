'''
list queue 
'''


class node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def length(self):
        return self.size

    def enqueue(self, item):
        newnode = node(item)

        self.size += 1
        if not self.head:
            self.head = self.tail = newnode
            return

        self.tail.next = newnode

    def dequeue(self):
        if not self.head:
            return -1

        tmp = self.head
        self.head = self.head.next
        self.size -= 1

        return tmp

    def peek(self):
        return self.tail
