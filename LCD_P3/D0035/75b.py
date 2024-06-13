# 75. Sort Colors

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointers for the next positions of 0 and 2
        p0, curr, p2 = 0, 0, len(nums) - 1
        
        while curr <= p2:
            if nums[curr] == 0:
                # Swap the current element with the element at p0
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                # Swap the current element with the element at p2
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1

# 示例用法
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)  # 输出: [0, 0, 1, 1, 2, 2]

'''
说明：
三个指针：

p0 指向下一个应该放 0 的位置。
p2 指向下一个应该放 2 的位置。
curr 当前处理的元素。
遍历数组：

如果 nums[curr] == 0, 则将其与 p0 指针交换，并移动 p0 和 curr。
如果 nums[curr] == 2, 则将其与 p2 指针交换，并移动 p2。
否则, curr 指针移动一步。
这种方法确保了所有 0 都在前面，所有 2 都在后面，所有 1 在中间，并且只需一次遍历即可完成排序。
'''