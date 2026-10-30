

# Leetcode Problem: 977. Squares of a Sorted Array
class Solution:
   def sortSquares(self, nums: list[int]) -> list[int]:
      squares = []

      for num in nums:
         squares.append(num * num)

      squares.sort()

      return squares

"""
Complexity
ধরি, array-তে n টি element আছে।
- প্রতিটি element square করতে O(n) time।
- Sorting করতে O(n log n) time।
সুতরাং overall time complexity:
O(n) + O(n log n) = O(n log n)

Auxiliary space হলো O(n), কারণ আমরা squares নামে নতুন list তৈরি করেছি। 
Python-এর sorting implementation-ও অতিরিক্ত space ব্যবহার করতে পারে।

"""

nums = [-4, -1, 0, 3, 10]
# Two Pointers (Optimal Solution)
class Solution:
   def sortSquares(self, nums: list[int]) -> list[int]:
      n = len(nums)
      result = [0] * n 

      left = 0
      right = n - 1
      position = n - 1

      while left <= right:
         left_square = nums[left] * nums[left]
         right_square = nums[right] * nums[right]

         if left_square > right_square:
            result[position] = left_square
            left += 1
         else: 
            result[position] = right_square
            right -= 1

         position -= 1

      return result


# Time Complexity: O(n)
# Auxiliary Space Complexity: O(n), কারণ result নামে নতুন array তৈরি করছি।
# এখানে(O(n) auxiliary space optimal time complexity-এর অংশ নয়; result array-তেই n টি element রাখতে হচ্ছে।

"""
We use two pointers, left and right,
to compare the squares of the elements at both ends of the sorted array.
We place the larger square at the end of the result and move the corresponding pointer inward.
We repeat this process until all elements are processed.
Time complexity: O(n)
Space complexity: O(n)

"""



