

class Solution:
   def lengthOfLastWord(self, s: str) ->int:

      right = len(s) - 1
      count = 0

      while right >= 0 and s[right] == " ":
         right -= 1

      while right >= 0 and s[right] != " ":
         count += 1
         right -= 1

      return count


"""

I start form the end of the string and skip all trailing spaces.
Then I count characters until I reach a space.
The count is the length of the last word.

I traverse the string from right to left, skip trailing spaces, and count the characters of the last word.

traverse from right to left → ডান থেকে বামে যাওয়া
trailing spaces → শেষে থাকা spaces
count characters → character গণনা করা
last word → শেষ শব্দ

Time Complexity = 0(n)
Space Complexity = 0(1)

"""
