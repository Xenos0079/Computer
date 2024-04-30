# two number sum
# need to know that the input are string

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000) ###
        return str(int(num1) + int(num2))