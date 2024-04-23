# Majority element in a list


'''
### the first edition

class Solution:
    def majorityElement(self, nums) -> int:

        nums.sort()
        print('nums', nums)

        mid = int(len(nums)/2)
        print('mid', mid)

        if nums[0] == nums[mid]:
            print('0', nums[0])
            return nums[0]
        
        elif nums[-1] == nums[mid - 1]:
            print('-1', nums[-1])
            return nums[-1]
        
        else:
            print('failed')
            return None
'''

'''
### 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        nums.sort()
        le = len(nums)
        if le == 1:
            return nums[0]

        x = le / 2
        e = le // 2
        if e == 0:
            l = nums[x - 1], r = nums[x]
            if nums[0] == l:
                return l
            elif nums[-1] == r:
                return r
            else:
                return None
        else:
            m = nums[int(e)]
            if nums[0] == m or nums[-1] == m:
                return m
            else:
                return None
'''


#'''
class Solution:
    def majorityElement(self, nums) -> int:
        if not nums:
            return None
        x = len(nums)
        if x == 1:
            return nums[0]
        memo = {}
        for _ in nums:
            if _ not in memo:
                memo[_] = 1
            elif memo[_] >= x/2:
                print('a', _)
                return _
            else:
                memo[_] += 1
        print('what?')
#'''

q = Solution()

test = [3, 2, 3]

#print(q.majorityElement(test))

q.majorityElement(test)