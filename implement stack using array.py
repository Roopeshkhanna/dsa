class stack:
    def __init__(self):
        self.size=1000
        self.top=-1
        self.arr=[0]*self.size
    def push(self,val):
        if(self.size<=0):
            return("stack is full")
        self.top+=1
        self.arr[self.top]=val
        self.size-=1
    def Top(self):
        if(self.top==-1):
            return("stack is empty")
        return(self.arr[self.top])
    def pop(self):
        if(self.top==-1):
            return("stack is empty")
        val=self.arr[self.top]
        self.top-=1
        return(val)
    def Size(self):
        return(self.top+1)

st=stack()    
st.push(5)
print(st.Top())
print(st.pop())
print(st.Size())


        
