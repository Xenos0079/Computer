# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums):
        coll = set(nums) ### very importent!!!
        ans = []
        for _ in range(1 , len(nums) + 1):
            if _ not in coll:
                ans.append(_)
        return ans
