

class Solution:
   def containsDuplicate(self, nums: list[int])-> bool:
      seen = set()

      for x in nums:
         if x in seen:
            return True 

         seen.add(x)

      return False


class Solution:
   def containsDuplicate(self, nums: list[int])-> int:
      seen = set()
      duplicates = set()

      for x in nums:
         if x in seen:
            duplicates.add(x)
         else:
            seen.add(x)

      return duplicates


nums = [1, 2, 3, 2, 4, 3]

solution = Solution()
print(solution.containsDuplicate(nums))


