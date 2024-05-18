# 786. K-th Smallest Prime Fraction
from typing import List

class Solution:
	def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

		if len(arr) == 1 or len(arr) == 2:
			return arr

		col, ans = [], []
		refer = {}
		l, r, x = 0, 1, len(arr)

		while l < r and r < x:
			s, b = arr[l], arr[r]
			col.append(s/b)
			ans.append([s, b])
			refer[s/b] = [s, b]

			if r + 1 == x:
				l += 1
				r = l + 1
			else:
				r += 1

		col.sort()

		return refer[col[k - 1]]