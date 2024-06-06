# 1002. Find Common Characters

from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """ 
        不可能把每个word都建一个hash map。
        这题关键在于，result中其实只要确定char的最小次数

        """
        if len(words) == 1:
            return words[0]

        result = []
        chars = set(words[0])
        
        for char in chars:
            frequency = min([word.count(char) for word in words])
            result += frequency * [char]

        return result