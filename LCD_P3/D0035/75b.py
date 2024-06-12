# 75. Sort Colors

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointers for the next positions of 0 and 2
        p0, curr, p2 = 0, 0, len(nums) - 1
        
        while curr <= p2:
            if nums[curr] == 0:
                # Swap the current element with the element at p0
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                # Swap the current element with the element at p2
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1

# 示例用法
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)  # 输出: [0, 0, 1, 1, 2, 2]
