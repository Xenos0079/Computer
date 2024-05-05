# 575. Distribute Candies

class Solution:
    def distributeCandies(self, candyType):
        return min(len(candyType) // 2, len(list(candyType)))