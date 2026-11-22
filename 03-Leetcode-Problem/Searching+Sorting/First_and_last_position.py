
# Leetcode Problem: 34. Find First and Last Position of Element in Sorted Array
# আমাদের একটি Sorted Array দেওয়া আছে।
# আমাদের কাজ হলো target = 8 কত নম্বর Index থেকে শুরু হয়েছে এবং কোন Index-এ শেষ হয়েছে, তা বের করা।
# মনে রাখবে:
# - First Position = প্রথমবার target পাওয়া Index।
# - Last Position = শেষবার target পাওয়া Index।
# - Target না পাওয়া গেলে [-1, -1] return করতে হবে।

# Approach 1 — Simple Approach (Linear Search)
nums = [5, 7, 7, 8, 8, 10]
target = 8

class Solution:
   def searchRange(self, nums: list[int], target: int)-> list[int]:
      first = -1
      last = -1

      for i in range(len(nums)):

         if nums[i] == target:

            if first == -1:
               first = i 

            last = i 

      return [first, last]

# Time: O(n)
# Space: O(1)


# Approach 2 — Interview Approach (Binary Search)
class Solution:
   def searchRange(self, nums: list[int], target: int) -> list[int]:

      def findFirst():

         left = 0
         right = len(nums) - 1
         ans = -1

         while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
               ans = mid 
               right = mid - 1 

            elif nums[mid] < target:
               left = mid + 1 

            else:
               right = mid - 1 

         return ans 


      def findLast():
         left = 0
         right = len(nums) - 1
         ans = -1

         while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
               ans = mid 
               left = mid + 1

            elif nums[mid] < right:
               left = mid + 1

            else:
               right = mid - 1

         return ans 

      return [findFirst(), findLast()]

"""
6. Time & Space Complexity Analysis
আমাদের Interview Approach-এ দুটি Binary Search চলছে।

Operation	Time Complexity
First Position	O(log n)
Last Position	O(log n)
Total	O(log n)

কারণ:
O(log n) + O(log n)
Constant বাদ দিলে:
O(log n)

Interview:
Since the given array is sorted, I can use Binary Search to achieve O(log n) time complexity.
I will perform Binary Search twice.

First, I will find the first occurrence of the target.
Whenever I find the target, I will store its index and continue searching in the left half.

Second, I will find the last occurrence.
Whenever I find the target, I will store its index and continue searching in the right half.

Finally, I will return both positions as a list.

The overall time complexity is O(log n) and 
the auxiliary space complexity is O(1).

"""




         
