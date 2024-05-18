'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
count = 0

from typing import Optional

class Solution:
    def distributeCoins(self, root: Optional[TreeNode], parent = None) -> int:

        def move(child, parent, distance):
            global count
            if parent:
                d = 1 - parent.val - distance
                count += 1
            else:
                d = 0
            return d

        if root.left:
            self.distributeCoins(root.left, root)
        if root.right:
            self.distributeCoins(root.right, root)

        d1 = 1 - root.val
        d2 = move(root, parent, d1)

        return count

'''