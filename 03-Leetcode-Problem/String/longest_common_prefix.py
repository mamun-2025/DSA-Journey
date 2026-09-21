

class Solution:
   def longestCommonPrefix(self, strs: list[str]) ->str:
      result = ""

      for i in range(len(strs[0])):
         for word in strs:
            if i >= len(word) or word[i] != strs[0][i]:
               return result 

         result += strs[0][i]

      return result

         
"""
I use the first string as a reference 
and compare each character position with the same position in every other string.
If a string ends or a character doesn't match,
I immediately return the prefix found so far.

n = number of strings
m = length of the shortest string
time = 0(nxm) 
space = 0(1)

"""