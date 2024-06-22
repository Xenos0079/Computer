# 1248. Count Number of Nice Subarrays

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            result = 0
            left, right = 0, 0
            count = 0
            while right < len(nums):
                if nums[right] % 2 != 0:
                    count += 1
                while count > k:
                    if nums[left] % 2 != 0:
                        count -= 1
                    left += 1
                result += right - left + 1
                right += 1
            return result
        
        return atMostK(nums, k) - atMostK(nums, k - 1)