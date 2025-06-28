class queue:
    def __init__(self):
        self.start=-1
        self.end=-1
        self.size=1000
        self.cursize=0
        self.arr=[0]*self.size
    def push(self,val):
        if(self.cursize>=self.size):
            print("queue is full")
            exit(1)
        elif(self.start==-1):
            self.start=0
            self.end=0
        else:
           self.end=(self.end+1)%self.size
        self.arr[self.end]=val
        self.cursize+=1
    def Top(self):
        if(self.cursize==0):
            print("queue is empty")
            exit(1)
        return(self.arr[self.end])
    def pop(self):
        if(self.cursize==0):
            print("queue is empty")
            exit(1)
        ele=self.arr[self.end]
        if(self.cursize==1):
            self.satrt=-1
            self.end=-1
        else:
            self.start=(self.start+1)%self.size
        self.cursize-=1
        return(ele)
    def Size(self):
        return(self.cursize)
q = queue()
q.push(4)
q.push(14)
q.push(24)
q.push(34)
print("The peek of the queue before deleting any element", q.Top())
print("The size of the queue before deletion", q.Size())
print("The first element to be deleted", q.pop())
print("The peek of the queue after deleting an element", q.Top())
print("The size of the queue after deleting an element", q.Size())



