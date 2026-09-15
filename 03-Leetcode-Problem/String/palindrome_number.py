

class Solution:
   def isPalindrome(self, x: int) -> bool:
      if x < 0:
         return False

      original = x 
      reverse_num = 0

      while x > 0:
         last_digit = x % 10
         reverse_num = reverse_num * 10 + last_digit 
         x //= 10

      return original == reverse_num 



"""

I first check if the number is negative.
If it is negative, I return false.
Then I saved the original number and reverse the digits using modulo and integer division.
Finally, I compare the original number with the reversed number.
If they are equal, I return true, otherwise false.
The number is a palindrome if it reads the same backward as forward.
So the time complexity is 0(log x), and the space complexity is 0(1).

"""

