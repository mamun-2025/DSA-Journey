

# Leetcode Problem: 88. Merge Sorted Array
# Extend and sort 
class Solution:
   def merge(self, nums1: list[int], m:int, nums2: list[int], n:int) -> None:
      for i in range(n):
         nums1[m + i] = nums2[i]

      nums1.sort()

# Complexity
# Time Complexity: O((m+n)\log(m+n) — sorting-এর জন্য।
# Auxiliary Space: Python-এর sorting implementation-এর অতিরিক্ত space লাগতে পারে; 
# তাই এটিকে strict O(1) space solution বলা ঠিক নয়।


# Threee Pointers (Optimal Solution)
class Solution:
   def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
      i = m - 1 
      j = n - 1
      k = m + n - 1 

      while i >= 0 and j >= 0:
         if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
         else:
            nums1[k] = nums2[j]
            j -= 1

         k -= 1

      while j >= 0:
         nums1[k] = nums2[j]
         j -= 1
         k -= 1


"""
Time Complexity: O(m+n)
প্রতিটি element সর্বোচ্চ একবার করে process করা হয়। তিনটি pointer শুধু বাম দিকে চলে; কোনো element-এর জন্য আবার শুরু থেকে loop চালানো হয় না।
তাই:
O(m+n)

Auxiliary Space Complexity: O(1)
আমরা শুধু i, j, k-এর মতো কয়েকটি variable ব্যবহার করেছি। কোনো অতিরিক্ত array তৈরি করিনি।
O(1)

এখানে auxiliary space বলতে input array বাদে algorithm-এর ব্যবহৃত অতিরিক্ত space বোঝানো হয়েছে।

"""

"""
We use three pointers: i for the last valid element of nums1, 
j for the last element of nums2, and k for the last position of the merged array.

We compare the elements at i and j.
We place the larger element at k and move the corresponding pointer backward.
We continue until one array is exhausted.
If elements remain in nums2, we copy them into nums1.
Time complexity: O(m+n)
Space Complexity: O(1)

Why do we merge from the end?
= We merge from the end to avoid overwriting the original elements of nums1.

Why is the second loop necessary?
= If nums2 still contains elements after the first loop, 
  we must copy them into nums1.Any remaining elements of nums1 are already in their correct positions.
  
"""