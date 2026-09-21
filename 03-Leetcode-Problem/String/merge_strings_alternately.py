

class Solution:
   def mergeAlternately(self, word1: str, word2: str) ->str:
      result = []

      for i in range(max(len(word1), len(word2))):
         if i < len(word1):
            result.append(word1[i])

         if i < len(word2):
            result.append(word2[i])

      return "".join(result)


"""
I use one index to traverse both strings.
For each string, I append the character from the first string if it exists.
And then I append the character from the second string if it exists.
I use the maximum length so that the remaining characters of the longer strings are also included.

I traverse both strings using the same index. 
At each index, I append the character from word1 if it exists, then the character from word2 if it exists. 
I use a list to build the result efficiently and join the characters at the end.”

n = len(word1)
m = len(word2)
time complextity = (n+m) = 0(n)

result = []
space complexity = (n+m) = 0(n)

"""