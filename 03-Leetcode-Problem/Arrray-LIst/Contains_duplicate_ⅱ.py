

nums = [1, 2, 3, 1]
k = 3

# Brute Force(Nested Loop)
class Solution:
   def containsNearbyDuplicates(self, nums: list[int], k: int)-> bool:
      n = len(nums)

      for i in range(n):
         for j in range(i + 1, min(i + k + 1, n)):
            if nums[i] == nums[j]:
               return True

      return False

   
# Time Complexity: O(n X K)
# Space Complexity: O(1)


# Hash Set + Siliding Window
nums = [1, 2, 3, 1, 2, 3]
k = 2

class Solution:
   def containsNearbyDuplicate(self, nums: list[int], k: int)-> bool:
      seen = set()

      for i, num in enumerate(nums):
         if num in seen:
            return True

         seen.add(num)

         if i >= k:
            seen.remove(nums[i - k])

      return False


# Time Complexity: O(n)
# Space Complexity: O(min(n, k))

"""
I use a hash set to maintain a sliding window of the previous k elements.
For each number, I check whether it already exists in the set.
If it does, a nearby duplicate exists, so I return True.
Otherwise, I add the number and remove the element that is no longer within the allowed window.
If no nearby duplicate is found, I return False.
The average time complexity is 0(n), with O(min(n,k)) auxiliary space.

"""