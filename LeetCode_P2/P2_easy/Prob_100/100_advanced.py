class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
def SameTree(p, q):
    if p == q:
        return True
    try:
        p.val == q.val
        left = SameTree(p.left, q.left)
        right = SameTree(p.right, q.right)
        ans = left and right
        return ans 
    except:
        return False
'''
def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

print(False and False)