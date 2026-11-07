


# 1. Unique Character কী?
# Unique Character হলো এমন Character, যা একটি String-এর মধ্যে মাত্র একবার এসেছে।

"""
Character Frequency:
text = "leetcode"

Character	Frequency
l	         1
e	         3
t	         1
c	         1
o	         1
d	         1

এখানে:
- l এসেছে 1 বার।
- e এসেছে 3 বার।
- t এসেছে 1 বার।
- c এসেছে 1 বার।

তাহলে Unique Characters হলো:
l, t, c, o, d

কিন্তু আমাদের শুধু যেকোনো একটি Unique Character নয়, First Unique Character খুঁজতে হবে।

সুতরাং উত্তর:
l

কারণ l প্রথমে এসেছে এবং এটি মাত্র একবার রয়েছে।

"""


# 2. Problem Statement — LeetCode 387
"""
First Unique Character in a String

Original Problem:
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

বাংলায় Problem বুঝি
তোমাকে একটি String দেওয়া হবে।

তোমাকে বের করতে হবে:
1. কোন Character মাত্র একবার এসেছে?
2. তাদের মধ্যে প্রথম Character কোনটি?
3. সেই Character-এর Index কত?
যদি কোনো Unique Character না থাকে, তাহলে -1 return করবে।

Example 1
s = "leetcode"

Output:
0

কারণ:
- l প্রথম Character।
- l মাত্র একবার এসেছে।
- এর Index হলো 0।


Example 2
s = "loveleetcode"

Output:
2

কারণ:
- l একাধিকবার এসেছে।
- o একাধিকবার এসেছে।
- v প্রথম Unique Character।
- v-এর Index হলো 2।


Example 3
s = "aabb"

Output:
-1

কারণ কোনো Character মাত্র একবার আসেনি।

"""


# 3. Problem Solving Logic
"""
এখানে একটি গুরুত্বপূর্ণ বিষয় বুঝতে হবে।

আমরা শুধু Frequency Count করলেই হবে না। আমাদের Original String-এর Order বজায় রাখতে হবে।

তাই আমরা দুটি Pass ব্যবহার করব।

Pass 1 — Frequency Counting

প্রথমে প্রতিটি Character কতবার এসেছে তা Dictionary-তে রাখব।

Pass 2 — Find First Unique Character

আবার Original String Traverse করব।

যে Character-এর Frequency 1, তার Index return করব।

কেন?

কারণ Original String বাম থেকে ডানে Traverse করলে প্রথম যে Unique Character পাব, সেটিই আমাদের উত্তর।

"""


# 4. Python Code — Optimized Solution
def firstUniqueChar(s):

   frequency = {}

   for char in s:
      frequency[char] = frequency.get(char, 0) + 1

   for i in range(len(s)):
      if frequency[s[i]] == 1:
         return i 

   return -1

print(firstUniqueChar("leetcode"))
print(firstUniqueChar("loveleetcode"))
print(firstUniqueChar("aabb"))



# 5. Alternative Approach — enumerate()
# Python-এর enumerate() Function দিয়ে একই Problem আরও সুন্দরভাবে লেখা যায়।
def firstUniqueChar(s):

   frequency = {}

   for char in s:
      frequency[char] = frequency.get(char, 0) + 1

   for index, char in enumerate(s): # একসঙ্গে Index এবং Character পাওয়া যাচ্ছে।

      if frequency[char] == 1:
         return index

   return -1



# 6. Brute Force Approach 
def firstUniqueChar(s):

   for i in range(len(s)):

      if s.count(s[i]) == 1:
         return i 

   return -1


# 7. আজকের Master Concept
"""
Frequency + Traversal Pattern
1. প্রথমবার পুরো String Traverse করো।
2. Dictionary-তে Frequency Store করো।
3. দ্বিতীয়বার Original String Traverse করো।
4. যে Character-এর Frequency 1, তার Index Return করো।
5. না পেলে -1 Return করো।

Key Formula

frequency[char] == 1

Complexity: O(n) Time, O(k) Space.

"""
