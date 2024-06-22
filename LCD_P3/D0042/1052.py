# 1052. Grumpy Bookstore Owner

from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        # Calculate the initially satisfied customers
        satisfied_customers = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        # Calculate the potential gain if the technique is applied in the first "minutes" window
        additional_satisfied = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
        
        max_additional_satisfied = additional_satisfied
        
        # Use sliding window to find the maximal additional satisfied customers
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        return satisfied_customers + max_additional_satisfied