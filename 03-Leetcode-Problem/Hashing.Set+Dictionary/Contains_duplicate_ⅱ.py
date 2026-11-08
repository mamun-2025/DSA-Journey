

# তোমাকে একটি Integer List এবং একটি সংখ্যা k দেওয়া হবে।

# তোমাকে পরীক্ষা করতে হবে:
# - একই Value কি একাধিকবার আছে?
# - থাকলে তাদের Index-এর Distance কি k-এর সমান অথবা ছোট?
# দুটি শর্তই পূরণ হলে True, অন্যথায় False।

# 1. Brute Force Approach — Nested Loop
# Leetcode Problem: 219 
nums = [1, 2, 3, 1]
k = 3

def containsNearbyDuplicate(nums, k):
   for i in range(len(nums)):
      for j in range(i+1, len(nums)):

         if nums[i] == nums[j] and abs[i-j] <= k:
            return True

   return False

# Complexity
# - Time Complexity: O(n²) — Nested Loop-এর কারণে।
# - Space Complexity: O(1) — অতিরিক্ত কোনো Data Structure ব্যবহার করছি না।
# সমস্যা: বড় Array হলে অনেক বেশি তুলনা করতে হবে।

# আমরা এটাকে O(n) করতে চাই।




# 2. Optimized Approach — Dictionary + Index Mapping
# Hash Set + Siliding Window
nums = [1, 2, 3, 1]
k = 3

class Solution:
   def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
      last_seen = {}

      for i, num in enumerate(nums):

         if num in last_seen:
            return True

         last_seen.add(num)

         if i >= k:
            last_seen.remove(num[i-k])

      return False


"""
Complexity Analysis
ধরি, Array-এর Length n।

Time Complexity:
- Loop: O(n)
- Set membership: Average O(1)
- Set add: Average O(1)
- Set remove: Average O(1)
সুতরাং:
O(n)

Space Complexity: O(min(n,k+1))

Set-এ সর্বোচ্চ kটি Element-এর মতো সংরক্ষণ প্রয়োজন হতে পারে (Window-এর সীমার কারণে)।


Interview:
I use a Set to maintain a sliding window of the most recent elements.
For each element, I first check whether it already exists in the Set.
If it exists, I return True because a duplicate is found within distance k.
Otherwise, I add the current element to the Set.
If the current index is greater than or equal to k, I remove the element that is outside the allowed window.
If no nearby duplicate is found, I return False.
Time Complexity: O(n) average.
Space Complexity: O(min(n, k + 1)).

"""


