# 857. Minimum Cost to Hire K Workers
# From ChatOS

import sys
import heapq

sys.float_repr_format = '{:0.5f}'.format

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted((wage[i] / quality[i], quality[i]) for i in range(n))
        heap = []
        sum_quality = 0
        min_cost = float('inf')
    
        for ratio, q in workers:
            heapq.heappush(heap, -q)
            sum_quality += q
        
            if len(heap) > k:
                sum_quality += heapq.heappop(heap)
            
            if len(heap) == k:
                min_cost = min(min_cost, sum_quality * ratio)
    
        return min_cost