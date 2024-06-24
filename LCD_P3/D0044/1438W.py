# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()  # to store indices of elements in decreasing order of value
        min_deque = deque()  # to store indices of elements in increasing order of value
        n = len(nums)
        left = 0
        max_length = 0
        
        for right in range(n):
            # Update max_deque with current window
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Update min_deque with current window
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Adjust the left pointer to maintain the window condition
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Calculate the maximum length of valid subarray
            max_length = max(max_length, right - left + 1)
        
        return max_length
