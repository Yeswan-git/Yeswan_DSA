class myStack:
    def __init__(self, n):
        self.n = n
        self.arr = [-1] * n
        self.top = -1
    
    def isEmpty(self):
        return self.top == -1 
    
    def isFull(self):
        return self.top == self.n - 1 
    
    def push(self, x):
        if not self.isFull():
            self.top += 1
            self.arr[self.top] = x
        else:
            pass
    
    def pop(self):
        if not self.isEmpty():
            val = self.arr[self.top]
            self.arr[self.top] = -1
            self.top -= 1
            return val
        else:
            return -1
    
    def peek(self):
        if not self.isEmpty():
            return self.arr[self.top]
        return -1