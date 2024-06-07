# 846. Hand of Straights
'''
To solve this problem, we can follow these steps:

Check if the total number of cards is divisible by the groupSize. If it's not divisible, return False because it's impossible to form groups of size groupSize with the given cards.
Create a dictionary to store the count of each card value in the hand list.
Sort the hand list.
Iterate through the sorted hand list:
For each card value, check if it's available to form a group.
If the card value is available, reduce the count of that card and check the next consecutive cards to form a group of size groupSize.
If it's not possible to form a group, return False.
If all groups are successfully formed, return True.
Here is the Python code implementing the above steps:
'''

from collections import defaultdict
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = defaultdict(int)
        for card in hand:
            count[card] += 1
        
        hand.sort()
        
        for card in hand:
            if count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] == 0:
                        return False
                    count[card + i] -= 1
        
        return True