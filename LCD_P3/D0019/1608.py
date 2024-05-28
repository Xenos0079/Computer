# 1608. Special Array With X Elements Greater Than or Equal X

from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort()

        if nums[0] >= l:
            return l

        for i in range(1, l):
            if nums[-i - 1] < i and nums[-i] >= i:
                return i
                
        return -1