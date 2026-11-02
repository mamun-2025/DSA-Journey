


# Leetocode Problem: 349. Intersection of Two Arrays
# Using set
class Solution:
   def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
      set1 = set(nums1)
      set2 = set(nums2)

      result = []

      for num in set1:
         if num in set2:
            result.append(num)

      return result 

# Time: O(n + m)
# Space: O(n + m)


# Sorting + Two Pointers
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

class Solution:
   def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
      arr1 = sorted(nums1)
      arr2 = sorted(nums2)

      result = []

      left = 0
      right = 0

      while left < len(arr1) and right < len(arr2):

         if arr1[left] == arr2[right]:

            if not result or result[-1] != arr1[left]:
               result.append(arr1[left])

            left += 1
            right += 1

         elif arr1[left] < arr2[right]:
            left += 1

         else:
            right += 1

      return result


"""
4. Interview:
First, sort both arrays. Use two pointers to compare their elements.
If both elements are equal, add the element to the result if it is not already present.
Otherwise, move the pointer pointing to the smaller element.
Time Complexity: O(n log n + m log m)
Space Complexity: O(min(n, m))


5. Complexity Analysis
Operation	         Complexity
Sorting first array	O(n log n)
Sorting second array	O(m log m)
Two Pointers	      O(n+m)
Overall	            O(n log n+m log m)

Auxiliary space: sorted copies এবং result-এর জন্য O(n+m)।

6. তোমার HashMap approach বনাম Two Pointers
বিষয়	HashMap	Two Pointers
Sorting প্রয়োজন	না	হ্যাঁ
Duplicate handling	Frequency count	Both pointers move
Average time	      O(n+m)	         O(nl og n+m log m)
Extra space	         O(n+m)	         O(n+m)
Main concept	      Dictionary	      Sorting + Two Pointers

"""