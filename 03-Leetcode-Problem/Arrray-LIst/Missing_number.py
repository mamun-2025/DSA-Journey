


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



