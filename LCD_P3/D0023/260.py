# 260. Single Number III

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums

        x = set()

        for _ in nums:
            if _ not in x:
                x.add(_)
            else:
                x.remove(_)
        
        return x