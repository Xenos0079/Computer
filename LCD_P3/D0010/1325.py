# 1325. Delete Leaves With a Given Value

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int, parent = None, direction = None) -> Optional[TreeNode]:
        def delete(current, parent, direction):
            if not current.left and not current.right: # leaf, current
                if direction == 1: # left
                    parent.left = None
                elif direction == 2: #right
                    parent.right = None

        d = direction

        if root.left:
            self.removeLeafNodes(root.left, target, root, 1)
        if root.right:
            self.removeLeafNodes(root.right, target, root, 2)

        if root.val == target and parent:
            delete(root, parent, d)
        elif root.val == target:
            if not root.left and not root.right:
                return None
            
        return root