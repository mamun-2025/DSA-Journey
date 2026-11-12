

# Leetcode Problem: 49. Group Anagrams
# Optimized Python Code — Sorting + Dictionary
strs = ["eat", "tea", "tan", "nat", "ate", "bat"]

class Solution:
   def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      groups = {}

      for word in strs:
         key = "".join(sorted(word))

         if key not in groups:
            groups[key] = []

         groups[key].append(word)

      return list(groups.values())

"""
I use a hash map to group anagrams.
For each word, I sort its characters and use the sorted string as a key.
If the key already exists, I append the word to that group.
Otherwise, I create a new group.
Finally, I return all the groups as the list.
Time complexity: O(N X K log K)
Space complexity: O(N X K), including the output.
"""

# Alternative Approach — Frequency Counting + Dictionary
def groupAnagrams(strs):

   groups = {}

   for word in strs:

      count = [0] * 26 

      for char in word:
         index = ord(char) - ord('a')
         count[index] += 1

      key = tuple(count)

      if key not in groups:
         groups[key] = []

      groups[key].append(word)

   return list(groups.values())





