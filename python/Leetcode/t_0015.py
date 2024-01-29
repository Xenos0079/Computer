class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
        # 如果当前数字(最小的数)大于0，则后面不可能再有三个数加起来等于0
            if nums[i] > 0:
                break
        # 如果当前数字和前一个数字相同，则会出现重复结果，应该跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
        # 双指针法
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                # 跳过重复的数字
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
        #  Copied from ChatOS

nums = [1,2,-2,-1]
what = Solution()
print(what.threeSum(nums))