# 945. Minimum Increment to Make Array Unique

from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        
        # Initialize the number of moves to 0
        moves = 0
        
        # Iterate through the sorted array
        for i in range(1, len(nums)):
            # If the current number is not greater than the previous number
            if nums[i] <= nums[i - 1]:
                # Calculate the increment needed to make it unique
                increment = nums[i - 1] - nums[i] + 1
                # Add the increment to the current number
                nums[i] += increment
                # Add the increment to the total moves
                moves += increment
        
        return moves