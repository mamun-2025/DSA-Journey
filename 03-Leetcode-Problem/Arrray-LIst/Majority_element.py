

nums = [2, 2, 1, 1, 1, 2, 2]
# Leetcode Problem: 169. Majority Element
class Solution:
   def majorityElement(self, nums: list[int]) -> int:
      counts = {}
      n = len(nums)

      for num in nums:
         counts[num] = counts.get(num, 0) + 1 

         if counts[num] > n // 2:
            return num 


# Complexity Analysis
# Time Complexity: O(n) — প্রতিটি element একবার করে process করি।
# Space Complexity: O(n) — worst case-এ dictionary-তে সব সংখ্যাই আলাদা হলে (n) টি entry থাকতে পারে।



# Boyer-moore voting algorithm
class Solution:
   def majorityElement(self, nums: list[int]) -> int:
      candidate = None
      count = 0

      for num in nums:
         if count == 0:
            candidate = num 

         if num == candidate:
            count += 1
         else:
            count -= 1

      return candidate

# Complexity Analysis
# Time Complexity: O(n) — array একবার scan করি।
# Auxiliary Space: O(1) — শুধু candidate ও count-এর মতো কয়েকটি variable রাখি।

"""
First, I can use a hash map to count the frequency of each element.
This takes O(n) time and O(n) extra space.
To optimize space, I can use the Boyer-Moore Voting Algorithm, 
which maintains a candidate and a counter.
Since a majority element is guaranteed to exist, the final candidate is the answer.
The optimized solution takes O(n) time and O(1) extra space.

"""