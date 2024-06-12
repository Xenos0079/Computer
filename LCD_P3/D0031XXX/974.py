# 974. Subarray Sums Divisible by K

from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}  # 

        for num in nums:
            prefix_sum += num
            modulus = prefix_sum % k
            count += prefix_sum_count.get(modulus, 0)  # 
            prefix_sum_count[modulus] = prefix_sum_count.get(modulus, 0) + 1  # 
            
        return count