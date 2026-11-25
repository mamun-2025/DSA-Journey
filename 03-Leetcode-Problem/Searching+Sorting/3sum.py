
"""
nums = [-1, 0, 1, 2, -1, -4]

আমাদের এমন তিনটি সংখ্যা খুঁজে বের করতে হবে, যাদের যোগফল শূন্য হবে।
Mathematical Condition: a+b+c=0

উদাহরণ:
-1 + 0 + 1 = 0

আরেকটি:
-1 + -1 + 2 = 0

তাই আমাদের Output:
[[-1, -1, 2], [-1, 0, 1]]

"""

# Leetcode Problem: 15. 3Sum
# Approach 1 — Simple Approach (Brute Force)
class Solution:
   def threeSum(self, nums: list[int]) -> list[list[int]]:

      result = set()
      n = len(nums)

      for i in range(n):
         for j in range(i + 1, n):
            for k in range(j + 1, n):
               if nums[i] + nums[j] + nums[k] == 0:
                  tripplet = tuple(sorted([
                     nums[i],
                     nums[j],
                     nums[k],
                  ]))

                  result.add(tripplet)

      return [list(t) for t in result]

"""
Complexity Analysis:

আমাদের তিনটি Nested Loop রয়েছে।
Time: O(n³)
Space: O(n) worst case

Time Complexity O(n³), কারণ তিনটি Loop চালানো হচ্ছে।

এটি ছোট Array-এর জন্য কাজ করলেও Constraint-এ n = 3000 দেওয়া আছে। 
তাই এই Approach অনেক বেশি Slow হবে।
"""


# Approach 2 — Interview Approach (Sorting + Two Pointers)
