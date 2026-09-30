
# OOP 
class Solution:
   def thirdMax(self, nums: list[int]) -> int:
      unique_nums = sorted(set(nums), reverse=True)

      if len(unique_nums) >= 3:
         return unique_nums[2]

      else:
         return unique_nums[0]


solution = Solution()

result = solution.thirdMax([2, 2, 1, 3])
print(result)


class Solution:
   def thirdMax(self, nums: list[int])-> int:
      first = None 
      second = None 
      thrid = None 

      for num in nums:

         if num == first or num == second or num == thrid:
            continue

         if first is None or num > first:
            third = second 
            second = first
            first = num 

         elif second is None or num > second:
            third = second
            second = num 

         elif third is None or num > third:
            third = num 

      if third is None:
         return first

      return third 


"""
I maintain the three largest distinct values while traversing the array once.
I skip duplicates, and whenever I find a larger value, 
I shift the existing values down. 
This allows me to solve the problem in 0(n) time and 
0(1) extra space without sorting.

"""
