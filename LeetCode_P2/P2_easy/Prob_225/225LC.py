import collections
class MyStack:

    def __init__(self):
        self.stack = collections.deque() # only one deque
        
    def push(self, x: int) -> None:
        self.stack.append(x) # add it to the last place
        
    def pop(self) -> int:
        n = len(self.stack) # find the length? is that permitted?
        for i in range(n-1):
            x = self.stack.popleft()
            self.stack.append(x)
            n -= 1
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[-1]
        
    def empty(self) -> bool:
        return len(self.stack) == 0