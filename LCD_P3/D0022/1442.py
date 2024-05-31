# 1442. Count Triplets That Can Form Two Arrays of Equal XOR

from typing import List

class Solution: 
	def countTriplets(self, arr: List[int]) -> int: 
		count = 0 
		n = len(arr) 
		
		for i in range(n): 
			xor_sum = 0 
			for j in range(i, n): 
				xor_sum ^= arr[j] 
				if xor_sum == 0 and j > i: 
					count += j - i

		return count