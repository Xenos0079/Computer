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
        newest = Node(data , None)
        newest.pointer = self.head
        self.head = newest
        self.size = self.size+1

def count_node(node):
    return test_list.size


test_list = SinglyLinkedList()
nums = [4,2,3,1,0,-1]  # An example. We will change it during testing.
for num in nums:
    test_list.insert(num)
first_node = test_list.head
print('The number of nodes in test_list is:')
print(count_node(first_node))

