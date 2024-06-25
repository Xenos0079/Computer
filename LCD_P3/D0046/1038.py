# 1038. Binary Search Tree to Greater Sum Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.greater_sum = 0
        self.reverse_inorder(root)
        return root
    
    def reverse_inorder(self, node):
        if not node:
            return
        
        # Traverse right subtree
        self.reverse_inorder(node.right)
        
        # Update node value
        node.val += self.greater_sum
        self.greater_sum = node.val
        
        # Traverse left subtree
        self.reverse_inorder(node.left)