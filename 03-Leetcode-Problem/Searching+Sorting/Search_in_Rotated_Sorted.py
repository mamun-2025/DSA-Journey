

"""
আমরা জানি Target-এর Index খুঁজে বের করতে হবে।

তাহলে প্রতিটি Index পরীক্ষা করতে পারি:
- বর্তমান Element Target-এর সমান কি না?
- সমান হলে Index Return করব।
- না হলে পরবর্তী Index-এ যাব।
- সম্পূর্ণ Array পরীক্ষা করেও না পেলে -1 Return করব।

"""

# Approach 1 — Simple Approach (Linear Search)

nums = [0, 1, 2, 4, 5, 6, 7]
# Array Sorted, কিন্তু মাঝখান থেকে Rotate করা হয়েছে।
nums = [4, 5, 6, 7, 0, 1, 2]
# দেখো, Array-টি এখন দুটি Sorted Part-এ বিভক্ত হয়েছে।
# Left Sorted Part: [4,5,6,7]
# Right Sorted Part: [0,1,2]
# দুটি অংশ আলাদাভাবে Sorted, কিন্তু সম্পূর্ণ Array-টি আর সরাসরি Ascending Order-এ নেই।

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

class Solution:
   def search(self, nums: list[int], target: int) -> int:

      for i in range(len(nums)):
         
         if nums[i] == target:
            return i 

      return -1

"""
Complexity	Result
Time	O(n)
Space	O(1)

এটি সঠিকভাবে কাজ করলেও Problem-এর O(log n) Requirement পূরণ করে না।
"""


nums = [4, 5, 6, 7, 0, 1, 2]
# Approach 2 — Interview Approach (Modified Binary Search)
class Solution:
   def search(self, nums: list[int], target: int) -> int:

      left = 0
      right = len(nums) - 1

      while left <= right:

         mid = (left + right) // 2

         if nums[mid] == target:
            return mid 

         if nums[left] <= nums[mid]:

            # Target যদি Left Sorted Half-এর মধ্যে থাকে → Left দিকে Search করবে।
            # Target যদি Left Sorted Half-এর মধ্যে না থাকে → Right দিকে Search করবে।
            if nums[left] <= target < nums[mid]:

               right = mid - 1   

            else:
               left = mid + 1 

         else:

            # Target যদি Right Sorted Half-এর মধ্যে থাকে → Right দিকে Search করবে।
            # Target যদি Right Sorted Half-এর মধ্যে না থাকে → Left দিকে Search করবে।
            if nums[mid] < target <= nums[right]:

               left = mid + 1 

            else:
               right = mid - 1


"""
Time & Space Complexity
আমাদের Modified Binary Search প্রতিটি Iteration-এ Search Space প্রায় অর্ধেক করে দেয়।

n - n/2 - n/4 - n/8- n/16

সুতরাং:
Complexity	Result	Explanation
Best Case	O(1)	প্রথম Mid-এই Target পাওয়া গেলে
Average Case	O(log n)	Search Space বারবার ছোট হয়
Worst Case	O(log n)	সর্বোচ্চ Logarithmic Search
Space	O(1)	শুধু কয়েকটি Variable ব্যবহার হচ্ছে
Final Complexity:
Time: O(log n)
Space: O(1)

Interview:
I will use a modified Binary Search approach.

First, I initialize two pointers, left and right, and calculate the middle index.

If the middle element equals the target, I return its index.
Otherwise, I check which half of the array is sorted.

If the left half is sorted, I check whether the target lies within its range.
If it does, I search the left half; otherwise, I search the right half.

If the right half is sorted, I perform the same range check and eliminate the irrelevant half.

I repeat this process until the target is found or the serach space becomes empty.

The time complexity is O(log n), and the space complexity is O(1).

"""                      
