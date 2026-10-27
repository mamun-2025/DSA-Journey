

# Total Sum + Running Sum (Optimized)
class Solution:
   def pivotIndex(self, nums: list[int]) -> int:
      total_sum = sum(nums)
      left_sum = 0

      for i in range(len(nums)):
         right_sum = total_sum - left_sum - nums[i]

         if left_sum == right_sum:
            return i 

         left_sum += nums[i]

      return -1 


# Complexity Analysis
# Time Complexity: \(O(n)\) — sum(nums) একবার array ঘোরে, এরপর loop সর্বোচ্চ একবার array ঘোরে। তাই মোট সময় linear।
# Auxiliary Space: \(O(1)\) — শুধু কয়েকটি variable ব্যবহার করছি। sum(nums) নতুন করে array তৈরি করে না।

"""
I first calculate the total sum of the array.
Then I iterate through the array while maintaining a running left sum.
For each index, I calculate the right sum by subtracting the left sum and 
the current element from the total sum.
If both sums are equal, I return that index.
Otherwise I update the left sum and continue.
If no pivot exists, I return -1.
The time complexity is O(n) and space compleixty is O(1).

"""


