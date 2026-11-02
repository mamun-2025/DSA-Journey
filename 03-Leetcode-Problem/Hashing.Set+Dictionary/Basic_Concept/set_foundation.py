

# 1️⃣ Set কী?
# Python-এর Set হলো এমন একটি collection যেখানে unique values রাখা হয়।
numbers = {10, 20, 20, 30}
result = set(numbers) # তাহলে Set duplicate রাখবে না।
print(result)


# 2️⃣ List বনাম Set
# List
# Duplicate থাকতে পারে:
numbers = [10, 20, 10, 30]

# Set
# Duplicate not supported(unique value/fast lookup)
numbers = {10, 20, 30}
"""
| Feature         | List              | Set |

| Duplicate       | ✅ Allowed       | ❌ Not stored |
| Index           | ✅ Yes           | ❌ No |
| Ordered sequence | ✅ Yes          | Set-কে index-based ordered sequence হিসেবে ব্যবহার করা যায় না |
| Membership      | O(n)             | O(1) average |
| Main purpose    | Sequence         | Unique values / fast lookup |

"""


"""
3️⃣ Set-এর Main Purpose
Set-এর সবচেয়ে গুরুত্বপূর্ণ ব্যবহার:

Membership checking

অর্থাৎ:
“এই value-টা কি এখানে আছে?”

Example:
seen = {10, 20, 30}

Check:
20 in seen

Output:
True

আর:
50 in seen

Output:
False

"""


# 4️⃣ 🔥 List Search বনাম Set Search
# এটা আজকের সবচেয়ে গুরুত্বপূর্ণ concept।

# List Membership checking
numbers = [10, 20, 30, 40, 50]
if 50 in numbers:
   print("found")

# Python-কে list-এর মধ্যে search করতে হতে পারে:
# 10 → 20 → 30 → 40 → 50

# তাই:
# List membership = O(n)


# Set Membership checking
numbers = {10, 20, 30, 40, 50}
if 50 in numbers:
   print("found")

# Set-এর hash-based lookup ব্যবহার করে সাধারণ ক্ষেত্রে দ্রুত membership checking করা যায়।

# তাই:
# Set membership = O(1) average
# 🔥 এই difference-টাই Hashing-এর মূল শক্তি।


# 5️⃣ Set তৈরি করার দুটি উপায়
# Method 1 — Curly Braces
numbers = {10, 20, 30}

# Method 2 - set()
numbers = set()
# এটি একটি empty set তৈরি করে।



# 6️⃣ ⚠️ {} কেন Empty Set নয়?
# {}       → Empty Dictionary
# set()    → Empty Set

# Empty Dictionary
data = {}

# Empty Set:
data = set()



# 7️⃣ Set-এ Element Add করা
numbers = set()

numbers.add(10)
numbers.add(20)
numbers.add(30)

print(numbers)



# 8️⃣ Duplicate Add করলে কী হয়?
numbers = {10, 20, 30}
numbers.add(20)
print(numbers)
"""
কোনো error হবে না।
Set-এর মধ্যে 20 আগে থেকেই আছে।

তাই:
{10, 20, 30}

এই concept খুব গুরুত্বপূর্ণ।

“Set বলে: আমি একই value দ্বিতীয়বার আলাদা element হিসেবে রাখব না।”
"""



# 9️⃣ add() Example
data = set()

data.add(5)
data.add(10)
data.add(5)

print(data)
# 5 দুইবার add করার চেষ্টা করা হলেও একবারই থাকবে।
seen = set()

seen.add(5)
seen.add(10)
seen.add(5)

print(seen)


# 🔟 Set Membership — in
seen = {10, 20, 30}

print(50 in seen)
print(10 in seen)


# 1️⃣1️⃣ not in
# আমরা উল্টোটাও করতে পারি:
seen = {10, 20, 30}

if 10 in seen:
   print("10 is present")

##
seen = {100, 200, 300}

if 500 not in seen:
   print("500 is not present.")



# 1️⃣2️⃣ remove()
numbers = {10, 20, 30}

numbers.remove(20)
print(numbers)


"""
1️⃣3️⃣ ⚠️ remove()-এর গুরুত্বপূর্ণ বিষয়

যদি value Set-এর মধ্যে না থাকে:
numbers = {10, 20, 30}numbers.remove(50)

তাহলে:
KeyError
হবে।

তাই uncertainty থাকলে remove() সবসময় safest choice নয়।

"""


# 1️⃣4️⃣ discard() — Safe Remove
numbers = {10, 20, 30}

numbers.discard(30)
print(numbers)


# এখন value না থাকলেও:
# কোনো error হবে না।
numbers.discard(50)
print(numbers)

# তাই:
# remove()
# → Missing value হলে error

# discard()
# → Missing value হলেও no error



"""
1️⃣5️⃣ remove() vs discard():

Method	      Value থাকলে	      Value না থাকলে
remove(x)	   Remove	         KeyError
discard(x)	   Remove	         Nothing happens

"""



# 1️⃣6️⃣ len()
## Set
numbers = {10, 20, 30}
print(len(numbers))

# Duplicate থাকলেও unique element count হবে:
numbers = {10, 10, 20, 20, 30}
print(len(numbers))


## List 
numbers = [10, 20, 30, 40, 50]
print(len(numbers))

# Duplicate থাকলেও all element count হবে:
numbers = [10, 10, 20, 20]
print(len(numbers))



# 1️⃣7️⃣ clear()
numbers = {10, 20, 30}

numbers.clear()
print(numbers)

empty_set = numbers.clear()
print(empty_set)



# 1️⃣8️⃣ Set Traversal
# Set-এর elements iterate করা যায়:

numbers = {10, 20, 30}

for number in numbers:
   print(number)

# result = numbers[0]
# print(result)
# Set-কে list-এর মতো index-based sequence হিসেবে ব্যবহার করবে না।
# করলে error হবে।
# কারণ Set-এ list-এর মতো index access নেই।


# List 
numbers = [10, 20, 30]

for number in numbers:
   print(number)

# List index-based
numbers = [100, 200, 300, 400]

index = numbers[0]
print(index)

index = numbers[1]
print(index)



# 1️⃣9️⃣ কেন Set-এ Index নেই?
numbers = [10, 20, 30]

"""
এখানে:
index:
  0   1   2

তাই:
numbers[1]
possible।

কিন্তু Set-এর মূল উদ্দেশ্য:
Unique values
+
Fast membership

Index-based access নয়।

তাই:
numbers = {10, 20, 30}numbers[1]
করবে না।

"""



"""
2️⃣0️⃣ 🔥 Set-এর Order নিয়ে গুরুত্বপূর্ণ কথা
Set-কে sequence order-এর জন্য ব্যবহার করবে না।

যেমন:
numbers = {30, 10, 20}


তুমি Set-এর iteration দেখে কোনো নির্দিষ্ট list-style order ধরে algorithm লিখবে না।

তোমার মূল concern হবে:
Is this value present?

এবং:
Is this value unique?

"""
numbers = {30, 10, 20}

if 20 in numbers:
   print("20 is present")

numbers = {10, 10, 20, 30, 30}

if 20 in numbers:
   print("20 is unique")



# 2️⃣1️⃣ Set-এর মূল চারটি প্রশ্ন
# একটি Set দেখলে নিজেকে জিজ্ঞেস করবে:
seen = {1, 2, 3, 4, 5}

2 in seen
print("Yes -2 in seen.")

if 10 not in seen:
   print("Yes- 10 not in seen. ")

seen.add(6)
print(seen)

seen.remove(1)
print(seen)

seen.discard(6)
print(seen)



"""
2️⃣2️⃣ Set Complexity
এখন complexity।

সাধারণভাবে Python Set-এর জন্য:
Operation	      Average Complexity
x in set	         O(1)
x not in set	   O(1)
add(x)	         O(1) average
remove(x)	      O(1) average
discard(x)	      O(1) average
len(set)	         O(1)
clear()	         O(n)

Interview-এ in, add, remove নিয়ে সাধারণত বলবে:
Average O(1)

"""



"""
2️⃣3️⃣ কেন Average O(1)?

এখানে আসে Hashing।
Set internally hash-based structure ব্যবহার করে।

ধারণাটা খুব সহজভাবে:
Value
  ↓
Hash Function
  ↓
Hash
  ↓
Location/Bucket

তাই Python-কে সাধারণ list-এর মতো:
10
20
30
40
50
...

এক এক করে search করতে হয় না।
এ কারণে average case-এ membership খুব দ্রুত।




2️⃣4️⃣ Hashing এখন কতটুকু বুঝলেই হবে?

এখন তোমার শুধু এই concept বুঝলেই যথেষ্ট:
List
 ↓
Search
 ↓
O(n)

Set
 ↓
Hash-based lookup
 ↓
Average O(1)

এখনই hash table-এর internal implementation মুখস্থ করার দরকার নেই।
পরের Dictionary lessons-এ hashing আরও পরিষ্কার হবে।



2️⃣5️⃣ 🔥 Set দিয়ে Duplicate Detection

এখন আসি আমাদের প্রথম LeetCode problem-এ।
LeetCode 217 — Contains Duplicate
Problem-এর মূল প্রশ্ন:
Array-তে কোনো value একাধিকবার আছে কি না?

Example:
nums = [1, 2, 3, 1]


এখানে:
1

দুইবার এসেছে।

তাই:
True

"""


# 2️⃣6️⃣ Brute Force Approach
def contains_duplicate(nums):
   for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
         if nums[i] == nums[j]:
            return True 

   return False

# omplexity:
# Time  → O(n²)
# Space → O(1)
# কাজ করে, কিন্তু বড় array হলে expensive।



# 2️⃣7️⃣ Set দিয়ে Optimization
def contains_duplicate(nums):
   seen = set()

   for num in nums:
      if num in seen:
         return True

      seen.add(num)

   return False



"""
2️⃣8️⃣ Code Line by Line
Line 1
seen = set()


একটি empty Set তৈরি করলাম।

এর কাজ:
যে values আমরা ইতিমধ্যে দেখেছি সেগুলো মনে রাখা।

Line 2
for num in nums:


Array traverse করছি।
Line 3
if num in seen:


প্রশ্ন:
“এই number-টা কি আগে দেখেছি?”

যদি Yes:
Duplicate found

তাই:
return True


Line 4
যদি আগে না দেখে থাকি:
seen.add(num)


অর্থাৎ:
“এখন থেকে এই number-টাকে seen হিসেবে মনে রাখো।”



2️⃣9️⃣ 🔥 Dry Run
Input:
nums = [1, 2, 3, 1]


Start:
seen = {}

Step 1
num = 1

Check:
1 in seen


False।

তাই:
seen.add(1)


এখন:
seen = {1}

Step 2
num = 2

Check:
2 in {1}


False।

Add:
{1, 2}

Step 3
num = 3

Check:
3 in {1, 2}

False।

Add:
{1, 2, 3}

Step 4
num = 1

Check:
1 in {1, 2, 3}


True!

তাহলে:
return True


আমরা সঙ্গে সঙ্গে answer পেয়ে গেলাম।



3️⃣0️⃣ Early Return
এখানে একটি গুরুত্বপূর্ণ concept আছে:
if num in seen:    return True


Duplicate পাওয়া মাত্র আমরা পুরো array traverse করি না।

এটাকে বলা যায়:
Early Return / Early Exit

Example:
[1, 2, 3, 1, 5, 6, 7, 8, 9]

চার নম্বর element-এই duplicate পাওয়া গেছে।

তাই পরে:
5, 6, 7, 8, 9

check করার দরকার নেই।



3️⃣1️⃣ Duplicate না থাকলে কী হবে?
Input:
nums = [1, 2, 3, 4]


Dry run:
1 → add
2 → add
3 → add
4 → add

শেষে:
seen = {1, 2, 3, 4}

Loop শেষ।

তাই:
return False




3️⃣2️⃣ Complexity — Contains Duplicate
প্রতিটি element-এর জন্য:
num in seen


Average:
O(1)

এবং:
seen.add(num)


Average:
O(1)

Array-এর n elements traverse করতে হতে পারে।

তাই:
Time = O(n) average

Set-এ সর্বোচ্চ n unique values থাকতে পারে।

তাই:
Space = O(n)



3️⃣3️⃣ Brute Force vs Hash Set
এটা তোমার notebook-এর জন্য খুব গুরুত্বপূর্ণ:
Approach	Time	Space
Nested Loop	O(n²)	O(1)
Hash Set	O(n) average	O(n)


এখানে:
O(n²)
   ↓
Use extra memory
   ↓
Set
   ↓
O(n) average

এটাই:
⚖️ Time-Space Tradeoff
আমরা অতিরিক্ত space ব্যবহার করে time কমিয়েছি।

"""



"""
3️⃣4️⃣ Pattern Name
এই pattern-এর নাম:
⭐ Seen Set Pattern
Template:
seen = set()for x in arr:    if x in seen:        # already seen        ...    seen.add(x)


এটি মুখস্থ করার চেয়ে logic বুঝবে:
Current value
      ↓
Already seen?
   ↙       ↘
 YES       NO
  ↓         ↓
Duplicate  Add to seen



3️⃣5️⃣ seen.add() আগে করলে কী সমস্যা?
খুব common beginner mistake:
seen = set()for num in nums:    seen.add(num)    if num in seen:        return True


এটা ভুল।

কেন?

প্রথম element:
num = 1

প্রথমে:
seen.add(1)


তারপর check:
1 in seen


অবশ্যই True!

তাহলে প্রথম element-কেই duplicate মনে করবে।




3️⃣6️⃣ সঠিক Order
সবসময়:
1. Check
2. Then Add

অর্থাৎ:
if num in seen:    return Trueseen.add(num)


🔥 এই order মনে রাখবে।




3️⃣7️⃣ set() কেন seen নামে?
এটা শুধু variable name।

তুমি লিখতে পারো:
visited = set()


অথবা:
unique_values = set()


কিন্তু DSA-তে:
seen = set()


খুব common এবং readable।

seen মানে:
Already encountered / আগে দেখা হয়েছে।





3️⃣8️⃣ Interview Explanation 🎤
Q: Why did you use a Set?
বলবে:
“I use a Set to keep track of the elements I have already seen. Set provides average O(1) membership lookup, so I can detect duplicates efficiently.”

Q: Explain your approach.
“I traverse the array once and maintain a Set called seen. For each element, I first check whether it is already in the Set. If it is, I return True because a duplicate exists. Otherwise, I add it to the Set. If the traversal finishes without finding a duplicate, I return False.”

Q: Complexity?
“The average time complexity is O(n), because each element is checked and inserted into the Set in average O(1) time. The space complexity is O(n) because the Set can store up to n unique elements.”



3️⃣9️⃣ Important English Vocabulary
English	বাংলা
Set	Unique collection
Unique	অনন্য / duplicate নয়
Duplicate	পুনরাবৃত্ত value
Membership	কোনো collection-এ থাকা
Lookup	খুঁজে দেখা
Hash	Hash value
Seen	আগে দেখা
Add	যোগ করা
Remove	সরানো
Discard	নিরাপদে remove
Empty	খালি
Collision	একই hash location-এ একাধিক value
Average	গড়
Constant Time	O(1)
Efficient	কার্যকর / দ্রুত
Duplicate Detection	Duplicate শনাক্তকরণ

"""