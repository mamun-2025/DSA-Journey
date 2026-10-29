

# Leetcode Problem: 136. Single Number
nums = [4, 1, 2, 1, 2]
# Nested Loop
class Solution:
   def singleNumber(self, nums: list[int]) -> int:
      for i in range(len(nums)):
         count = 0

         for j in range(len(nums)):
            if nums[i] == nums[j]:
               count += 1

            if count == 1:
               return nums[i]

# Complexity
# Time Complexity: \(O(n^2)\), কারণ প্রতিটি number-এর জন্য পুরো list scan করা হচ্ছে।
# Extra Space Complexity: \(O(1)\), কারণ কয়েকটি variable ব্যবহার হচ্ছে।

            
# Bit Manipulation (XOR)
nums = [2, 1, 2]
class Solution:
   def singleNumber(self, nums: list[int]) -> int:
      result = 0

      for num in nums:
         result = result ^ num 

      return result 


# Complexity	
# Time: O(n) প্রতিটি number একবার process হয়
# Space: O(1)	শুধু result-এর মতো constant সংখ্যক variable ব্যবহার হয়

"""
I use the XOR bitwise operator to solve this problem.
XOR of a number with itself is zero, and XOR of any number with zero is the number itself.
Since every number appears twice except one, all duplicate numbers cancel out.
The remaining result is the single number.
I iterate through the array once, 
so the time complexity is O(n) and the extra space complexity is O(1).

"""