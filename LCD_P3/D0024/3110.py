# 3110. Score of a String

class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for _ in range(0, len(s) - 1):
            ans += abs(ord(s[_]) - ord(s[_ + 1]))
        return ans