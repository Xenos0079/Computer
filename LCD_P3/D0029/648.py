# 648. Replace Words

from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        sentence_words = sentence.split()
        
        def find_root(word):
            for i in range(1, len(word)):
                if word[:i] in roots:
                    return word[:i]
            return word
        
        replaced_sentence = [find_root(word) for word in sentence_words]
        
        return " ".join(replaced_sentence)