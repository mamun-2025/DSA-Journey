

class Solution:
   def isPowerOfTwo(self, n: int) ->bool:

      if n <= 0:
         return False

      while n % 2 == 0:
         n //= 2

      return n == 1
   


"""
First of all, I check if n is less than or equal to zero, because a power of two must be positive.
Then I repeatedly divide n by 2 while it is divisible by 2.
If the final value becomes 1, the number is a power of two, so I return True.
Otherwise I return False.
The time complextity is 0(log n) and space complexity is 0(1).

"""


class Solution:
   def isPowerOfTwo(self, n: int) ->bool:
      if n <= 0:
         return False 

      return n & (n- 1) == 0 

"""
Pattern: Bit Manipulation
Complexity:
Time  → O(1)
Space → O(1)

A positive power of two has exactly one set bit in its binary representation.
When we subtract 1 from a power of two, that only set bit becomes 0,
and all the bits to its right become 1.
For example 8 is 1000, and 7 is 0111.
So: 1000 & 0111 = 0000
Therefor, if n is positive and n & (n-1) == 0, then n is a power of two.
The time complexity is 0(1), and the space complexity is 0(1).


"""