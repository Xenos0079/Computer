"""
You are only permitted to write code between Start and End.
Don't change the template. Otherwise, you will get zero point.
"""


## Here you can write some extra code if needed, or you can igore this block.
# Start writing your code.

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
        #create a node,set pointer to head of the singly linked list
        node=Node(data,self.head)
        #set the new node as the  head
        self.head=node
        #change the size
        self.size=self.size+1
        # End writing your code.


    ## Here you can write some other functions inside the class if needed, or you can igore this block.
    # Start writing your code.

    # End writing your code.
    

def quick_sort(node):
    # Start writing your code.
    if node is None or node.pointer is None:
        return node
    # Partitioning the list(The dummy nodes are for simplifying the partitioning logic)
    pivot = node
    left_dummy = Node(0, None)
    right_dummy = Node(0, None)
    left_tail = left_dummy
    right_tail = right_dummy
    current = node.pointer
    while current != None:
        if current.element < pivot.element:
            left_tail.pointer = current
            left_tail = current
        else:
            right_tail.pointer = current
            right_tail = current
        current = current.pointer
    # End of left and right partitions
    left_tail.pointer = None
    right_tail.pointer = None
    # Recursively sort left and right partitions
    left_sorted = quick_sort(left_dummy.pointer)
    right_sorted = quick_sort(right_dummy.pointer )
    # Concatenate partitions
    # Find the end of left partition
    tail = left_sorted
    if tail != None:
        while tail.pointer !=None:
            tail = tail.pointer
        # Link the pivot to the right partition
        tail.pointer = pivot
    else:
        left_sorted = pivot
    # Link pivot to right sorted list
    pivot.pointer = right_sorted
    return left_sorted
    # End writing your code.


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
    
