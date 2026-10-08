

# 🟢 1. Write Pointer — In-place
class Solution:
   def moveZeroes(self, nums: list[int])-> None:

      write = 0

      for read in range(len(nums)):
         if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

      while write < len(nums):
         nums[write] = 0
         write += 1


arr = [0, 1, 0, 3, 12]
solution = Solution()
solution.moveZeroes(arr)
print(arr)
   


# 🟢 2. Swap-based Two Pointer
class Solution:
   def move_Zeros(self, arr: list[int])-> int:

      write = 0

      for read in range(len(arr)):
         if arr[read] != 0:
            arr[write], arr[read] = arr[read], arr[write]
            write += 1

      return arr 


arr = [0, 1, 0, 3, 12]
solution = Solution()
print(solution.move_Zeros(arr))




# 🔵 3. result = [] ব্যবহার করলে?
def moveZeros(arr):
   result = []

   for x in arr:
      if x != 0:
         result.append(x)

   while len(result) < len(arr):
      result.append(0)

   return result

arr = [0, 1, 0, 3, 12]
print(moveZeros(arr))
      



