class myQueue:
    def __init__(self, n):
        self.arr = [-1] * n
        self.size = n
        self.front = 0
        self.rear = -1
        self.count = 0

    
    def isEmpty(self):
        return self.count == 0

    
    def isFull(self):
        return self.count == self.size

    
    def enqueue(self, x):
        if self.isFull():
            return 
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = x
        self.count += 1

    
    def dequeue(self):
        if self.isEmpty():
            return
        self.arr[self.front] = -1
        self.front = (self.front + 1) % self.size
        self.count -= 1
        

    
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front]
       
    
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[self.rear]
        
        