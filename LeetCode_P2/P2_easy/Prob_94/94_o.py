# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> int:
        # inspired by 
        # geeksforgeeks
        answer = []
        def record(root):
            if root:
                record(root.left)
                answer.append(root.val)
                record(root.right)
        record(root)
        return answer