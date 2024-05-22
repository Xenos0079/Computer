# Devv

# 131. Palindrome Partitioning

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path, partitions):
            if start == len(s):
                partitions.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path, partitions)
                    path.pop()
        
        partitions = []
        backtrack(0, [], partitions)
        return partitions