

# Leetcode Problem: 27
# In-place Removal using pop()
class Solution:
   def removeElement(self, nums: list[int], val: int)-> int:
      i = 0

      while i < len(nums):
         if nums[i] == val:
            nums.pop(i)
         else:
            i += 1 

      return len(nums)

# Complexity:
# Time: O(n^2) worst case — প্রতিবার pop(i) করলে পরের element-গুলো সরাতে বা shift করতে হতে পারে।
# Extra space: \(O(1)\) — অতিরিক্ত array তৈরি করছি না।



# Two Pointers
class Solution:
   def removeElement(self, nums: list[int], val: int) -> int:
      k = 0 

      for num in nums:
         if num != val:
            nums[k] = num 
            k += 1

      return k 


# Complexity
# Time Complexity: \(O(n)\) — প্রতিটি element একবার করে পরীক্ষা করা হয়।
# Extra Space Complexity: \(O(1)\) — অতিরিক্ত array বা অন্য কোনো data structure তৈরি করা হয় না।

"""
I use a write pointer k, initialy set to zero.
I iterate through the array and copy each element,
that is not equal to val to position k.
Then I increment k. After processing all elements, 
k represents the number of remaining elements.
The algorithm runs 0(n) time and uses 0(1) extra space.

"""
