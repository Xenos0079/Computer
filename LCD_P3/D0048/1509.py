# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
# try not to job day0

from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        a = nums[-1] - nums[3]
        b = nums[-2] - nums[2]
        c = nums[-3] - nums[1]
        d = nums[-4] - nums[0]

        return min(a,b,c,d)