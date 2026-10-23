

# 1️⃣ Character Traversal কী?
""""
ধরুন:
text = "Python"

String:
P  y  t  h  o  n
0  1  2  3  4  5

আমরা যদি প্রতিটি character একবার করে দেখতে চাই:
text = "Python"

fof cha in text:
   print(cha)

Output:
P
y
t
h
o
n

এখানে ch প্রতিবার একটি করে character নিচ্ছে।
"""


# 2️⃣ 7-Step Analysis
"""
① Input কী?
"Python"

② Output কী?
P
y
t
h
o
n

③ Logic কী?
String-এর প্রতিটি character-এর উপর loop চালাব।
for ch in text:


④ Dry Run
text = "Python"

ch = P
ch = y
ch = t
ch = h
ch = o
ch = n

⑤ Time Complexity
String-এর length যদি n হয়:
n characters
↓
n iterations
↓
O(n)

⑥ Space Complexity
Extra variable ch constant:
O(1)

"""




# 3️⃣ Character Comparison
# এখন character-এর সাথে condition ব্যবহার করি।
# Problem
# String-এর মধ্যে "a" আছে কি না দেখুন।
text = "Programming"

for cha in text:
   if cha == "a":
      print("found")
   else:
      print("Not found")



# 4️⃣ == দিয়ে Character Compare
"""
সবচেয়ে গুরুত্বপূর্ণ operator:
==

উদাহরণ:
ch = "a"
if ch == "a":    
   print("Yes")

Output:
Yes

আর:
ch = "b"
if ch == "a":    
   print("Yes")

কিছু print হবে না।

"""



# 5️⃣ Count করার Foundation
# এখন শুধু "a" আছে কি না সেটা না দেখে কতবার আছে সেটা বের করি।
# "banana"-তে "a" কতবার আছে?
text = "banana"
count = 0

for cha in text:
   if cha == "a":
      count += 1

print(count)



"""
6️⃣ Dry Run — খুব গুরুত্বপূর্ণ
text = "banana"count = 0


Characters:
b a n a n a

Step-by-step
ch = b
b == a → False
count = 0

ch = a
a == a → True
count = 1

ch = n
n == a → False
count = 1

ch = a
a == a → True
count = 2

ch = n
n == a → False
count = 2

ch = a
a == a → True
count = 3

Final:
count = 3



7️⃣ Complexity
যদি string-এর length n হয়:

প্রতিটি character একবার check করছি।
Time = O(n)

আমরা শুধু count এবং ch ব্যবহার করছি।
Space = O(1)

"""



"""
8️⃣ Interview Explanation

"I initialize a counter with zero. 
Then I traverse the string once. 
Whenever the current character matches the target character, I increment the counter. 
Since every character is checked once, the time complexity is O(n), and the extra space is O(1)."

"""



# 9️⃣ Count Vowels
# এখন একই concept একটু বড় করি।
text = "Programming"

vowels = "aeiou"
count = 0


for cha in text:
   if cha in vowels:
      count += 1

print(count)



"""
🔟 in কী করছে?

if ch in vowels:

মানে:
ch কি vowels-এর মধ্যে আছে?

উদাহরণ:
"a" in "aeiou"
→ True

"b" in "aeiou"
→ False

"""



# 1️⃣1️⃣ Better Version — Set
# Interview/DSA-তে membership checking-এর জন্য Set ব্যবহার করা ভালো pattern:
text = "Programming"

vowels = {"a", "e", "i", "o", "u"}

count = 0

for cha in text:
   if cha in vowels:
      count += 1

print(count)



# 1️⃣2️⃣ Uppercase Handle করা
# আমরা চাই lowercase/uppercase উভয় vowel count করতে।
text = "PROGRAMMING"

vowels = {"a", "e", "i", "o", "u"}

count = 0

for ch in text.lower():
   if ch in vowels:
      count += 1

print(count)
"""
lower() নতুন string তৈরি করে।

তাই overall auxiliary space-এ string copy-এর কারণে:
Time  = O(n)
Space = O(n)

"""



# 1️⃣3️⃣ Character-এর Type Check
# Python-এর কিছু useful methods:
cha = "A"
print(cha.isupper())

cha = "a"
print(cha.islower())

num = "4"
print(num.isdigit())

cha = "abc12"
print(cha.isalnum())

cha = "abcd"
print(cha.isalpha())




# 1️⃣4️⃣ Count Digits in String
# কতগুলো digit আছে?
text = "abcd1234"

count = 0

for cha in text:
   if cha.isdigit():
      count += 1

print(count)



# 1️⃣5️⃣ Count Uppercase Characters
text = "GEEKsfoRGEEks"

count = 0

for cha in text:
   if cha.isupper():
      count += 1

print(count)


# Character Comparison দিয়ে Letter Check
letter = "abcde123"

count = 0

for cha in letter:
   if cha.isalpha():
      count += 1

print("Letter:", count)




"""
1️⃣6️⃣ গুরুত্বপূর্ণ Pattern

আজকের সব problem-এর pattern প্রায় একই:
count = 0for ch in text:    if condition:        count += 1


এটাকে বলি:
⭐ Counting Pattern
এটি DSA-তে অত্যন্ত গুরুত্বপূর্ণ।

পরবর্তীতে:
Count Vowels
Count Digits
Count Characters
Count Frequency
Count Duplicates
Count Occurrences

সব জায়গায় এই ধরনের pattern দেখতে পাবেন।


🧠 Interview Pattern Recognition
Problem দেখলেন:
"Count how many..."

সাথে সাথে ভাববেন:
Count
 ↓
Initialize counter
 ↓
Traverse
 ↓
Condition
 ↓
counter += 1

"""



"""
🔑 আজকের ৫টি জিনিস অবশ্যই মনে রাখবেন
1. String traversal
       ↓
   for ch in text

2. Index traversal
       ↓
   text[i]

3. Character comparison
       ↓
   ch == "a"

4. Condition
       ↓
   if ch in vowels

5. Counting
       ↓
   count += 1

Lesson 4-এর মূল কথা:
String problem দেখলে প্রথমে ভাববেন — “আমি কি প্রতিটি character একবার করে traverse করে কোনো condition check করতে পারি?”

যদি পারেন, খুব সম্ভবত আপনার প্রথম solution হবে O(n)।


"""

