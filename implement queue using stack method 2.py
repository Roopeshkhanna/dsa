from queue import LifoQueue
# using LifoQueue which is a stack in python




class MyQueue:
    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()


    # Push element x to the back of queue.
    def push(self, x: int) -> None:
        print("The element pushed is ", x)
        self.input.put(x)


    # Removes the element from in front of queue and returns that element.
    def pop(self) -> int:
        # shift input to output
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
        x = self.output.get()
        return x


    # Get the front element.
    def top(self) -> int:
        # shift input to output
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
        return self.output.queue[-1]


    def size(self) -> int:
        return self.input.qsize() + self.output.qsize()




if __name__ == "__main__":
    q = MyQueue()
    q.push(3)
    q.push(4)
    print("The element poped is ", q.pop())
    q.push(5)
    print("The top of the queue is ", q.top())
    print("The size of the queue is ", q.size())