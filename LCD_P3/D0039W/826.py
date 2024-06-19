# 826. Most Profit Assigning Work

from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Pair each job's difficulty with its profit and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # Sort the workers by their ability
        worker.sort()
        
        max_profit = 0
        total_profit = 0
        i = 0
        
        # Iterate through each worker
        for ability in worker:
            # Update the max_profit for the current worker's ability
            while i < len(jobs) and jobs[i][0] <= ability:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            # Add the max_profit for the current worker to the total profit
            total_profit += max_profit
        
        return total_profit