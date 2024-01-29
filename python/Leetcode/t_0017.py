class Solution:
    def letterCombinations(self, digits: str):
        ref = {'2':['a','b','c'] , '3':['d','e','f'] , '4':['g','h','i'] , \
               '5':['j','k','l'] ,'6':['m','n','o'] ,'7':['p','q','r','s'] ,'8':['t','u','v'] ,'9':['w','x','y','z']}
        pos = 0
        answer = []
        while pos <= len(digits) - 1:
            if pos == 0:
                answer = ref[digits[pos]]
                pos += 1
            elif pos >= 0:
                next = ref[digits[pos]]
                answer = [x + y for x in answer for y in next] # the most important
                pos += 1
        return answer
# above from ChatOS and below is original
'''
class Solution:
    def letterCombinations(self, digits: str):
        ref = {'2':['a','b','c'] , '3':['d','e','f'] , '4':['g','h','i'] , '5':['j','k','l'] ,'6':['m','n','o'] ,'7':['p','q','r','s'] ,'8':['t','u','v'] ,'9':['w','x','y','z']}
        pos = 0
        answer = []
        while pos <= len(digits) - 1:
            if pos == 0:
                answer = ref[digits[pos]]
                pos += 1
            elif pos >= 0:
                step = len(ref[digits[pos]])
                answer *= step
                #answer.sort()
                next = ref[digits[pos]] * step
                next.sort()
                answer = [x + y for x , y in zip(answer , next)]
                pos += 1
        return answer
'''