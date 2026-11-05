

# 1. Anagram কী?
"""
Anagram হলো এমন দুটি Word বা String, যাদের Character একই থাকে 
এবং প্রতিটি Character-এর সংখ্যা সমান থাকে, 
কিন্তু Character-এর Order আলাদা হতে পারে।

উদাহরণ:
s = "listen"t = "silent"

দুটি String-এর Character:
- listen → l, i, s, t, e, n
- silent → s, i, l, e, n, t
Character একই, শুধু Order আলাদা।

তাই:
listen == silent

সাধারণ String Comparison অনুযায়ী False।

কিন্তু Anagram হিসেবে:
is_anagram("listen", "silent")

Result:
True

আরও কিছু উদাহরণ
String 1	   String 2	   Anagram?
listen	   silent	   True
eat	      tea	      True
rat	      car	      False
hello	      world	      False
anagram	   nagaram	   True
aab	      abb	      False

মূল শর্ত: প্রতিটি Character-এর Frequency সমান হতে হবে।

"""


# 2. Problem Statement — LeetCode 242
s = "silent"
t = "listen"

s = "anagram"
t = "nagaram"

s = "rat"
t = "car"

s = "aab"
t = "abb"

s = "aabbc"
t = "bbaac"

"""
Valid AnagramOriginal Problem:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

বাংলায় Problem বুঝি
তোমাকে দুটি String দেওয়া হবে:
- s
- t
তোমাকে পরীক্ষা করতে হবে t কি s-এর Anagram?

যদি দুটি String-এর Character এবং প্রতিটি Character-এর Frequency একই হয়, তাহলে True return করবে।
অন্যথায় False।

Example 1
s = "anagram"t = "nagaram"

Output:
True
কারণ দুটি String-এর সব Character-এর Frequency একই।


Example 2
s = "rat"t = "car"

Output:
False

কারণ:
- s-এ r আছে।
- t-তে r নেই।
- Character-গুলো এক নয়।


Example 3
s = "aab"t = "abb"

Output:
False

কারণ:
Character	s Frequency	t Frequency
a	2	1
b	1	2

এখানে Character একই হলেও Frequency সমান নয়।


3. Problem Solving-এর আগে গুরুত্বপূর্ণ Concept
ধরো:
s = "aabbc"t = "bbaac"

প্রথম String-এর Frequency:
{    "a": 2,    "b": 2,    "c": 1}

দ্বিতীয় String-এর Frequency:
{    "b": 2,    "a": 2,    "c": 1}

দুটি Dictionary-এর তথ্য একই।

তাই দুটি String Anagram।

আমাদের Logic:
1. প্রথম String-এর Frequency Map তৈরি করব।
2. দ্বিতীয় String-এর Frequency Map তৈরি করব।
3. দুটি Frequency Map Compare করব।
4. সমান হলে True, অন্যথায় False।

"""


# 4. Approach 1 — Brute Force Concept
s = "anagram"
t = "nagaram"

def is_anagram(s, t):
   return sorted(s) == sorted(t)

print(is_anagram(s, t))
"""
দুটি Sorted List একই।

তবে এটিকে সাধারণত Sorting Approach বলা হয়, Brute Force নয়।
Complexity Analysis
ধরি:
- n = s-এর Length
- m = t-এর Length
Operation	Complexity
Sorting s	O(n log n)
Sorting t	O(m log m)
Comparing	O(min(n, m)) পর্যন্ত

সাধারণভাবে, দুটি String-এর Length সমান হলে:
- Time: O(n log n)
- Space: O(n) — Python-এর sorted result তৈরি করার অতিরিক্ত memory-এর কারণে।
এই Approach সহজ, কিন্তু আমরা আরও Efficient Hash Map Approach শিখব।

"""



# 5. Approach 2 — Frequency Map (Dictionary)
class Solution:
   def is_anagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
         return False

      count_s = {}
      count_t = {}

      for char in s:
         count_s[char] = count_s.get(char, 0) + 1

      for char in t:
         count_t[char] = count_t.get(char, 0) + 1

      return count_s == count_t

solution = Solution()

print(solution.is_anagram("listen", "silent"))



"""
6. Dry Run — Step by Step

Input:
s = "aab"t = "aba"

Step 1 — Initialize
count_s = {}count_t = {}

Step 2 — Traverse s
s = "aab"

Step	Character	Frequency Dictionary
1	      a	      {'a': 1}
2	      a	      {'a': 2}
3	      b	      {'a': 2, 'b': 1}

Final:
count_s = {    "a": 2,    "b": 1}

Step 3 — Traverse t
t = "aba"

Step	Character	Frequency Dictionary
1	      a	      {'a': 1}
2	      b	      {'a': 1, 'b': 1}
3	      a	      {'a': 2, 'b': 1}

Final:
count_t = {    "a": 2,    "b": 1}

Step 4 — Compare
count_s == count_t

Result:
True

কারণ দুটি Dictionary-এর Key এবং Value একই।

"""


# 7. Approach 3 — Single Dictionary Optimization
"""
দুটি Dictionary তৈরি না করেও Anagram পরীক্ষা করা যায়।

আমরা একটি Dictionary ব্যবহার করব।
Logic
- s-এর প্রতিটি Character-এর Count বাড়াব।
- t-এর প্রতিটি Character-এর Count কমাব।
- শেষে প্রতিটি Character-এর Count শূন্য হলে Anagram।

"""
def is_anagram(s, t):
   if len(s) != len(t):
      return False

   frequency = {}

   for char in s:
      frequency[char] = frequency.get(char, 0) + 1

   for char in t:
      frequency[char] = frequency.get(char, 0) - 1

   for count in frequency.values():
      if count != 0:
         return False

   return True

print(is_anagram("abbc", "bbcc"))


# 8. Approach 4 — Python Counter
"""
Python-এর collections Module-এ Counter নামে একটি বিশেষ Class আছে।

এটি Frequency Counting-এর কাজ সহজ করে।

Counter(s) নিজেই প্রতিটি Character-এর Frequency তৈরি করে।

তবে DSA শেখার সময় আগে নিজে Dictionary দিয়ে Frequency Map তৈরি করতে শেখা জরুরি। 
Counter হলো সুবিধাজনক Built-in Tool।
"""
from collections import Counter

def is_anagram(s, t):

   return Counter(s) == Counter(t)

print(is_anagram("listen", "silent"))




"""
9. Approach Comparison
Approach	         Time Complexity	      Space Complexity
Sorting	         O(n log n)	            O(n)
Two Dictionaries	O(n) average	         O(k)
One Dictionary	   O(n) average	         O(k)
Counter	         O(n) average	         O(k)


এখানে k হলো unique Character-এর সংখ্যা। সাধারণ lowercase English alphabet-এর ক্ষেত্রে k ≤ 26।

কোনটি ব্যবহার করবে?
- সহজ Code চাইলে Sorting।
- Hash Map শেখার জন্য Two Dictionary।
- কম অতিরিক্ত Dictionary ব্যবহার করতে চাইলে One Dictionary।
- Python-এর Built-in সুবিধা চাইলে Counter।
Interview-এ Frequency Map Approach ব্যাখ্যা করতে পারলে ভালো হবে।

"""