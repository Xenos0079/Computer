# 3075. Maximize Happiness of Selected Children
from typing import List

class Solution:
	def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
		col = sorted(happiness, reverse = True)
		count, ans = 0, 0
		
		for x in col:
			x -= count
			count += 1
			if x > 0 and count <= k:
				ans += x
				
		return ans