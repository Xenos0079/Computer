# 2816. Double a Number Represented as a Linked List
# My Code

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# import module
import sys
sys.set_int_max_str_digits(0)

class Solution:
    def doubleIt(self, head):
        col = 0
        ans = ListNode()
        pointer = ans
        while head:
            col = col * 10 + head.val
            head = head.next
        col *= 2
        temp = str(col)
        for _ in temp:
            pointer.next = ListNode(int(_))
            pointer = pointer.next
        return ans.next