# binary research
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            sum_mid = mid * (mid + 1) // 2
            if sum_mid == n:
                return mid
            elif sum_mid < n:
                left = mid + 1
            else:
                right = mid - 1
        return right
