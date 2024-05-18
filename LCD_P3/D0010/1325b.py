# 1325. Delete Leaves With a Given Value

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return # where 'return' means 'delete'

        if not root.left and not root.right and root.val == target:
            return

        root.left = self.removeLeafNodes(root.left, target)

        root.right = self.removeLeafNodes(root.right, target)
        
        if not root.left and not root.right and root.val == target:
            return
            
        return root # where 'return' means 'delete'