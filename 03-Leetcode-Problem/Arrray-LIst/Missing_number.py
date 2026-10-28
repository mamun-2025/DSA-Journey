


# Leetocode Problem: 268. Missing Number
class Solution:
   def missingNumber(self, nums: list[int]) -> int:
      n = len(nums)

      expected_sum = n * (n + 1) // 2
      actual_sum = sum(nums)

      return expected_sum - actual_sum

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
solution = Solution()
result = solution.missingNumber(nums)
print(result)

"""
0 থেকে n পর্যন্ত সব সংখ্যার যোগফল বের করা যায় একটি formula দিয়ে:
            s = n * (n + 1) // 2   |||| s = n(n+1)/2

তারপর array-এর সব element-এর যোগফল বাদ দিলেই missing number পাওয়া যাবে।
         Missing Number = Expected Sum - Actual Sum

Complexity Analysis
- Time Complexity: O(n), কারণ sum(nums) array একবার traverse করে।
- Auxiliary Space: O(1), কারণ আমরা কয়েকটি variable ব্যবহার করছি। sum() নতুন করে array তৈরি করে না।
এই approach সহজ এবং কার্যকর। তবে integer-এর range অনেক বড় হলে sum-এর overflow নিয়ে কিছু programming language-এ সতর্ক থাকতে হয়। 
Python-এর integer সাধারণত এই সমস্যায় overflow করে না।

"""



# XOR (Bit Manipulation)
nums = [3, 0, 1]
class Solution:
   def missing_number(self, nums: list[int]) -> int:
      n = len(nums)
      missing = n 

      for i, num in enumerate(nums):
         missing = missing ^ i ^ num 

      return missing
"""
মূল ধারণা
XOR হলো একটি bitwise operation। Python-এ এর symbol হলো ^।

XOR-এর তিনটি গুরুত্বপূর্ণ নিয়ম:
Expression	Result	কারণ
5 ^ 5	      0	      একই সংখ্যার XOR শূন্য
5 ^ 0	      5	      শূন্যের সঙ্গে XOR করলে সংখ্যা অপরিবর্তিত
5 ^ 3 ^ 5	3	      একই সংখ্যা দুবার থাকলে cancel হয়


DRY RUN:

i        num        missing ^ i ^ num              missing     
__       ____       _________________              _______
-        -                 -                          3     (n = len(nums) | missing = n)
0        3          3 ^ 0 ^ 3                         0      
1        0          0 ^ 1 ^ 0                         1
2        1          1 ^ 2 ^ 1                         2

missing = 2
output: 2


Complexity Analysis
Time Complexity: O(n) — array একবার traverse করি।
Auxiliary Space: O(1) — n, missing, i ও num-এর মতো কয়েকটি variable ব্যবহার করি।

"""
   