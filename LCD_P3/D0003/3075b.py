# 3075. Maximize Happiness of Selected Children


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        children = sorted(happiness, reverse=True)

        # Fast calc if no child hits zero happiness
        # Could do binary search to see if I can do half, quarter, etc this way
        if children[k-1] >= k-1:
            return sum(children[:k]) - ((0 + k-1) * k // 2)

        # Else slow way
        res = 0
        for i, h in enumerate(children[:k]):
            if h - i <= 0:
                break
            res += h - i

        return res