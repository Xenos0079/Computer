# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head:[ListNode]) ->[ListNode]:
        if not head or not head.next:
            return head
        new_head = head.next
        prev = None
        while head and head.next:
            first_node = head
            second_node = head.next
            # Swap the pair of nodes
            first_node.next = second_node.next
            second_node.next = first_node
            # Update the previous node's next pointer
            if prev:
                prev.next = second_node
            prev = first_node
            head = first_node.next
        return new_head