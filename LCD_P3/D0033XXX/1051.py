# 1051. Height Checker

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x = sorted(heights)
        c = 0
        
        for i in range(len(x)):
            if heights[i] != x[i]:
                c += 1
        
        return c