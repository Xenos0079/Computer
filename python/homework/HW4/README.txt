I wrote this text file to explain my homework.
I used 3 py.files and each file represents one question in the assignment prief file pdf.
The title q1 means question1, q2 for  question2, etc.
The py. file can not be run directly to answer the question. 
You can use the code below to check my homework.
Run the program and enter them into the terminal to get feedback.

q1:
if __name__ == '__main__':
    test_list = SinglyLinkedList()
    nums = [4,2,3,1,0,-1]  # An example. We will change it during testing.
    for num in nums:
        test_list.insert(num)
    first_node = test_list.head  # Get the first node of the linked list.
    print('The number of nodes in test_list is:')
    print(count_node(first_node))

q2:
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

q3:
if __name__ == '__main__':
    n = 3  # An example. We will change it during testing.
    result_list = HanoiTower(n)
    for step in result_list:
        print(step['from'], '-->', step['to'])

Thanks for grading.