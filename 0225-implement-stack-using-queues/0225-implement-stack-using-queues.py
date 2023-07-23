class MyStack:

    def __init__(self):
        self.q = deque() #create queue

    def push(self, x: int) -> None:
        self.q.append(x) #putting new element on far right of queue

    def pop(self) -> int:
        for i in range(len(self.q) - 1): #for all besides last value
            self.push(self.q.popleft()) #removes far left element and returns it for adding to rightside
            
        #every element besides the one on top has been rotated to the back, which leaves the original top element
        return self.q.popleft() #returns far left element

    def top(self) -> int:
        return self.q[-1] #returning rightmost element

    def empty(self) -> bool:
        return len(self.q) == 0 #true if empty, false if not


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()