

# Leetcode Problem: 1. Two Sum
# 1. Brute Force Approach — Nested Loop
# প্রতিটি Number-এর সঙ্গে পরবর্তী Number যোগ করে দেখব।
nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):

   for i in range(len(nums)):

      for j in range(i+1, len(nums)):

         if nums[i] + nums[j] == target:
            return [i, j]


# Complexity
# - Time Complexity: O(n²) — Nested Loop।
# - Auxiliary Space Complexity: O(1) — অতিরিক্ত Data Structure নেই।



# 2. Optimized Approach — HashMap + Complement
nums = [2, 7, 11, 15]
target = 9


class Solution:
   def twoSum(self, nums: list[int], target: int) -> list[int]:

      seen = {}

      for i, num in enumerate(nums):

         needed = target - num 

         if needed in seen:
            return [seen[needed], i]

         seen[num] = i 

      return []

   
"""
Complexity:
Time Complexity — Average: O(n)
Array একবার Traverse করি। Dictionary-এর Lookup এবং Insert Average O(1)।

Auxiliary Space Complexity: O(n)
Worst case-এ Dictionary-তে প্রায় সব Number Store হতে পারে।

Interview:
First, I create an empty dictionary called seen to store numbers and their indices. 
Then, I iterate through the array using enumerate(). 
For each number, I calculate its complement by subtracting the current number from the target. 
I check whether the complement already exists in the dictionary. 
If it exists, I return the stored index and the current index. 
Otherwise, I store the current number and its index in the dictionary. 
This approach takes O(n) average time and O(n) auxiliary space.


Negative Number ও Zero:
nums = [-3, 4, 3, 90]target = 0

i	   num	      Complement	Dictionary Before Check	      Action
0	   -3          	3	      {}	Store                      -3:0
1	   4	            -4	      {-3:0}	                     Store 4:1
2	   3	            -3	      {-3:0, 4:1}	                  Return [0,2]

কারণ:
-3+3=0

Output:
[0, 2]

HashMap Approach Positive, Negative এবং Zero—সব Integer-এর ক্ষেত্রেই কাজ করে।
"""

