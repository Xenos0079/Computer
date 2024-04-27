# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''# from LeetCode

class Solution:
    def isPalindrome(self, head) -> bool:
        
        
        slow, fast = head, head
        q, r = None, None
        
        while fast and fast.next:
            r = q
            q = slow
            slow = slow.next
            fast = fast.next.next
            q.next = r
            
        if fast:
            slow = slow.next
        
  
        while slow and q:
            if slow.val != q.val:
                return False
            
            slow = slow.next
            q = q.next
        
        return True

''' # fast and slow pointers

# my code
class Solution:
    def isPalindrome(self, head) -> bool:
            re = []
            while head:
                re.append(head.val)
                head = head.next
            return re == re[::-1]
# create a list to store the data

# LeetBest
'''

import sys

with open('user.out', 'w') as f:
    while True:
        line = sys.stdin.readline().strip()[1:-1]
        if not line:
            break
        f.write('true\n' if line == line[::-1] else 'false\n')

exit(0)

'''
    

        