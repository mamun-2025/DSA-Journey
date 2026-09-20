

# While Loop
class Solution:
   def plusOne(self, digits: list[int]) ->list[int]:

      right = len(digits) - 1

      while right >= 0:
         if digits[right] < 9:
            digits[right] += 1
            return digits

         digits[right] = 0
         right -= 1

      digits.insert(0, 1)
      return digits


# For Loop
class Solution:
   def plusOne(self, digits: list[int]) ->list[int]:
      for i in range(len(digits) - 1, -1, -1):

         if digits[i] < 9:
            digits[i] += 1
            return digits

         digits[i] = 0

      digits.insert(0, 1)
      return digits

"""
I traverse the digits from right to left 
because the plus-one operation starts from the least significant digit.
If the current digit is less than 9, I increment it and return it.
If it is 9, I set it to 0 and continue to the left because of the carry.
If all digits are 9, I insert 1 at the beginning.

"""

        