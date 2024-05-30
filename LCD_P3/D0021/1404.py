# 1404. Number of Steps to Reduce a Number in Binary Representation to One

class Solution:
    def numSteps(self, s: str) -> int:
        # do not use int()
        # follow the comment's suggestion(Coollaitar)
        steps = 0
        carry = 0
        n = len(s) - 1
        for i in range(n, 0, -1):
            if int(s[i]) + carry == 1:
                carry = 1
                steps += 2
            else:
                steps += 1
        return steps + carry