# Assign cookies
# two pointers
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans, pg, ps = 0, 0, 0
        g.sort()
        s.sort()
        while pg <= len(g) - 1 and ps <= len(s) - 1:
            if g[pg] <= s[ps]:
                ans += 1
                pg += 1
                ps += 1
            else:
                ps += 1
        return ans