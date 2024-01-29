from typing import List
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        for num in range(len(candidates)):
            if target % candidates[num] == 0:
                sub = []
                for i in range(target // candidates[num]):
                    sub.append(candidates[num])
                ans.append(sub)
            else:
                sub = []
                piece = target // candidates[num]
                left = target % candidates[num]
                while piece > 0:
                    if left in candidates:
                        for i in range(piece):
                            sub.append(candidates[num])
                        sub.append(left)
                        ans.append(sub)
                    else:
                        piece -= 1
                        left += num
        return ans

question = Solution()
print(question.combinationSum([2,3,6,7] , 7))
'''
# time limit succeeded
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return
            for i in range(start, len(candidates)):
                backtrack(i, path + [candidates[i]], target - candidates[i])

        ans = []
        candidates.sort()
        backtrack(0, [], target)
        return ans
''' 
# copied from Chat

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:                                  # O(N): for each candidate
            for i in range(c, target+1):                      # O(M): for each possible value <= target
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]
# copied from leetcode