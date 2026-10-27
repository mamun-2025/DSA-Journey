

# LeetCode Problem: 905 
# Extra Array ব্যবহার করে
class Solution:
   def sortArrayByParity(self, nums: list[int]) -> list[int]:
      even = []
      odd = []

      for num in nums:
         if num % 2 == 0:
            even.append(num)
         else:
            odd.append(num)

      return even + odd 

# Complexity
# Time Complexity: \(O(n)\) — প্রতিটি সংখ্যা একবার পরীক্ষা করা হয়।
# Space Complexity: \(O(n)\) — অতিরিক্ত list-এ সংখ্যাগুলো রাখা হয়।



# Two Pointers 
class Soution:
   def sortArrayByParity(self, nums: list[int]) -> list[int]:
      left = 0
      right = len(nums) - 1

      while left < right:
         if nums[left] % 2 == 0:
            left += 1
         elif nums[right] % 2 != 0:
            right -= 1
         else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

      return nums 


# Complexity
# Time Complexity: \(O(n)\) — সর্বোচ্চ linear সংখ্যক pointer movement ও swap হয়।
# Auxiliary Space Complexity: \(O(1)\) — নতুন array তৈরি করছি না; মূল array-তেই পরিবর্তন করছি।

"""
I use two pointers, one starting from the left and one from the right.
If the left element is even, I move the left pointer forward.
If the right element is odd, I move the right pointer backward.
Otherwise, I swap the misplaced odd and even elements.
This gives an O(n) time solution with O(1) extra space.

"""