'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        collect = {}
        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]
        for pos in range(len(nums) - 2):
            if pos > 0 and nums[pos] == nums[pos - 1]:
                continue
            left , right = pos + 1 , len(nums) - 1
            while left < right:
                val = nums[pos] + nums[left] + nums[right]
                dis = val - target
                if dis == 0:
                    return target
                elif dis < 0:
                    left += 1
                elif dis > 0:
                    right -= 1
                if collect:
                    if abs(dis) <= collect[min(collect , key = collect.get)]:
                        collect[val] = abs(dis)
                else:
                    collect[val] = abs(dis)
        return min(collect , key = collect.get)
'''
 # above is my original code, which will cause Time Limit Exceeded in example 62/101
 # below is copied from ChatOS
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]
        for pos in range(len(nums) - 2):
            if pos > 0 and nums[pos] == nums[pos - 1]:
                continue
            left , right = pos + 1 , len(nums) - 1
            while left < right:
                val = nums[pos] + nums[left] + nums[right]
                dis = val - target
                if dis == 0:
                    return target
                elif dis < 0:
                    left += 1
                elif dis > 0:
                    right -= 1
                if abs(dis) < abs(closest_sum - target):
                    closest_sum = val
        return closest_sum

target = -100
nums = [1,1,1,0]
question = Solution()
question.threeSumClosest(nums , target)