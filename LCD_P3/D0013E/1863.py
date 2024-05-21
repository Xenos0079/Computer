# 1863. Sum of All Subset XOR Totals
# There is no D14 as D14's mission is finished by the subset program

from typing import List

class Solution:
    def backtrack(self, nums: List[int], curr_subset) -> list:
        subsets = []
        subsets.append(curr_subset[:])
        
        for i in range(len(nums)):
            curr_subset.append(nums[i])
            subsets.extend(self.backtrack(nums[i + 1 :], curr_subset))
            curr_subset.pop()        

        return subsets
    
    def xor_sum(self, target: List[int]) -> int:
        if not target:
            return 0
        elif len(target) == 1:
            return target[0]
        else:
            ans = 0
            for i in target:
                ans ^= i

            return ans

    def subsetXORSum(self, nums: List[int]) -> int:
        count = 0
        sub = self.backtrack(nums, [])
        for _ in sub:
            count += self.xor_sum(_)
        return count