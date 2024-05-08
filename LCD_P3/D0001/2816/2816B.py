# 2816. Double a Number Represented as a Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# LeetCode best
class Solution(object):
    def doubleIt(self, head):
        curr = head
        if curr.val > 4: # reach 10 after double
            head = ListNode(1, head)
            # ans = ListNode(1, head)
        while curr.next:
            curr.val = (curr.val * 2 + (curr.next.val > 4)) % 10
            curr = curr.next
        curr.val = (curr.val * 2) % 10

        return head