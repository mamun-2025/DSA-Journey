

# LeetCode 35 — Search Insert Position

# nums = [1, 3, 5, 7]
# target = 5

# nums = [1,3,5,6], 
# target = 2


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

