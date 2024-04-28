# HAPPY NUMBER
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()  # end the loop when the number is going to repeat
        while n != 1 and n not in visited:
            visited.add(n)
            split = [int(_) for _ in str(n)]
            n = sum([num ** 2 for num in split])
        return n == 1

''' # Hash_Table solution in LC

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.squared(n)
        fast = self.squared(self.squared(n))

        while slow != fast and fast != 1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))
    
        return fast == 1
    
    def squared(self, n) -> int:
        result = 0
        while n > 0:
            last = n % 10
            result += last * last
            n = n // 10
        return result

'''