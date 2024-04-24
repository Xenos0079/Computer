class Solution2:
    def majorityElement(self, nums) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]
    

import statistics
stdin = 0 # what is that?
f = open("user.out", 'w')
for line in stdin:
    l = sorted(map(int, line.rstrip()[1:-1].split(',')))
    print(l[len(l) // 2], file=f)
exit(0)

