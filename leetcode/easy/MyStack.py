# 225. Implement Stack using Queues

# stack using 2 qs
# always keep one q full and other q empty

# when you are pushing, push the element onto the empty q
# and move the  element from the full q to empty q
# by popping them from the front of the full q
# after the full q is empty swap both the arrays

#  use the full q for all the other operations


class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        
        self.q1,self.q2=self.q2,self.q1

    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()