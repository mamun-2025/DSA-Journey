

class Solution:
   def reverseString(self, s: list[str]) -> None:
      left = 0
      right = len(s) - 1 

      while left < right:
         s[left], s[right] = s[right], s[left]
         left += 1
         right -= 1


"""

I use two pointers, one at the biginning and one at the end of the array.
I swap the characters at these two positions and then move the left pointer forward and right pointer backward.
I continue until the pointers meet.
This reverses the array in-place with 0(n) time and 0(1) extra space.

"""