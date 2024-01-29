def is_prime(num):
   if num <= 1:
      return False
   for i in range(2, num):
      if num % i == 0:
         return False
   return True
def solve(num):
   if not is_prime(num):
      return False
   reverse_num = 0
   while num != 0:
      d = num % 10
      reverse_num = reverse_num * 10 + d
      num = int(num / 10)
   return is_prime(reverse_num)
n = 97
print (solve(n))