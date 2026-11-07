


# Leetcode Problem: 387. First Unique Character in a String
# HashMap 
class Solution:
   def firstUniqChar(self, s: str) -> int:

      frequency = {}

      for char in s:
         frequency[char] = frequency.get(char, 0) + 1

      for index, char in enumerate(s):
         if frequency[char] == 1:
            return index

      return -1

"""
First, I use a hash map to count the frequency of each character in the string.
Then, I traverse the string again from left to right.
If I find a character whose frequency is exactly one, I return its index.
If no unique character exists, I return -1.
Time Complexity: O(n).
Space Complexity: O(1), because the string contains only lowercase English letters.

"""


# Approach 2 — Array as Frequency Map
"""
যেহেতু Problem-এর Constraint অনুযায়ী String-এ শুধু lowercase English letters (a–z) আছে, 
তাই Dictionary-এর পরিবর্তে একটি List ব্যবহার করা যায়।

এখানে ২৬টি Character-এর জন্য ২৬টি Position থাকবে।

ord() Function
ord() একটি Character-এর Unicode Code Point Return করে।

"""
class Solution:
   def firstUniqChar(self, s: str) -> int:

      frequency = [0] * 26

      for char in s:
         index = ord(char) - ord("a")
         frequency[index] += 1

      for index, char in enumerate(s):
         index = ord(char) - ord("a")

         if frequency[index] == 1:
            return index

      return -1

   
print(ord("a"))
print(ord("b"))
print(ord("c"))
print(ord("z"))