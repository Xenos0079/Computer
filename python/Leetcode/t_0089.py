class Solution:
    def grayCode(self, n: int):
        # Inspired by ChatOS and write by my self, low efficiency
        if n == 1:
            return [0,1]
        if n >= 1:
            x = self.grayCode(n - 1)
            for _ in range(len(x)):
                x[_] = str(bin(x[_])[2:])
            for i in range(len(x)):
                while len(x[i]) < n-1:
                    x[i] = '0' + x[i]
            zero, one = x, x[::-1]
            for _ in range(len(x)):
                zero[_] = '0' + zero[_]
                one[_] = '1' + one[_]
            print('zero: ', zero, ', one: ', one)
            coll = zero + one
            print('coll: ', coll)
            for _ in range(len(coll)):
                coll[_] = int(coll[_], 2)
            print(coll , 'finish')
        return coll

Quest = Solution()
Quest.grayCode(3)
'''
#by ChatOS, high efficiency
class Solution:
    def grayCode(self, n: int):
        if n == 1:
            return [0, 1]
        x = self.grayCode(n - 1)
        res = x + [2 ** (n - 1) + i for i in reversed(x)]
        return res
'''