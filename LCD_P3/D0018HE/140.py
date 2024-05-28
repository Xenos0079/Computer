from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        def backtrack(start, path):
            if start == len(s):
                result.append(' '.join(path))
                return

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet:
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result