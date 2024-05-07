# 459. Repeated Substring Pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # If concatenated and removed first and last chars
        # Even then we can find s
        # It is recreatable
        # Space: O(n)
        # Time:  O(n)
        
        return s in (s + s)[1: -1]