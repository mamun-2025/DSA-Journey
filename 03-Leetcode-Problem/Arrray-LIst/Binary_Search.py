

class Solution:
   def search(self, nums: list[int], target: int)-> int:
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



numbers = [-1, 0, 3, 5, 9, 12]
solution = Solution()
result = solution.search(numbers, 9)
print(result)


"""
I use binary search on the sorted array.
I maintain left and right boundaries and calculate the middle index.
If the middle value equals the target, I return its index.
If it is smaller, I search the right half;
otherwise, I search the left half.
The gives 0(log n) time and 0(1) space.

"""