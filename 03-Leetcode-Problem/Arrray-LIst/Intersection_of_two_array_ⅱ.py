

# LeetCode 350 — Intersection of Two Arrays II
# Problem: Dictionary/HashMap

# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]

class Solution:
   def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
      frquency = {}

      for num in nums1:
         frquency[num] = frquency.get(num, 0) + 1

      result = []

      for num in nums2:
         if frquency.get(num, 0) > 0:
            result.append(num)
            frquency[num] -= 1

      return result

"""
I use a hash map to count the frequency of each element in the first array.
Then I iterate through the second array. 
If an element has a positive remaining frequency, I add it to the result and decrement its count.
This preserves duplicates correctly and gives average 0(n+m) time comlplexity.
"""

# Two Pointers (Sorted Arrays)
# এবার আমরা Two Pointers ব্যবহার করব।
# শর্ত: এই পদ্ধতিতে দুটি Array-কে Sorted Order-এ থাকতে হবে। তাই সাধারণ Input-এর জন্য আগে Sort করব।
class Solution:
   def intersect(self, nums1: list[int], nums2: list[int])-> list[int]:
      arr1 = sorted(nums1)
      arr2 = sorted(nums2)

      result = []
      left = 0
      right = 0

      while left < len(arr1) and right < len(arr2):
         if arr1[left] == arr2[right]:
            result.append(arr1[left])
            left += 1
            right += 1

         elif arr1[left] < arr2[right]:
            left += 1

         else:
            right += 1


      return result

   

