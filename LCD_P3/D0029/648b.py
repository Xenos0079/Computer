# 648. Replace Words

from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            node = trie
            for letter in word:
                if letter in node:
                    node = node[letter]
                else:
                    new_node = {}
                    node[letter] = new_node
                    node = new_node
            else:
                node["is_word"] = True

        words = []
        for word in sentence.split(" "):
            node = trie
            for idx, letter in enumerate(word):
                if letter in node:
                    node = node[letter]
                    if node.get("is_word"):
                        words.append(word[:idx+1])
                        break
                else:
                    words.append(word)
                    break
            else:
                words.append(word)
        
        return " ".join(words)
        