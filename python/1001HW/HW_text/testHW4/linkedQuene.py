from linkedlist_origin import Node

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail =None
        self.size=0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        if self.is_empty:
            print(' Queue is empty.')
        else:
            return self.head.element
        
    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            answer = self.head.element
            self.head = self.head.pointer
            self.size -= 1
            if self.is_empty():
                self.tail = None
            return answer
        
    def enqueue(self,e):
        newest = Node(e,None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.pointer = newest
            self.tail = newest
            self.size += 1