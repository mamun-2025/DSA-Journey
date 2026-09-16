
class Solution:
   def isHappy(self, n: int) -> bool:
      seen = set()

      while n != 1:
         if n in seen:
            return False 
         else:
            seen.add(n)

         total = 0 
         while n > 0:
            last_digit = n % 10
            total += last_digit ** 2
            n //= 10
         n = total 

      return True 


result = Solution()
print(result.isHappy(19))

