


# Brute Force(Nested loop)
class Solution:
   def containsDuplicate(self, nums: list[int]) -> bool:
      n = len(nums)

      for i in range(n):
         for j in range(i + 1, n):
            if nums[i] == nums[j]:
               return True

      return False

# Time Complexity: 0(n^2)
# Space complexity: 0(1)


# Hash Set(Optimal Practical Approach)
class Solution:
   def containsDuplicate(self, nums: list[int])-> bool:
      seen = set()

      for num in nums:
         if num in seen:
            return True

         seen.add(num)

      return False

# Time Complexity: O(n)
# Space Complexity: O(n)

"""
I use a hash set to store the elements I have already visited.
For each number, I check whether it exists in the set.
If it does, I return True.
Otherwise, I add it to the set.
If I finish the iteration without finding a duplicate, I return False.
The average time complexity is O(n) and extra space complexity is O(n).

"""
