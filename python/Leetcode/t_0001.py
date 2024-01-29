class Solution(object):

	def twoSum(self, nums, target):
		hash_table = {}
		for index , value in enumerate(nums):
			pair = target - value
			if pair in hash_table:
				return [hash_table[pair] , index]
			hash_table[value] = index
		return []