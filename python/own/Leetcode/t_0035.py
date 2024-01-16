class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] >= target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary research again
        if nums[0] >= target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        elif nums[-1] == target:
            return len(nums)-1
        l, r = 0, len(nums)-1
        if nums[l] < target < nums[r] and len(nums) < 3:
            return 1
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        while nums[mid] < target < nums[r]:
            if r - mid == 1:
                return mid + 1
            elif nums[mid] == target:
                return mid
            else:
                l = mid
                mid = (l + r) // 2
        while nums[l] < target < nums[mid]:
            if mid - l == 1:
                return l + 1
            elif nums[mid] == target:
                return mid
            else:
                r = mid
                mid = (l + r) // 2
'''