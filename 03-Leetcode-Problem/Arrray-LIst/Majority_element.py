

nums = [2, 2, 1, 1, 1, 2, 2]
# Leetcode Problem: 169. Majority Element
class Solution:
   def majorityElement(self, nums: list[int]) -> int:
      counts = {}
      n = len(nums)

      for num in nums:
         counts[num] = counts.get(num, 0) + 1 

         if counts[num] > n // 2:
            return num 


# Complexity Analysis
# Time Complexity: O(n) — প্রতিটি element একবার করে process করি।
# Space Complexity: O(n) — worst case-এ dictionary-তে সব সংখ্যাই আলাদা হলে (n) টি entry থাকতে পারে।



# 