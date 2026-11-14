


# Leetcode Problem:  
# Approach 1 — Linear Search (Brute Force)

nums = [10, 20, 30, 40, 50]
target = 30


class Solution:
   def linearSearch(self, nums, target):

      for i in range(len(nums)):

         if nums[i] == target:
            return i 

      return -1

   
   
# Approach 2 — Binary Search (Optimized)
class Solution:
   def binarySearch(self, nums: list[int], target: int) -> int:
      left = 0
      right = len(nums) - 1 

      while left <= right:
         mid = (left + right) // 2

         if nums[mid] == target:
            return mid 

         elif nums[mid] < target:
            left = mid + 1 

         else: 
            right = mid - 1

      return -1 



