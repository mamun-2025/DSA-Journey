

class Solution:
   def twoSum(self, nums: list[int], target: int)-> list[int]:
      seen = {}

      for index, current in enumerate(nums):
         needed = target - current

         if needed in seen:
            return [seen[needed], index]

         seen[current] = index




         

