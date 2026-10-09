

# Leetcode Problem
# Remove_duplicates_from_sorted_array

class Solution:
   def removeDuplicates(self, nums: list[int])-> int:
      i = 0

      for j in range(1, len(nums)):
         if nums[j] != nums[i]:
            i += 1 
            nums[i] = nums[j]

      return i + 1 



# আগের Lesson 15 — Find Duplicate-এর পরের step শিখব।

# Lesson 15-এ আমাদের কাজ ছিল:
# Duplicate আছে কি না / duplicate value খুঁজে বের করা।

# আজকের কাজ:
# Duplicate বাদ দিয়ে unique values-এর একটি নতুন list তৈরি করা।


# 1️⃣ Problem কী?
"""
ধরি:

arr = [1, 2, 2, 3, 3, 4]

এখানে:

1 → একবার
2 → দুইবার
3 → দুইবার
4 → একবার

আমরা duplicate বাদ দিলে চাই:

[1, 2, 3, 4]

অর্থাৎ প্রতিটি value শুধু একবার থাকবে।

"""



# 2️⃣ Input কী?
# একটি List:
# arr = [1, 2, 2, 3, 3, 4]



# 3️⃣ Output কী?
# Duplicate ছাড়া unique list:
# [1, 2, 3, 4]




# 4️⃣ সবচেয়ে গুরুত্বপূর্ণ বিষয় — Order
"""
আজকের basic problem-এ আমরা original order preserve করব।

Example:

arr = [5, 2, 5, 3, 2]

Expected:

[5, 2, 3]

কারণ:

প্রথম 5 → রাখি
প্রথম 2 → রাখি
দ্বিতীয় 5 → বাদ
প্রথম 3 → রাখি
দ্বিতীয় 2 → বাদ

তাই:

[5, 2, 3]

এখানে শুধু unique করা নয়, first occurrence-এর order ধরে রাখা হচ্ছে।

"""




# 5️⃣ Basic Logic
"""
আগের Lesson 15-এর seen concept এবার আবার ব্যবহার করব।

Pattern:

ARRAY
  ↓
TRAVERSE
  ↓
আগে দেখেছি?
 ↙       ↘
YES       NO
 ↓         ↓
SKIP     RESULT-এ ADD
           ↓
        SET-এ ADD

অর্থাৎ:

আগে দেখা না হলে value রাখব।


"""



## 6️⃣ Set + Result List Approach
arr = [1, 2, 2, 3, 3, 4]
seen = set()
result = []

for x in arr:
   if x not in seen:
      result.append(x)
      seen.add(x)

print(result)


## 
def remove_duplicats(arr):
   seen = set()
   result = []

   for x in arr:
      if x not in seen:
         result.append(x)
         seen.add(x)

   return result

arr = [1, 2, 3, 2, 3, 4, 4]
remove_duplicate = remove_duplicats(arr)
print(remove_duplicate)



# 7️⃣ Code Line by Line
"""
Step 1 — seen
seen = set()

এখানে আমরা রাখব:

কোন values আগে already দেখেছি।

Step 2 — result
result = []

এখানে রাখব:

Duplicate বাদ দেওয়ার পর final unique values।

Step 3 — Traverse
for x in arr:

প্রতিটি element একে একে নিচ্ছি।

Step 4 — Check
if x not in seen:

প্রশ্ন:

এই value কি আগে দেখা হয়নি?

যদি নতুন হয়:

YES → Keep
Step 5 — Result-এ যোগ
result.append(x)

Unique value-টি final list-এ রাখছি।

Step 6 — Seen-এ যোগ
seen.add(x)

এখন থেকে এই value-কে আমরা "already seen" হিসেবে মনে রাখব।

"""




# 8️⃣ 🔥 Dry Run
"""
Input:

arr = [1, 2, 2, 3, 3, 4]

শুরু:

seen = {}
result = []
Step 1
x = 1

Check:

1 not in seen → True

তাই:

result = [1]
seen = {1}
Step 2
x = 2
2 not in seen → True

তাই:

result = [1, 2]
seen = {1, 2}
Step 3

আবার:

x = 2

Check:

2 not in seen → False

তাই কিছুই করব না।

result = [1, 2]
seen = {1, 2}
Step 4
x = 3

নতুন:

result = [1, 2, 3]
seen = {1, 2, 3}
Step 5

আবার 3:

3 in seen → True

তাই skip।

result = [1, 2, 3]
Step 6
x = 4

নতুন:

result = [1, 2, 3, 4]
seen = {1, 2, 3, 4}

শেষে:

[1, 2, 3, 4]

"""



# 9️⃣ Dry Run Table
"""
| Step |  x | `x in seen` | Action | result      |
| ---- | -: | ----------- | ------ | ----------- |
| 1    |  1 | ❌           | Add    | `[1]`       |
| 2    |  2 | ❌           | Add    | `[1,2]`     |
| 3    |  2 | ✅           | Skip   | `[1,2]`     |
| 4    |  3 | ❌           | Add    | `[1,2,3]`   |
| 5    |  3 | ✅           | Skip   | `[1,2,3]`   |
| 6    |  4 | ❌           | Add    | `[1,2,3,4]` |

"""



# 🔟 কেন seen এবং result দুটো লাগছে?
"""

এটা খুব গুরুত্বপূর্ণ।

seen

এটি শুধু check করার জন্য:

x in seen

অর্থাৎ:

আগে দেখেছি কি?

result

এটি final output রাখার জন্য:

result.append(x)

অর্থাৎ:

কোন unique values output-এ থাকবে?

তাই:

seen   → tracking
result → output

"""



# 1️⃣1️⃣ শুধু Set ব্যবহার করলে?
arr = [1, 2, 2, 3, 3, 4]

result = list(set(arr))
print(result)

"""
Output হতে পারে:

[1, 2, 3, 4]

কিন্তু এখানে একটি গুরুত্বপূর্ণ সমস্যা আছে:

Set order preserve করার উদ্দেশ্যে ব্যবহার করা উচিত নয়।

তোমার DSA শেখার জন্য আমরা তাই explicit seen + result approach ব্যবহার করছি।

এতে algorithm-এর logic পরিষ্কার:

Seen?
 ↓
No → Keep
Yes → Skip

এবং input-এর first-occurrence order preserve করা যায়।

"""



# 1️⃣2️⃣ Example — Order বুঝি
"""
Input:

arr = [5, 1, 5, 3, 1, 4]

Process:

5 → Keep
1 → Keep
5 → Skip
3 → Keep
1 → Skip
4 → Keep

Result:

[5, 1, 3, 4]

খেয়াল করো:

Original order:
5 → 1 → 3 → 4

একই আছে।

"""
def remove_duplicates(arr):
   seen = set()
   result = []

   for x in arr:
      if x not in seen:
         result.append(x)
         seen.add(x)

   return result

arr = [5, 1, 5, 3, 1, 4]
result = remove_duplicates(arr)
print(result)




# 1️⃣3️⃣ সব values unique হলে?
# arr = [1, 2, 3, 4]
# কোনো duplicate নেই।

# তাই:
# [1, 2, 3, 4]
# Output input-এর মতোই থাকবে।




# 1️⃣4️⃣ সব values একই হলে?
# arr = [7, 7, 7, 7]

# Process:
# 7 → Keep
# 7 → Skip
# 7 → Skip
# 7 → Skip

# Output:
# [7]




# 1️⃣5️⃣ Empty List
# arr = []

# Loop চলবে না।

# তাই:
# result = []
# Output:
# []




# 1️⃣6️⃣ Negative Number
# arr = [-1, 2, -1, 3, 2]

# Output:
# [-1, 2, 3]

# অর্থাৎ negative number-এর ক্ষেত্রেও একই logic।




# 1️⃣7️⃣ String-এর ক্ষেত্রেও কাজ করবে
"""

এই algorithm শুধু integer-এর জন্য নয়।

arr = ["apple", "banana", "apple", "orange"]

Result:

["apple", "banana", "orange"]

কারণ set strings-ও track করতে পারে।
"""

def remove_duplicates(arr):
   seen = set()
   result = []

   for x in arr:
      if x not in seen:
         result.append(x)
         seen.add(x)

   return result

arr = ["apple", "banana", "apple", "orange"]
print(remove_duplicates(arr))




# 1️⃣8️⃣ Time Complexity
"""
আমরা:

for x in arr:

দিয়ে পুরো array একবার traverse করছি।

তাই traversal:

O(n)

প্রতিটি element-এর জন্য:

x in seen

Set membership average case:

O(1)

এবং:

seen.add(x)

average:

O(1)

তাই মোট:

Time Complexity = O(n)

"""



# 1️⃣9️⃣ Space Complexity
"""
আমরা দুটি extra structure ব্যবহার করছি:

seen = set()
result = []

Worst case-এ যদি সব element unique হয়:

seen → n elements
result → n elements

তাই:

Space Complexity = O(n)

"""



# 2️⃣0️⃣ 🔥 Time-Space Tradeoff আবার
"""

Lesson 15-এ দেখেছিলাম:

Brute Force
Time  = O(n²)
Space = O(1)

Set approach:

Time  = O(n)
Space = O(n)

আজও একই ধারণা:

Extra memory ব্যবহার করে দ্রুত lookup করা হচ্ছে।

"""



# 2️⃣1️⃣ একটি গুরুত্বপূর্ণ Difference
"""
Lesson 15:

Find Duplicate

প্রশ্ন:

Duplicate পাওয়া গেছে?

তাই:

if x in seen:
    return x

Lesson 16:

Remove Duplicates

প্রশ্ন:

Duplicate না হলে রাখব।

তাই:

if x not in seen:
    result.append(x)
    seen.add(x)

দুটোর relationship:

Find Duplicate
→ Duplicate পেলে STOP

Remove Duplicates
→ Unique হলে KEEP
→ Duplicate হলে SKIP

"""



# 2️⃣2️⃣ 🔥 এই Pattern মনে রাখো
"""
                ARRAY
                  ↓
              TRAVERSE
                  ↓
             Seen before?
              ↙       ↘
            YES        NO
             ↓          ↓
            SKIP       KEEP
                         ↓
                  result.append(x)
                         ↓
                    seen.add(x)

এটা একটি খুব useful Deduplication Pattern।

"""



# 2️⃣3️⃣ Common Mistake ❌
"""
অনেকে এভাবে লিখতে পারে:

def remove_duplicates(arr):
    seen = set()
    result = []

    for x in arr:
        if x not in seen:
            result.append(x)

    return result

এখানে সমস্যা:

seen.add(x)

দেওয়া হয়নি।

ফলে seen সবসময় empty থাকবে।

ধরি:

arr = [1, 1, 1]

প্রতিবার:

1 not in seen → True

হবে।

তাই result হবে:

[1, 1, 1]

❌ Duplicate remove হবে না।

সঠিক:

if x not in seen:
    result.append(x)
    seen.add(x)

"""



# 2️⃣4️⃣ append() কোথায় হবে?
"""

সঠিক:

if x not in seen:
    result.append(x)

কারণ unique value-ই result-এ রাখতে চাই।

যদি ভুল করে:

result.append(x)
if x not in seen:
    seen.add(x)

লিখি, তাহলে duplicate-ও result-এ ঢুকে যাবে।

"""




# 2️⃣5️⃣ Alternative Approach — Check Result
"""
Set ব্যবহার না করে beginner-level approach:

def remove_duplicates(arr):
    result = []

    for x in arr:
        if x not in result:
            result.append(x)

    return result

এটাও কাজ করবে।

Example:

arr = [1, 2, 2, 3, 3]

print(remove_duplicates(arr))

Output:

[1, 2, 3]

কিন্তু এখানে:

x not in result

একটি List membership check।

List-এ membership সাধারণত:

O(n)

তাই পুরো algorithm worst/averageভাবে:

O(n²)

হতে পারে।

"""



# 2️⃣6️⃣ দুই Approach-এর Comparison
"""
| Approach          |         Time | Extra Space | Order                                   |
| ----------------- | -----------: | ----------: | --------------------------------------- |
| `x not in result` |        O(n²) |        O(n) | Preserve                                |
| `seen + result`   | O(n) average |        O(n) | Preserve                                |
| `set(arr)`        | O(n) average |        O(n) | Set-এর ordering semantics-এর ওপর নির্ভর |

"""



# 2️⃣7️⃣ Interview Question 🎤
"""
1. How do you remove duplicates from an array while preserving order?
= I use a set to keep track of the elements I have already seen 
  and a result to preserve the original order.
  While traversing the array, if an element is not in the set, 
  I append it to the result and add it to the set.
  Duplicate elements are skipped.

2. What is the time complexity?
= The time complexity is 0(n) on average because I traverse the array once 
  and set membership checking is 0(1) on average.

3. What is the space complexity?
= The space complexity is 0(n) because the set and 
  the result list can both grow up to n elements.

""" 



# 2️⃣8️⃣ Important English Vocabulary
"""
| English       | বাংলা                          |
| ------------- | ------------------------------ |
| Remove        | বাদ দেওয়া                      |
| Duplicate     | পুনরাবৃত্ত value               |
| Unique        | স্বতন্ত্র                      |
| Preserve      | বজায় রাখা                      |
| Order         | ক্রম                           |
| Skip          | বাদ দিয়ে যাওয়া                 |
| Keep          | রেখে দেওয়া                     |
| Track         | নজরে রাখা                      |
| Deduplication | Duplicate বাদ দেওয়ার প্রক্রিয়া |
| Membership    | Collection-এর মধ্যে থাকা       |

""" 



# 2️⃣9️⃣ 📝 1-Page Interview Note
""" 
🟢 LESSON 16 — REMOVE DUPLICATES

Goal:
Array থেকে duplicate বাদ দিয়ে
unique values তৈরি করা।

Order preserve করতে হবে।

Example:

arr = [1, 2, 2, 3, 3, 4]

Output:
[1, 2, 3, 4]


Optimized Basic Approach:

def remove_duplicates(arr):
    seen = set()
    result = []

    for x in arr:
        if x not in seen:
            result.append(x)
            seen.add(x)

    return result


Pattern:

Traverse
   ↓
Seen?
 ↙    ↘
Yes    No
 ↓      ↓
Skip   Keep
        ↓
 result.append(x)
        ↓
 seen.add(x)


Time:
O(n) average

Space:
O(n)


Important:

seen → tracking
result → final output

Lesson 15:
Find Duplicate
→ Duplicate পেলে return

Lesson 16:
Remove Duplicates
→ Unique হলে keep
→ Duplicate হলে skip


Core Pattern:

Check → Keep/Skip → Track

"""



## Short Paragraph
"""
Removing duplicates from an array means creating a new list that contains each value only once 
while preserving the original order of its first occurrence. 
For example, if the array is [1, 2, 2, 3, 3, 4], the result should be [1, 2, 3, 4]. 
A basic and efficient approach is to use a set called seen to keep track of the values 
we have already encountered and a list called result to store the unique values in their original order. 
While traversing the array, we check whether the current value is already in seen. 
If it is, we skip it; if it is not, we append it to result and then add it to seen. 
This approach takes O(n) time on average because the array is traversed once 
and set membership checking and insertion are O(1) on average, 
while the space complexity is O(n) because both seen and result can grow up to n elements. 
The important pattern is: traverse the array, check whether the value has been seen before, 
keep it if it is new, skip it if it is a duplicate, and track new values in the set. 
This is called a deduplication pattern. 
Unlike Lesson 15, where we stop and return a value when we find a duplicate, 
in Lesson 16 we keep unique values and skip duplicates. The main idea is: Check → Keep/Skip → Track.


বাংলা অর্থ:
একটি array থেকে duplicate বাদ দেওয়া মানে এমন একটি নতুন list তৈরি করা 
যেখানে প্রতিটি value শুধু একবার থাকবে এবং তার প্রথমবার আসার original order বজায় থাকবে। 
যেমন, [1, 2, 2, 3, 3, 4] array-এর result হবে [1, 2, 3, 4]। 
এর জন্য একটি basic এবং efficient approach হলো seen নামে একটি set ব্যবহার করা, 
যেখানে আগে দেখা valueগুলো track করা হবে, এবং result নামে একটি list ব্যবহার করা, 
যেখানে unique valueগুলো original order-এ রাখা হবে। Array traverse করার সময় প্রথমে check করি বর্তমান value-টি seen-এর মধ্যে আগে থেকেই আছে কি না। 
যদি থাকে, তাহলে সেটি duplicate, তাই আমরা সেটিকে skip করি। 
আর যদি না থাকে, তাহলে সেটিকে result-এ append করি এবং seen-এ add করি। 
এই approach-এর average time complexity হলো O(n), কারণ array একবার traverse করা হয় এবং 
set-এর membership checking ও insertion average O(1)। 
Space complexity হলো O(n), কারণ seen এবং result—দুটিই worst case-এ n পর্যন্ত element রাখতে পারে। 
এই algorithm-এর মূল pattern হলো: array traverse করো → value আগে দেখা হয়েছে কি না check করো → 
নতুন হলে রাখো → duplicate হলে skip করো → নতুন value-টি set-এ track করো। 
এটিকে Deduplication Pattern বলা যায়। 
Lesson 15-এ duplicate পাওয়া গেলে আমরা সঙ্গে সঙ্গে সেটি return করে থেমে যেতাম, 
কিন্তু Lesson 16-এ আমাদের লক্ষ্য হলো unique values রাখা এবং duplicate values skip করা। 
মূল ধারণাটি হলো: Check → Keep/Skip → Track।

"""