

# Python-এ Set-এর Intersection বের করার Built-in Operation-ও আছে।
class Solution:
   def intersection(self, nums1: list[int], nums2: list[int])-> list[int]:
      return list(set(nums1) & set(nums2))

nums1= [1, 2, 2, 1]
nums2 = [2, 2]
solution = Solution()
print(solution.intersection(nums1, nums2))



# Set-based Solution
class Solution: 
   def intersection(self, nums1: list[int], nums2: list[int])-> list[int]:
      set1 = set(nums1)
      set2 = set(nums2)

      result = []

      for num in set1:
         if num in set2:
            result.append(num)

      return result

nums1= [1, 2, 2, 1]
nums2 = [1, 2]
solution = Solution()
print(solution.intersection(nums1, nums2))


