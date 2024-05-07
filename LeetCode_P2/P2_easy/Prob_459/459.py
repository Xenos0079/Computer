# 459. Repeated Substring Pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        x = len(s)
        for i in range(1, int(x // 2) + 1):
            if x % i == 0:
                sub = s[:i]
                n = x // i 
            if sub * n == s:
                return True
        return False