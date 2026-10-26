

# Subsequence বনাম Substring
# Subsequence: মাঝখানের character বাদ দেওয়া যায়, কিন্তু order ঠিক রাখতে হবে। যেমন "ace" হলো "abcde"-এর subsequence।
# Substring: character-গুলো পাশাপাশি থাকতে হবে। যেমন "bcd" হলো "abcde"-এর substring, কিন্তু "ace" নয়।

# Leetcode Problem: 392
# Repeated Search Using find()
class Solution:
   def isSubsequence(self, s: str, t: str) -> bool:
      pos = 0

      for cha in s:
         pos = t.find(cha, pos)

         if pos == -1:
            return False

         pos += 1 

      return True

# Complexity
# ধরি, m = {len}(s) এবং n = {len}(t)।
# Time: Worst case O(mn), কারণ প্রতিটি find()-কে অনেক character scan করতে হতে পারে।
# Extra space: O(1), auxiliary variable-এর জন্য।


# Two Pointers
class Solution:
   def isSubsequence(self, s: str, t: str) -> bool:
      i = 0
      j = 0

      while i < len(s) and j < len(t):
         if s[i] == t[j]:
            i += 1 

         j += 1 

      return i == len(s) 


# Complexity:
# Time Complexity: O(m+n) — প্রতিটি pointer শুধু সামনের দিকে এগোয়; t-এর প্রতিটি character সর্বোচ্চ একবার পরীক্ষা হয়।
# Extra Space Complexity: O(1) — দুটি integer pointer ব্যবহার করছি; অতিরিক্ত string বা data structure নেই।

"""
I use two pointers, one for each string.
I scan through t and advance the pointer for s whenever the characters match.
If the pointer for s reaches the end, all its characters have been found in the correct order.
The time complexity is O(m+n) and the extra space complexity is O(1).

"""