# 232. Implement Queue using Stacks

# take 2 stacks always keep one as empty
# and consider the empty stack as a secondary stack

# in the push(), move all the elements from 
# primary stack to secondary stack
#  once the primary stack is empty insert the 
# element into the primary stack
# and copy the elements from secondary stack
#  to the primary stack until the secondary stack
#  is empty 

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.s1.append(x)
        
        while self.s2:
            self.s1.append(self.s2.pop())
        
    def pop(self) -> int:
        return self.s1.pop()    

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()