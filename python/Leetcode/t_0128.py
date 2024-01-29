class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        length = []
        new = sorted(nums)
        print(new)
        count = 1
        for _ in range(1, len(nums)):
            if new[_] == new[_ - 1] + 1:
                count += 1
                print(count)
            else:
                length.append(count)
                count = 1
        length.append(count)
        return max(length)

question = Solution()
question.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
    