


class Solution:
   def isPalindrome(self, s: str) -> bool:
      left = 0
      right = len(s) - 1

      while left < right:

         while left < right and not s[left].isalnum():
            left += 1

         while left < right and not s[right].isalnum():
            right -= 1

         if s[left].lower() != s[right].lower():
            return False

         left += 1
         right -= 1

      return True


"""
I use two pointers, one from the beginning and one from the end.
I skip non-alphanumeric characters using isalnum().
Then, I compare the remaining characters in lowercase.
If any pair does not match, I return false.
If all valid characters match, I return True.
The time complexity is 0(n) and the space complexity is 0(1).


"""



