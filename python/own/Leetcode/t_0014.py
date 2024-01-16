class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        code = 0
        common = ''
        shortest = strs[0]
        for item in strs:
            if len(item) < len(shortest):
                shortest = item
        print(shortest)
        while code <= len(shortest) - 1:
            for string in strs:
                if string[code] != shortest[code]:
                    return shortest[:code]
                elif string == strs[-1]:
                    common += string[code]
                    code += 1
                    print(code)
        return common

strs = ["flower","flower","flower","flower"]
question = Solution()
print(question.longestCommonPrefix(strs))