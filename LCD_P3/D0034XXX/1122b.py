# 1122. Relative Sort Array

from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map = {}
        for i in range(len(arr2)):
            hash_map[arr2[i]] = i
        
        for i in range (len(arr1)):
            if arr1[i] not in hash_map:
                hash_map[arr1[i]] = 1000 + arr1[i]
        arr1.sort(key = lambda x: hash_map[x])
        return arr1