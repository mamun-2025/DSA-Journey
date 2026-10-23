

# 1️⃣ String কী?
"""
সহজ ভাষায়:
String হলো এক বা একাধিক character-এর sequence।

Example:
name = "Mamun"


এখানে:
M a m u n

প্রতিটি হলো একটি character।

পুরো "Mamun" হলো একটি String।
🧠 String-কে Array-এর মতো ভাবুন
আপনি আগে Array/List দেখেছেন:
numbers = [10, 20, 30, 40]


String-ও position অনুযায়ী character ধরে রাখে:
text = "Python"


এভাবে চিন্তা করুন:
Index:    0   1   2   3   4   5
          ↓   ↓   ↓   ↓   ↓   ↓
String:   P   y   t   h   o   n

তাই:
text[0]


দিলে:
P
"""


# 2️⃣ String Indexing
text = "Python"

print(text[0])
print(text[1])
print(text[2])
"""
কারণ:
Index:    0   1   2   3   4   5
          ↓   ↓   ↓   ↓   ↓   ↓
String:   P   y   t   h   o   n

⭐ গুরুত্বপূর্ণ: Index 0 থেকে শুরু হয়
Programming-এ সাধারণত প্রথম element-এর index:
0

দ্বিতীয়:
1

তৃতীয়:
2

অর্থাৎ:
Position → 1  2  3  4  5  6
Index    → 0  1  2  3  4  5

"""




# 3️⃣ Negative Index
"""
Python-এ পিছন থেকেও access করা যায়।
text = "Python"


Positive Index:

Index:    0   1   2   3   4   5
          ↓   ↓   ↓   ↓   ↓   ↓
          P   y   t   h   o   n


Negative Index:

Index:   -6  -5  -4  -3  -2  -1
          ↓   ↓   ↓   ↓   ↓   ↓
          P   y   t   h   o   n

"""
text = "Python"

print(text[-1])
print(text[-2])




# 4️⃣ String Length
# Python-এর len() দিয়ে String-এর character সংখ্যা বের করি।

text = "Programming"

print(len(text))
"""
কারণ:
P y t h o n
↓ ↓ ↓ ↓ ↓ ↓
1 2 3 4 5 6

Complexity
len(text)

Python string-এর length সরাসরি stored থাকে, তাই সাধারণভাবে:
Time: O(1)
Space: O(1)

"""



# 5️⃣ String Traversal
# String-এর প্রতিটি character একে একে visit করা।
text = "Programming"

for cha in text:
   print(cha)




# 6️⃣ Index দিয়ে Traversal
text = "Programming"

for i in range(len(text)):
   print(i)

for i in range(len(text)):
   print(text[i])




#7️⃣ Character Comparison
# String problem-এ character compare করা খুব গুরুত্বপূর্ণ।
text = "apple"

if text[0] == "b":
   print("Match")
else:
   print("Not Match")



# 8️⃣ String Immutable
# String তৈরি করার পর individual character সরাসরি পরিবর্তন করা যায় না।

# List Mutable
array = [10, 20, 30, 40]
array[0] = 100
print(array)

# String Immutable
string = "Python"
# string[0] = "J"  
print(string)

# অর্থাৎ String-এর character পরিবর্তন করতে চাইলে নতুন String তৈরি করতে হয়।
string = "Python"
new_string = "J" + string[1:]
print(new_string)

"""
🧠 Mutable vs Immutable
Data Type	         Mutable?
List	               ✅ Yes
Dictionary	         ✅ Yes
Set	               ✅ Yes
Tuple	               ❌ No
String	            ❌ No

"""



# 9️⃣ String Slicing
# Syntax: [start:end]
text = "Python"
print(text[1:4])
# 1 থেকে শুরু করবে, কিন্তু 4 বাদ যাবে।
# 1 ≤ index < 4



# 🔟 Reverse String Using Slicing
text = "Sajib"
reverse = text[::-1]
print(reverse)
"""
Complexity:
Time: O(n)
Space: O(n)

কারণ নতুন reversed string তৈরি হয়।
"""



# 1️⃣1️⃣ String-এর মধ্যে Character আছে কি না
text = "Python"

if "P" in text:
   print("Found")

if "p" in text.lower():
   print("Found")

"""
এটি সাধারণভাবে string-এর মধ্যে search করে।

Worst-case complexity:
O(n)

কারণ target শেষেও থাকতে পারে বা একেবারেই নাও থাকতে পারে।

"""


# 1️⃣2️⃣ একটি গুরুত্বপূর্ণ Basic Problem
# Count Characters 
# String-এ মোট কতটি character আছে তা বের করুন।
text = "Programming"

count = 0

for cha in text:
   count += 1

print(count)





"""
🔥 আজকের মূল কথা
আপনার মাথায় এই চারটি জিনিস বসাতে হবে:
String
 ↓
Character Sequence

Index
 ↓
Position Access

Traversal
 ↓
Character by Character

Comparison
 ↓
Character == Target


আর Complexity-এর ক্ষেত্রে:
text[0]       → O(1)
text[i]       → O(1)
for ch in text → O(n)
text[::-1]    → O(n) time + O(n) space

"""