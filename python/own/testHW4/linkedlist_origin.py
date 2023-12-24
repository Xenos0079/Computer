class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self,e):
        newest = Node(e , None)
        newest.pointer = self.head
        self.head = newest
        self.size = self.size+1

    def add_last(self,e):
        newest = Node(e,None)
        if self.size > 0:
            self.tail.pointer = newest
        else:
            self.head = newest
            self.tail = newest
            self.size = self.size+1

    def remove_first(self):
        if self.size == 0:
            print(' The linked list is empty')
        elif self.size == 1:
            answer = self.head.element
            self.head = None
            self.tail = None
            self.size -= 1
            return answer
        else:
            answer = self.head.element
            self.head = self.head.pointer
            self.size = self.size - 1
            return answer
        

