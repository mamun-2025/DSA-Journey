
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
class Solution:
   def threeSum(self, nums: list[int]) -> list[list[int]]:

      nums.sort()
      result = []
      n = len(nums)

      for i in range(n-2):

         if i > 0 and nums[i] == nums[i-1]:
            continue

         left = i + 1
         right = n - 1

         while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
               result.append([
                  nums[i],
                  nums[left],
                  nums[right],
               ])

               left += 1
               right -= 1

               while left < right and nums[left] == nums[left - 1]:
                  left += 1

               while left < right and nums[right] == nums[right + 1]:
                  right -= 1

            elif total < 0:
               left += 1

            else:
               right -= 1

      return result


"""
এখানে দুটি কাজ হচ্ছে:
1. Sorting → O(n log n)
2. Outer Loop এবং Two Pointers → O(n²)

তাই: O(n log n) + O(n^2)
Final: O(n^2)

Space Complexity:
- Result বাদ দিলে Two Pointers-এর অতিরিক্ত Space O(1)।
- Python-এর sort()-এর নিজস্ব Temporary Space লাগতে পারে, Worst Case O(n)।
- Output List-এর Space আলাদাভাবে গণনা করতে হবে।
Approach	Time	Auxiliary Space
Brute Force	O(n³)	O(n²) worst case
Sorting + Two Pointers	O(n²)	O(1) for pointer logic, excluding sorting

Interview:
I will use a combination of Sorting and the Two Pointers technique.
First, I will sort the input array.
Then, I will iterate through the array and fix one element at a time.
For each fixed element, I will initialize two pointers one immediately 
after the current index and another at the end of the array.
I will calculate the sum of these three elements.
If the sum is zero, I will add the triplet to the result and move both pointers.
If the sum is less than zero, I will move the left pointer forward to increase the sum.
If the sum is greater than zero, I will move the right pointer backword to decrease the sum.
I will also skip duplicate values to avoid duplicate triplets.
The overall time complexity is O(n^2)

"""