# 1051. Height Checker

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = sum(h1 != h2 for h1, h2 in zip(heights, expected))
        return count