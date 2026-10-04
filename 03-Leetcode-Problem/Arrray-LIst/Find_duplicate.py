


# 1️⃣ Duplicate কী?
"""
Duplicate মানে একই value একাধিকবার থাকা।

উদাহরণ:

arr = [1, 2, 3, 2, 4]

এখানে:

1 → একবার
2 → দুইবার ← Duplicate
3 → একবার
4 → একবার

তাই duplicate:

2

আরেকটি example:

arr = [5, 7, 8, 5, 9]

এখানে:

5 → দুইবার

তাই:

Duplicate = 5

"""



# 2️⃣ Problem কী?
"""
আমাদের একটি array দেওয়া হবে:

arr = [1, 2, 3, 2, 4]

আমাদের কাজ:

প্রথম যে value-টি আমরা দ্বিতীয়বার দেখতে পাচ্ছি, সেটি return করা।

Expected:

2

"""



# 3️⃣ Input কী?
# একটি List/Array:
# arr = [1, 2, 3, 2, 4]



# 4️⃣ Output কী?
# Duplicate value:
# 2



# 5️⃣ প্রথমে সহজ Brute Force Approach
"""
Set শেখার আগে আমরা nested loop দিয়ে problem-টা বুঝব।

Idea:

প্রতিটি element নাও
        ↓
তার পরের elementগুলোর সাথে compare করো
        ↓
একই হলে duplicate

"""



## 6️⃣ Brute Force Code
arr = [1, 2, 3, 2, 4]

for i in range(len(arr)):
   for j in range(i+1, len(arr)):
      if arr[i] == arr[j]:
          print(arr[i])


##
def find_duplicate(arr):
   for i in range(len(arr)):
      for j in range(i+1, len(arr)):
         if arr[i] == arr[j]:
            return arr[i]

   return -1

arr = [1, 2, 3, 4, 3, 5]
print(find_duplicate(arr))




# 7️⃣ Code Line by Line
"""
Outer loop
for i in range(len(arr)):

প্রতিটি element একবার করে নির্বাচন করছি।

Inner loop
for j in range(i + 1, len(arr)):

বর্তমান element-এর পরের elementগুলো check করছি।

i + 1 কেন?

কারণ নিজেকেই নিজের সাথে compare করার দরকার নেই।

Compare
if arr[i] == arr[j]:

দুটি value একই হলে duplicate পাওয়া গেছে।

Return
return arr[i]

Duplicate value return করছি।

"""



# 8️⃣ 🔥 Dry Run
"""
ধরি:
arr = [1, 2, 3, 2, 4]

Index:
index:  0  1  2  3  4
value:  1  2  3  2  4

Step 1
i = 0
arr[i] = 1

এর পরেরগুলো:
1 vs 2 ❌
1 vs 3 ❌
1 vs 2 ❌
1 vs 4 ❌

Duplicate পাওয়া গেল না।

Step 2
i = 1
arr[i] = 2

এর পরেরগুলো:

2 vs 3 ❌
2 vs 2 ✅

Duplicate পাওয়া গেছে।
return 2

Output:
2

"""



# 9️⃣ কেন range(i + 1, len(arr))?
"""
এটা খুব গুরুত্বপূর্ণ।

ধরি:
arr = [10, 20, 30]

i = 0 হলে:
range(1, 3)

মানে:
j = 1
j = 2

আমরা compare করব:
10 vs 20
10 vs 30
10 vs 10 করার দরকার নেই।

i = 1 হলে:
range(2, 3)

তখন:
20 vs 30

এভাবে duplicate pair check করা হয়।

"""



# 🔟 Brute Force Complexity
"""
এখানে দুটি loop আছে:

for i in range(...):
    for j in range(...):

একটি loop-এর ভিতরে আরেকটি loop।

তাই:

Time Complexity
O(n²)
Space Complexity
O(1)

আমরা extra data structure ব্যবহার করছি না।

"""



# 1️⃣1️⃣ সমস্যা কোথায়?
"""

ধরি array:

100,000 elements

Nested loop হলে অনেকগুলো comparison করতে হবে।

তাই আমাদের আরও efficient approach দরকার।

এখানে আসে:

⭐ Set

"""




# 1️⃣2️⃣ Set কী?
"""
Python-এর set হলো এমন একটি collection যেখানে unique values রাখা হয়।

Example:

numbers = {1, 2, 3, 4}

যদি duplicate value add করি:

numbers = {1, 2, 3}

numbers.add(2)

তাহলে:

{1, 2, 3}

আবার 2 আলাদা করে যোগ হবে না।

"""



# 1️⃣3️⃣ Set-এর সবচেয়ে গুরুত্বপূর্ণ Feature
"""

Set-এর মূল strength:

Fast membership checking

অর্থাৎ:

if x in seen:

এটা সাধারণত average case-এ:

O(1)

সময় নিতে পারে।

"""



# 1️⃣4️⃣ Set দিয়ে Duplicate Find
"""
এখন আমাদের logic:

একটি empty set তৈরি করো
        ↓
array traverse করো
        ↓
বর্তমান value set-এ আছে?
       ↙       ↘
     Yes        No
      ↓          ↓
 Duplicate     set-এ add
      ↓
    Return

"""
# Code:
def find_duplicate(arr):
   seen = set()

   for number in arr:
      if number in seen:
         return number

      seen.add(number)

   return -1




# 1️⃣5️⃣ Code Line by Line
"""
Step 1
seen = set()

একটি empty set তৈরি করলাম।

seen মানে:

আমরা আগে যেসব value দেখেছি।

Step 2
for number in arr:

Array-এর প্রতিটি value একে একে নিচ্ছি।

Step 3
if number in seen:

প্রশ্ন করছি:

এই value কি আমরা আগে দেখেছি?

যদি Yes:

Duplicate!
Step 4
return number

Duplicate পাওয়া গেছে।

Step 5
seen.add(number)

যদি আগে না থাকে, তাহলে set-এ রেখে দিই।

মানে:

"এই value আমি already দেখেছি।"

"""



# 1️⃣6️⃣ 🔥 Set Approach Dry Run
"""
Input:

arr = [1, 2, 3, 2, 4]

শুরু:

seen = {}
প্রথম value
number = 1

Check:

1 in seen?
No

Add:

seen = {1}
দ্বিতীয় value
number = 2

Check:

2 in seen?
No

Add:

seen = {1, 2}
তৃতীয় value
number = 3

Check:

3 in seen?
No

Add:

seen = {1, 2, 3}
চতুর্থ value
number = 2

Check:

2 in seen?
Yes ✅

তাই:

return 2

Output:

2

"""




# 1️⃣7️⃣ Brute Force বনাম Set
"""
| বিষয়        | Brute Force  | Set           |
| ----------- | ------------ | ------------- |
| Approach    | Nested Loop  | Set           |
| Time        | O(n²)        | O(n) average  |
| Extra Space | O(1)         | O(n)          |
| সহজ         | হ্যাঁ        | হ্যাঁ         |
| বড় input    | ধীর হতে পারে | সাধারণত দ্রুত |

এখানে একটি গুরুত্বপূর্ণ DSA lesson:
Time কমানোর জন্য অনেক সময় extra memory ব্যবহার করা হয়।

এটাকে broadly বলা যায়:
Time-Space Tradeoff

"""



# 1️⃣8️⃣ Time Complexity — Set Approach
"""

আমরা array একবার traverse করছি:

for number in arr:

এটা:

O(n)

প্রতিটি iteration-এ:

number in seen

এবং:

seen.add(number)

সাধারণত average:

O(1)

তাই মোট:

O(n)

"""




# 1️⃣9️⃣ Space Complexity
"""
আমরা:

seen = set()

ব্যবহার করছি।

যদি সবগুলো value unique হয়, তাহলে set-এ nটি value থাকতে পারে।

তাই:

Space = O(n)

"""




# 2️⃣0️⃣ খুব গুরুত্বপূর্ণ: set() বনাম {}
"""
Empty set তৈরি করতে:

seen = set()

ব্যবহার করবে।

এটা:

seen = {}

হলে empty dictionary হবে।

তাই:

set()  → Empty Set
{}     → Empty Dictionary

এটা মনে রাখবে।

"""




# 2️⃣1️⃣ Duplicate না থাকলে?
# শেষে কোনো duplicate পাওয়া যাবে না।
def find_duplicate(arr):
   seen = set()

   for x in arr:
      if x in seen:
         return x 

      seen.add(x)

   return -1

arr = [1, 2, 3, 4, 5]
print(find_duplicate(arr))



# 2️⃣2️⃣ Empty List
# Loop চলবে না।
arr = []

def find_duplicate(arr):
   seen = set()

   for i in arr:
      if i in seen:
         return i 

      seen.add(i)

   return -1

result = find_duplicate(arr)
print(result)



# 2️⃣3️⃣ Duplicate প্রথমেই হলে?
"""
ধরি:
arr = [5, 5, 10, 20]

Dry Run:
seen = {}

5 → not in seen → add
seen = {5}

5 → already in seen → Duplicate!

Return:
5

"""



# 2️⃣4️⃣ একাধিক Duplicate থাকলে?
# ধরি:
# arr = [1, 2, 3, 2, 3, 4]
# আমাদের code:

def find_duplicate(arr):
    seen = set()

    for number in arr:
        if number in seen:
            return number

        seen.add(number)

    return -1
"""
প্রথম duplicate যেটা encounter করবে, সেটাই return করবে।

এখানে:
1 → new
2 → new
3 → new
2 → duplicate

Output:
2

এটা সব duplicate return করছে না।

"""


# 2️⃣5️⃣ যদি সব Duplicate বের করতে চাই?
def find_all_duplicates(arr):
   seen = set()
   duplicates = set()

   for number in arr:
      if number in seen:
         duplicates.add(number)
      else:
         seen.add(number)

   return duplicates

arr = [1, 2, 3, 2, 3, 4, 3]
print(find_duplicate(arr))




# 2️⃣6️⃣ একটি গুরুত্বপূর্ণ প্রশ্ন
"""
seen.add(number) আগে করলে কী হবে?

ভুল logic:

for number in arr:
    seen.add(number)

    if number in seen:
        return number

এখানে কী হবে?

প্রথম value:

number = 1

প্রথমে:

seen = {1}

তারপর:

1 in seen

অবশ্যই True।

তাই প্রথম element-ই duplicate বলে ধরে নেবে।

❌ ভুল।

সঠিক order:

if number in seen:
    return number

seen.add(number)

অর্থাৎ:

প্রথমে Check
তারপর Add

"""




# 2️⃣7️⃣ 🔥 Pattern মনে রাখো
"""

Duplicate detection-এর সবচেয়ে গুরুত্বপূর্ণ pattern:

ARRAY
  ↓
TRAVERSE
  ↓
"আগে দেখেছি?"
  ↓
YES → DUPLICATE
  ↓
NO
  ↓
SET-এ ADD

Code:

seen = set()

for x in arr:
    if x in seen:
        return x

    seen.add(x)

এই pattern তুমি অনেক problem-এ দেখতে পাবে।

"""




# 2️⃣8️⃣ Real-Life Example
"""
ধরো security gate-এ visitor ID আসছে:

101
205
310
205
450

Gate system প্রতিটি ID-এর জন্য জিজ্ঞেস করছে:

"এই ID আগে এসেছিল?"

প্রথম:

101 → নতুন → record

তারপর:

205 → নতুন → record

তারপর:

310 → নতুন → record

আবার:

205 → আগে আছে → Duplicate!

এটাই seen set pattern।

"""




# 2️⃣9️⃣ আজকের সবচেয়ে গুরুত্বপূর্ণ DSA Concept
"""
আজ আমরা একটি বড় ধারণা শিখলাম:

Time-Space Tradeoff

Brute Force:

Time  → O(n²)
Space → O(1)

Set:

Time  → O(n)
Space → O(n)

অর্থাৎ:

আমরা extra memory ব্যবহার করে time complexity কমিয়েছি।

এটা একজন software engineer-এর problem-solving mindset-এর খুব গুরুত্বপূর্ণ অংশ।

"""




# 3️⃣0️⃣ Interview Question 🎤
"""
Q1. How do you find a duplicate in an array?

তুমি বলতে পারো:

“I use a set to keep track of the elements I have already seen. While traversing the array, if an element is already in the set, it is a duplicate, so I return it. Otherwise, I add the element to the set.”

Q2. What is the time complexity?

“The time complexity is O(n) on average because I traverse the array once and set membership checking is O(1) on average.”

Q3. What is the space complexity?

“The space complexity is O(n) because the set can store up to n unique elements.”

Q4. Can you solve it without extra space?

বলতে পারো:

“Yes, depending on the constraints, I can use a brute-force approach with O(1) extra space, but it takes O(n²) time. Other approaches may be possible if the input has additional constraints, such as a sorted array or a restricted value range.”

এটা ভালো interview answer কারণ তুমি শুধু একটি solution নয়, trade-off বুঝতে পারছ।

"""



# 3️⃣1️⃣ 🧠 Important English Words
"""
| English     | বাংলা                               |
| ----------- | ----------------------------------- |
| Duplicate   | পুনরাবৃত্ত value                    |
| Unique      | একবার/স্বতন্ত্র                     |
| Seen        | আগে দেখা                            |
| Membership  | কোনো collection-এর মধ্যে থাকা       |
| Detect      | শনাক্ত করা                          |
| Brute Force | সরাসরি/কম optimized পদ্ধতি          |
| Optimize    | আরও efficient করা                   |
| Trade-off   | একদিকে সুবিধার বিনিময়ে অন্যদিকে খরচ |
| Extra Space | অতিরিক্ত memory                     |
| Comparison  | তুলনা                               |


"""



# 3️⃣2️⃣ 📝 1-Page Interview Note
"""
🟢 FIND DUPLICATE

Goal:
Array-এর duplicate value খুঁজে বের করা।

Example:
arr = [1, 2, 3, 2, 4]

Output:
2


Approach 1 — Brute Force

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            return arr[i]

Time:
O(n²)

Space:
O(1)


Approach 2 — Set

def find_duplicate(arr):
    seen = set()

    for x in arr:
        if x in seen:
            return x

        seen.add(x)

    return -1


Logic:

আগে দেখেছি?
     ↓
YES → Duplicate
NO  → Set-এ add


Time:
O(n) average

Space:
O(n)


Important Pattern:

seen = set()

for x in arr:
    if x in seen:
        return x

    seen.add(x)


Key Concept:

Time-Space Tradeoff

Brute Force:
O(n²) time + O(1) space

Set:
O(n) average time + O(n) space

"""


# Short Paragraph"
"""
Finding a duplicate in an array means detecting a value that appears more than once. 
A simple brute-force approach uses two nested loops to compare each element with the elements that come after it, 
which takes O(n²) time and O(1) extra space. 
A more efficient approach uses a Python set to keep track of the values we have already seen.
While traversing the array, we check whether the current value is already in the seen set; 
if it is, we have found a duplicate and can return it immediately,
otherwise we add the value to the set and continue. 
This approach takes O(n) time on average because set membership checking and insertion are O(1) on average, 
while the extra space is O(n) because the set may store up to n unique values. 
An important detail is to check if number in seen before calling seen.add(number), 
because adding the value first would make the current value appear to be a duplicate. 
This problem demonstrates an important DSA concept called the time-space tradeoff,
where we use extra memory to reduce the running time. 
The key pattern is: traverse the array, check whether the value has been seen before, 
return it if it has, and otherwise add it to the set.


বাংলা অর্থ:
একটি Array-তে duplicate খুঁজে বের করা মানে এমন কোনো value শনাক্ত করা, যেটি একাধিকবার এসেছে। 
এর একটি সহজ Brute Force approach হলো দুটি nested loop ব্যবহার করে প্রতিটি element-এর সাথে তার পরের elementগুলো compare করা। 
এই পদ্ধতিতে O(n²) time এবং O(1) extra space লাগে। 
আরও efficient approach হলো Python-এর set ব্যবহার করা। 
আমরা একটি seen set তৈরি করি, যেখানে আগে দেখা valueগুলো রাখি। 
Array traverse করার সময় প্রথমে check করি বর্তমান value-টি seen set-এর মধ্যে আগে থেকেই আছে কি না। 
যদি থাকে, তাহলে সেটি duplicate এবং আমরা সঙ্গে সঙ্গে value-টি return করতে পারি। 
আর যদি না থাকে, তাহলে সেটিকে seen set-এ add করে পরবর্তী element-এর দিকে যাই। 
এই approach-এর average time complexity O(n), কারণ set-এর membership checking এবং insertion সাধারণত O(1) সময় নেয়। 
আর space complexity O(n), কারণ সর্বোচ্চ nটি unique value seen set-এ থাকতে পারে। 
এখানে একটি গুরুত্বপূর্ণ বিষয় হলো, seen.add(number) করার আগে if number in seen check করতে হবে। 
কারণ আগে add করলে current value-টিকেই ভুলভাবে duplicate হিসেবে ধরে নেওয়া হবে। 
এই problem আমাদের একটি গুরুত্বপূর্ণ DSA concept শেখায়, যার নাম Time-Space Tradeoff—অর্থাৎ extra memory ব্যবহার করে 
আমরা execution time কমিয়ে আনছি। 
মূল pattern হলো: Array traverse করো → value আগে দেখা হয়েছে কি না check করো → দেখা 
থাকলে duplicate return করো → না থাকলে set-এ add করো।

"""
