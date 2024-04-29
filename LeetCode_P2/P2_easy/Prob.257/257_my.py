# 257. Binary Tree Paths
class TreeNode: 
	def __init__(self, val=0, left=None, right=None): 
		self.val = val 
		self.left = left 
		self.right = right 
		
class Solution:
    def binaryTreePaths(self, root):
        ans = []
        if not root:
            return []
        self.find(str(root.val), root, ans)
        return ans
    
    def find(self, last, tar, ans):
        if not tar.left and not tar.right:
            ans.append(last)
            return
        if tar.left:
            self.find(last + '->' + str(tar.left.val), tar.left, ans)
        if tar.right:
            self.find(last + '->' + str(tar.right.val), tar.right, ans)