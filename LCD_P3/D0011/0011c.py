
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode], parent = None) -> int:

        self.moves = 0  # Initialize the total number of moves

        # Depth-first search to calculate the number of moves
        def dfs(node):
            if not node:
                return 0
            left_excess = dfs(node.left)  # Calculate excess coins in the left subtree
            right_excess = dfs(node.right)  # Calculate excess coins in the right subtree
            self.moves += abs(left_excess) + abs(right_excess)  # Update the total number of moves
            return node.val + left_excess + right_excess - 1  # Return the excess coins at the current node

        dfs(root)  # Start the depth-first search from the root
        return self.moves  # Return the total number of moves