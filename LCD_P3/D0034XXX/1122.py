# 1122. Relative Sort Array

from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        coll = []
        
        for i in range(len(arr2)):
            while arr2[i] in arr1:
                coll.append(arr2[i])
                arr1.remove(arr2[i])
        
        arr1.sort()

        return coll + arr1