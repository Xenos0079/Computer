class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        part = (s.split())[-1]
        return len(part)
        '''
        s = s.rstrip()
        count = 0
        for pos , val in enumerate(s[::-1]):
            if val == ' ':
                return count
            else:
                count += 1
                if pos == len(s) - 1:
                    return count
        '''