# 2486. Append Characters to String to Make Subsequence

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_, t_ = 0, 0

        while s_ < len(s) and t_ < len(t):
            if s[s_] == t[t_]:
                t_ += 1
            s_ += 1

        return len(t) - t_