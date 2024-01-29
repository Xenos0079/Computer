"""
You are only permitted to write code between Start and End.
Don't change the template. Otherwise, you will get zero point.
"""





class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer

## Here you can write some extra code if needed, or you can igore this block.
# Start writing your code.
left = Node('',None)
right = Node('',None)
# End writing your code.

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
    if node and node.pointer != None:
        pivot = node
        next = node.pointer
        if next != None:
            if next.element > pivot.element:
                right.pointer = next
                right = next
            else:
                left.pointer = next
                left = next
    LeftPart = quick_sort(left.pointer)
    RightPart = quick_sort(right.pointer)
    if LeftPart != None:
        if LeftPart.pointer != None:
            leftEnd = LeftPart.pointer
        leftEnd.pointer = pivot
    else:
        LeftPart = pivot
    pivot.pointer = RightPart
    return LeftPart
    # End writing your code.


# We will write code as follows to check your answer. You can remain or delete the following code in the submission. Because the following code will be rewritten when checking your answer.
if __name__ == '__main__':
    test_list = SinglyLinkedList()
    nums = [4,2,3,1,0,5]  # An example. We will change it during testing.
    for num in nums:
        test_list.insert(num)
    first_node = test_list.head  # Get the first node of the linked list.
    p = quick_sort(first_node)
    print(p)
    while p.pointer != None:
        print(p.element)
        p = p.pointer
    print(p.element)
    

