


# Leetcode Problem: 771. Jewels and Stones
# Nested Loop
jewels = "aA"
stones = "aAAbbbb"

class Solution:
   def numJewelIsStones(self, jewels: str, stones: str) -> int:
      count = 0

      for stone in stones:
         for jewel in jewels:
            if stone == jewel:
               count += 1
               break 

      return count

# Time Complexity: O(s X j)
# Space Complexity: O(1)


# Hash Set 
class Solution:
   def numJewelsIsStones(self, jewels: str, stones: str) -> int:
      jewel_set = set(jewels)

      count = 0

      for stone in stones:
         if stone in jewel_set:
            count += 1

      return count 


# Time Complexity: O(J + S)
# Auxiliary Space Complexity: O(J)
# কারণ jewel_set-এ সর্বোচ্চ J টি unique character থাকবে।

"""
Convert the jewels string into a set.
Iterate through stones and check whether each character exists in the set.
If it exists, increase the counter.
Time Complexity: O(J + S)
Space Complexity: O(J)

Why do we use a Hash Set?
= A Hash Set provides average O(1) membership checking.
This makes the solution faster than using nested loop.

Why do we count repeated stones?
= Every stone is counted separately. If the same jewel appears three times in stones, 
  it contributes three to the answer.

Is the comparison case-sensitive?
= Yes. Uppercase and lowercase letters are different characters.
"""