# sample
class Solution:
    def removeElement(self, nums, val: int) -> int:
        x , i, got = len(nums) - 1 , len(nums) - 1, 0
        while i >= 0:
            if nums[i] == val:
                #print(i)
                nums.pop(i)
                #print(nums)
                got += 1
            i -= 1
        return x - got
nums = [3,2,2,3] 
x = Solution()
x.removeElement(nums , 3)
print(nums)
        