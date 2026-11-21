

# LeetCode 35 — Search Insert Position
# Search Insert Position কী?
nums = [1, 3, 5, 7]
target = 5
# তোমাকে একটি Ascending Sorted Array এবং একটি Target Integer দেওয়া হবে।
# Target Array-তে থাকলে তার Index Return করবে।
# Target না থাকলে Sorted Order বজায় রেখে যে Index-এ Target Insert করতে হবে, সেটি Return করবে।
# Target থাকুক বা না থাকুক, আমাদের এমন একটি Position খুঁজতে হবে যেখানে Target বসালে Array Sorted থাকবে।

# 1. Simple approach 
def search_insert(nums, target):

   for i in range(len(nums)):

      if nums[i] >= target:
         return i 

   return len(nums)

print(search_insert([1, 3, 5, 7], 2))




# 2. Optimized Approach 
nums = [1,3,5,6], 
target = 2


class Solution:
   def searchInsert(self, nums:list[int], target:int) -> int:
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

      return left 


nums = [1,3,5,6]
target = 5

solution = Solution()
print(solution.searchInsert(nums, target))

