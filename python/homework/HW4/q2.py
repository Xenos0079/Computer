"""
You are only permitted to write code between Start and End.
Don't change the template. Otherwise, you will get zero point.
"""


## Here you can write some extra code if needed, or you can igore this block.
# Start writing your code.
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
# End writing your code.


class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        # Start writing your code.
        node = Node(data , None)
        node.pointer = self.head
        self.head = node
        self.size = self.size+1
        # End writing your code.


    ## Here you can write some other functions inside the class if needed, or you can igore this block.
    # Start writing your code.

    # End writing your code.
    

def quick_sort(node):
    # Start writing your code.
    if node != None and node.pointer != None: # meet the need
        pivot , next = node , node.pointer # pivot
        left , right= Node('', None) , Node('', None) # vector
        left_tail , right_tail= left , right # vector tail
        while next != None: # meet the need
            if next.element < pivot.element: # left
                left_tail.pointer = next
                left_tail = next # change
            else: # right
                right_tail.pointer = next
                right_tail = next # change
            next = next.pointer # change
        left_tail.pointer = None # reset
        right_tail.pointer = None # reset
        leftPart = quick_sort(left.pointer) # recursive
        rightPart = quick_sort(right.pointer ) # recursive
        tail = leftPart # leftEnd
        if tail != None: # meet the need
            while tail.pointer !=None:
                tail = tail.pointer # change
        # Link the pivot to the right partition
            tail.pointer = pivot # reset
        else: # not meet
            leftPart = pivot # reset
        pivot.pointer = rightPart # link
        return leftPart # the left part 
    # End writing your code.
    else: # not meet
        return node # back



# We will write code as follows to check your answer. You can remain or delete the following code in the submission. Because the following code will be rewritten when checking your answer.
if __name__ == '__main__':
    test_list = SinglyLinkedList()
    nums = [4,2,3,1,0,5]  # An example. We will change it during testing.
    for num in nums:
        test_list.insert(num)
    first_node = test_list.head  # Get the first node of the linked list.
    p = quick_sort(first_node)
    while p.pointer != None:
        print(p.element)
        p = p.pointer
    print(p.element)
    
