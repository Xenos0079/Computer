def backtrack(nums, curr_subset):
        subsets = []
        subsets.append(curr_subset[:])
        
        for i in range(len(nums)):
            curr_subset.append(nums[i])
            subsets.extend(backtrack(nums[i + 1 :], curr_subset))
            curr_subset.pop()        
        return subsets

print(backtrack([5, 1, 6], []))