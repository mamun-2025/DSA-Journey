


# Leetcode Problem: 217. Contains Duplicate
# Brute Force Approach:
nums = [1,2,3,4]
class Solution: 
   def containsDuplicate(self, nums: list[int]) -> int:
      for i in range(len(nums)):
         for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
               return True

      return False



# Set Optimization:
nums = [1,2,3,4]
class Solution:
   def containsDuplicate(self, nums: list[int]) -> int:
      seen = set()

      for num in nums:
         if num in seen:
            return True

         seen.add(num)

      return False
