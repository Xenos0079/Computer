# 1552. Magnetic Force Between Two Balls

from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Step 1: Sort the positions
        position.sort()
        
        # Step 2: Define the feasibility function
        def canPlaceBalls(min_force):
            count = 1  # Place the first ball in the first position
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            
            return False
        
        # Step 3: Initialize binary search bounds
        left, right = 1, position[-1] - position[0]
        
        # Step 4: Perform binary search
        while left < right:
            mid = (left + right + 1) // 2
            if canPlaceBalls(mid):
                left = mid  # Try for a larger minimum distance
            else:
                right = mid - 1  # Try for a smaller minimum distance
        
        return left
