'''
Linklist
operation: is_empty length travel append insertLL remove search
'''


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self, node=None):
        self._head = node # 哨兵节点
        self._size = 0 if self._head == None else 1

    def is_empty(self):
        return self._size == 0

    def length(self):
        return self._size

    def travel(self):
        cur = self._head

        while cur:
            print(cur.val, end=' ')
            cur = cur.next

        return 0

    def append(self, value):
        newnode = Node(val=value)

        cur = self._head

        while cur.next:
            cur = cur.next

        cur.next = newnode
        self._size += 1

        return self._head

    def headinsert(self, value):
        newNode = Node(val=value)
        self._size += 1
        if not self._head:
            self._head = newNode
            return 0

        newNode.next = self._head
        self._head = newNode

        return 0

    def insert(self, pos, val):
        if pos < -self._size or pos > self._size:
            return -1

        if pos < 0:
            pos = (pos + self._size) % self._size
            if pos == self._size - 1:
                self.append(value=val)
        if pos == 0:
            self.headinsert(value=val)

        count = 0
        cur = self._head
        newNode = Node(val=val)
        while count < (pos - 1):
            cur = cur.next
            count += 1

        newNode.next = cur.next
        cur.next = newNode

        self._size += 1

        return self._head

    def search(self, value):
        cur = self._head

        while cur:
            if cur.val == value:
                return True

            cur = cur.next

        return False

    def remove(self, value):
        if not self._head:
            return -1
        cur = self._head

        if self._head.val == value:
            self._head = None
            self._size -= 1
            return 0

        while cur.next:
            if cur.next.val == value:
                if cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None

                self._size -= 1

                return 0

            cur = cur.next

        return -1


def foo(llist, i):
    print('------------------', i, '-----------------')
    print(llist.is_empty())
    print('travel')
    llist.travel()
    print()
    print('travel')
    print(llist.length())


if __name__ == '__main__':
    node = Node(val=0)

    llist = LinkList(node)
    foo(llist, 0)

    llist.append(1)
    foo(llist, 1)

    llist.headinsert(-1)
    foo(llist, 2)

    llist.insert(1, 3)
    foo(llist, 3)

    print(llist.search(3))

    llist.remove(3)
    foo(llist, 4)
