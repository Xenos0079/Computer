# 523. Continuous Subarray Sum

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            # Handling the case where k is 0
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False
        else:
            # Using a dictionary to store the remainder of cumulative sum % k
            remainder_map = {0: -1}
            cumulative_sum = 0
            for i in range(len(nums)):
                cumulative_sum += nums[i]
                if k != 0:
                    cumulative_sum %= k
                if cumulative_sum in remainder_map:
                    if i - remainder_map[cumulative_sum] > 1:
                        return True
                else:
                    remainder_map[cumulative_sum] = i
            return False

# Example usage
solution = Solution()
nums = [23, 2, 4, 6, 7]
k = 6
print(solution.checkSubarraySum(nums, k))  # Output: True