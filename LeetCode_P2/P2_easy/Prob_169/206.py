# Reverse Linked list



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

''' #1
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        elif not head.next:
            return head
        new = None
        if head and head.next:
            temp = head
            temp.next = new
            new = temp
            head = head.next
        return new
'''

#'''#2
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        new = None
        while head and head.next: # REMEMBER TO CHECK THE LOOP: while/if
            temp = head
            temp.next = new
            new = temp
            head = head.next
        head.next = new
        return head     
#'''

"""# By ChatOS
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new = None

        while head:
            temp = head
            head = head.next
            temp.next = new
            new = temp

        return new
"""