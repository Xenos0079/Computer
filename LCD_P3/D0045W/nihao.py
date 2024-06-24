# 995. Minimum Number of K Consecutive Bit Flips

from collections import deque
from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flipCount = 0
        q = deque()
        
        for i in range(n):
            if len(q) > 0 and i - q[0] >= k:
                q.popleft()
            
            if len(q) % 2 == nums[i]:
                if i + k > n:
                    return -1
                q.append(i)
                flipCount += 1
        
        return flipCount