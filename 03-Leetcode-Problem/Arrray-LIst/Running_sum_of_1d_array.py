

class Solution:
   def runningSum(self, nums: list[int])-> list[int]:
      total = 0
      result = []

      for num in nums:
         total += num 
         result.append(total)

      return result


numbers = [5, 10, 15, 20]

solution = Solution()
result = solution.runningSum(numbers)
print("Running Sum: ", result)




   



      