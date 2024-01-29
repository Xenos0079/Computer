class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        result = 0
        temp = x
        while temp > 0:
            result = result * 10 + temp % 10
            temp = temp // 10
        print(result)
        if result == x:
            return True
        return False
    

m = Solution()
m.isPalindrome(121)