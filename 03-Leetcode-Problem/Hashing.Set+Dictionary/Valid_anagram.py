

# Leetcode Problem: 242. Valid Anagram
s = "eat"
t = "tea"

class Solution:
   def isAnagram(self, s: str, t: str)-> bool:
      if len(s) != len(t):
         return False

      count_s = {}
      count_t = {}

      for char in s:
         count_s[char] = count_s.get(char, 0) + 1

      for char in t:
         count_t[char] = count_t.get(char, 0) + 1

      return count_s == count_t 

   
# Time complexity: O(n)
# Space complexity: O(k)

"""
I use a single hash map to compare the character frequencies of both strings.
First, I check whether their lengths are equal.
Then, I icrease the frequency of each character in the first string 
and decrease the frequency of each character in the second string.
Finally, I check whether all frequency values are zero.
If they are, the strings are anagrams.
Time complexity: O(n)
Space Complexity: O(1), because the input contains only lowercase English letters.

"""