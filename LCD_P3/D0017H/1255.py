class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counts = [0] * 26
        for letter in letters:
            counts[ord(letter) - ord('a')] += 1

        def wordHelper(words, counts, score, index):
            if index > len(words) - 1:
                return 0

            excludedSum = wordHelper(words, counts[:], score, index + 1)

            includedSum = 0
            recursionCall = True
            wordScore = 0

            for c in words[index]:
                letterIndex = ord(c) - ord('a')
                counts[letterIndex] -= 1
                if counts[letterIndex] < 0:
                    recursionCall = False
                wordScore += score[letterIndex]

            if recursionCall:
                includedSum = wordScore + wordHelper(words, counts[:], score, index + 1)

            for c in words[index]:
                counts[ord(c) - ord('a')] += 1

            return max(excludedSum, includedSum)

        return wordHelper(words, counts, score, 0)