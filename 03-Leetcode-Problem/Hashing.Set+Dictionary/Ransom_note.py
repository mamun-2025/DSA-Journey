


# Leetcode Problem: 383. Ransom Note
# Dictionary/HashMap
# তোমাকে দুটি String দেওয়া হয়েছে:
# - ransomNote — যে শব্দটি তৈরি করতে হবে।
# - magazine — যেখান থেকে অক্ষর সংগ্রহ করা যাবে।
# তোমাকে পরীক্ষা করতে হবে, magazine-এর অক্ষর ব্যবহার করে ransomNote তৈরি করা সম্ভব কি না।

# গুরুত্বপূর্ণ নিয়ম: Magazine-এর প্রতিটি অক্ষর সর্বোচ্চ একবার ব্যবহার করা যাবে।

# আমরা প্রথমে magazine String-এর প্রতিটি অক্ষর কতবার আছে, তা Dictionary-তে সংরক্ষণ করব।
# এরপর ransomNote-এর প্রতিটি অক্ষর পরীক্ষা করব।
# - অক্ষরটি Dictionary-তে না থাকলে → False
# - অক্ষরটির সংখ্যা 0 হলে → False
# - অক্ষরটির সংখ্যা থাকলে → সেটি একবার ব্যবহার করব এবং count কমিয়ে দেব।

ransomNote = "aa"
magazine = "aab"

class Solution:
   def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      char_count = {}

      for char in magazine:
         char_count[char] = char_count.get(char, 0) + 1
         # if char in char_count:
         #     char_count[char] += 1
         # else:
         #     char_count[char] = 1

      for char in ransomNote:
         if char not in char_count or char_count[char] == 0:
            return False

         char_count[char] -= 1

      return True

# Time Complexity: O(n+m)
# Space Complexity: O(1)
# সাধারণভাবে Dictionary-তে kটি distinct character থাকলে Space Complexity O(k)। এখানে k ≤ 26, তাই O(1)।


# Python Counter
# Python-এর collections.Counter ব্যবহার করেও একই Problem সমাধান করা যায়।
# Counter হলো Dictionary-এর মতো একটি বিশেষ Class, যা Automatically Frequency গণনা করে।
from collections import Counter

ransomNote = "aa"
magazine = "ab"
class Solution:
   def canConstruct(self, ransomNote: str, magazine: str)-> bool:
      magazine_count = Counter(magazine) # এখানে Counter নিজেই Frequency গণনা করেছে।

      for char in ransomNote:
         if magazine_count[char] == 0:
            return False

         magazine_count[char] -= 1

      return True

   
"""
First, I count the frequency of the each character in the magazine using a hash map.
Then, I iterate through the ransom note and check wheter each charter is available.
If a character is unavailable or its frequency becomes zero, I return False.
Otherwise, I decrese its frequency by one because each character can only be used once.
If all character are successfully matched, I return True.
Time complexity: O(n+m)
Space Complexity: O(1)/O(k), because there are only 26 lowercase English letters.
"""
      
