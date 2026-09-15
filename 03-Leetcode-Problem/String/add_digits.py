

class Solution:
   def addDigits(self, num: int) -> int:

      while num >= 10:

         digit_sum = 0

         while num > 0:
            last_digit = num % 10
            digit_sum += last_digit
            num //= 10

         num = digit_sum

      return num



"""

 I repeatedly calculate the sum of the digits until the number becomes a single digit.
 I use the modulo operator to extract the last digit and integer division to remove it.
 I store the sum of the digits and use it as the new number for the next iteration.
 The time complexity is 0(log n) and 
 the space complexity is 0(1).

 """

