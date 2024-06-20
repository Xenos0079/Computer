# 1482. Minimum Number of Days to Make m Bouquets
# 
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMakeBouquets(days):
            bouquets = 0
            flowers_in_bouquet = 0
            
            for bloom in bloomDay:
                if bloom <= days:
                    flowers_in_bouquet += 1
                    if flowers_in_bouquet == k:
                        bouquets += 1
                        flowers_in_bouquet = 0
                        if bouquets == m:
                            return True
                else:
                    flowers_in_bouquet = 0
            
            return bouquets >= m
        
        if m * k > len(bloomDay):
            return -1
        
        low, high = 1, max(bloomDay)
        
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(mid):
                high = mid
            else:
                low = mid + 1
        
        return low if canMakeBouquets(low) else -1
