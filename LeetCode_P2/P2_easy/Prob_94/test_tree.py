class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#count = 0

class Solution:
    count = 0
    def isSameTree(self, p, q) -> bool:

        self.count += 1
        print(self.count)

        if p == q:
            print('p and q')
            return True
        try:
            p.val == q.val
            print('p = q', p.val , " " ,q.val)
            left = self.isSameTree(p.left, q.left)
            print('left' , left)
            right = self.isSameTree(p.right, q.right)
            print('right' , right)

            ans = left and right
            print('ans:', ans)
            return left and right
        
        except:
            print('exp')
            print('p != q', p.val , " " ,q.val)
            return False


p = TreeNode()
p.val = 1
p.left, p.right = TreeNode(2), TreeNode(1)


q = TreeNode()
q.val = 1
q.left, q.right = TreeNode(1), TreeNode(2)


ans = Solution()
ans.isSameTree(p, q)