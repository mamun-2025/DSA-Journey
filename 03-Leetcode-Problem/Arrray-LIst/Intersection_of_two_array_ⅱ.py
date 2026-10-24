

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