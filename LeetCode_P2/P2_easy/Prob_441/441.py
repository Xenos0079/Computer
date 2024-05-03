# Arranging Coins
# Recursion approach
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return self.fill(1, n)
    def fill(self, lev, rem):
        if lev <= rem:
            return self.fill(lev + 1, rem - lev)
        return lev - 1