# 506. Relative Ranks
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        refer = {}
        ans = [None] * len(score)
        col = sorted(score, reverse = True)

        for rank, credit in enumerate(col, start = 1):
            refer[credit] = rank

        for pos, credit in enumerate(score):
            if refer[credit] == 1:
                ans[pos] = "Gold Medal"
            elif refer[credit] == 2:
                ans[pos] = "Silver Medal"
            elif refer[credit] == 3:
                ans[pos] = "Bronze Medal"
            else:
                ans[pos] = str(refer[credit])

        return ans