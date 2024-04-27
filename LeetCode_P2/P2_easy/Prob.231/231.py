# find the input whether it is a power of two or not
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        ans = n / 2
        if not isinstance(ans, int) and not ans.is_integer():
            return False   
        else:
            return self.isPowerOfTwo(ans)

# Code in LC best:
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 2 != 0 or n == 0:
            return False
        
        return self.isPowerOfTwo(n / 2)

'''