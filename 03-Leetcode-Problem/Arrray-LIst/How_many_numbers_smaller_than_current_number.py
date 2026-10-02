


class Solution:
   def samllerNumbersThanCurrent(self, nums: list[int])-> list[int]:

      result = []

      for current in nums:
         count = 0

         for num in nums:
            if num < current:
               count += 1

         result.append(count)

      return result

   
