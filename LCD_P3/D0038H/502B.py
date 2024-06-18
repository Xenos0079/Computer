# 502. IPO

from heapq import heappush, heappop
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Combine the profits and capital into a list of tuples
        projects = list(zip(capital, profits))
        # Sort the projects based on the capital required
        projects.sort()
        
        max_heap = []
        idx = 0
        n = len(projects)
        
        for _ in range(k):
            # Push all projects that can be started with the current capital into the max-heap
            while idx < n and projects[idx][0] <= w:
                heappush(max_heap, -projects[idx][1])  # Use negative profit to simulate max-heap
                idx += 1
            
            # If there are no projects that can be started, break the loop
            if not max_heap:
                break
            
            # Select the project with the highest profit
            w += -heappop(max_heap)
        
        return w