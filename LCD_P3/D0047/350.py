# 350. Intersection of Two Arrays II

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        pos = []
        l, r = 0, 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                pos.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] <= nums2[r]:
                l += 1
            else:
                r += 1

        return pos