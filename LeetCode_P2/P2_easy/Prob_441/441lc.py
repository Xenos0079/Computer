# math approach
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        def f(x):
            return x * (x + 1) / 2
        t = int((math.sqrt(8 * n + 1) - 1) / 2)
        return t