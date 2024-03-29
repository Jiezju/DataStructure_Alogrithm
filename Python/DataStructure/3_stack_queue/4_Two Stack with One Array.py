class twoStacks:
     
    def __init__(self, n): 
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size
         
    # Method to push an element x to stack1
    def push1(self, x):
         
        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1 :
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
 
        else:
            print("Stack Overflow ")
 
    # Method to push an element x to stack2
    def push2(self, x):
 
        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
 
        else :
           print("Stack Overflow ")
 
    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 -1
            return x
        else:
            print("Stack Underflow ")
 
    # Method to pop an element from second stack
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow ")
