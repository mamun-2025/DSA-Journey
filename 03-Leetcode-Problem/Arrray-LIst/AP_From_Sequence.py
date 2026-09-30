

class Solution:
   def canMakeArithmeticProgression(self, arr: list[int])-> bool:

      arr.sort()
      current_difference = arr[1] - arr[0]

      for i in range(2, len(arr)):
         if arr[i] - arr[i-1] != current_difference:
            return False

      return True


solution = Solution()

result = solution.canMakeArithmeticProgression([1, 4, 7, 10])

print(result)

"""
First, I sort the array.
Then calculate the difference between the first two elements.
After that, I compare every consecutive difference with the initial difference.
If any difference is different, I return false.
Otherwise, I return true.

"""