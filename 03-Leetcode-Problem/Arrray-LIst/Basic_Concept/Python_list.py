

##### Python List কী?
# Python-এর List হলো এমন একটি container যেখানে আমরা একসাথে অনেকগুলো value রাখতে পারি।
# এখানে একটি List-এর ভিতরে ৪টি number আছে।
# প্রতিটি value-এর একটি position থাকে। সেই position-কে আমরা index বলি।
# Python-এ index 0 থেকে শুরু হয়।
numbers = [10, 20, 30, 40]

"""
Value:   10   20   30   40
Index:    0    1    2    3
"""


# 1️⃣ List-এর প্রধান বৈশিষ্ট্য
# ① Ordered:
# List-এর element-এর একটি নির্দিষ্ট order থাকে।
numbers = [10, 20, 30, 40]
# 10 - 20 - 30 - 40 = এই order বজায় থাকে।


# ② Mutable:
# Mutable মানে তৈরি করার পরে List-এর ভিতরের value পরিবর্তন করা যায়।
numbers = [10, 20, 30]
numbers[1] = 50
print(numbers)
# অর্থাৎ List পরিবর্তন করা যায়।


# ③ Duplicate:
# List-এ একই value একাধিকবার থাকতে পারে।
numbers = [10, 20, 20, 30, 40]
# কোনো duplicate automatically remove হবে না।


# ④ Different Data Type:
# একটি List-এ বিভিন্ন ধরনের data রাখা সম্ভব।
data = [10, "Mamun", 3.14, True]
"""
10       → int
"Mamun"  → string
3.14     → float
True     → bool
"""
# DSA problem solving-এর সময় সাধারণত একই ধরনের data নিয়ে কাজ করব:
numbers = [10, 20, 30, 40]
names = ["Mamun", "Rahim", "Karim"]




# 2️⃣ List তৈরি করার Syntax
numbers = [10, 20, 30, 40]
names  = ["Mamun", "karim", "Rahim"]
numbers = [] # List-এর ভিতরে কোনো element নেই। (Empty List)



# 3️⃣ List-এর Length
# List-এ কতগুলো element আছে সেটা জানতে
numbers = [10, 20, 30, 40, 50]
print(len(numbers)) # List-এর মধ্যে মোট কতটি element আছে?



# 4️⃣ List এবং Index
numbers = [10, 20, 30, 40]
print(numbers[0])
print(numbers[1])
print(numbers[2])



# 5️⃣ List কেন DSA-এর জন্য গুরুত্বপূর্ণ?
# DSA journey-তে List খুব গুরুত্বপূর্ণ কারণ LeetCode-এর অনেক problem-এ Array ব্যবহার করা হয়।
"""
numbers = [1, 2, 3, 4, 5]

- Find the maximum number
- Find whether a target exists
- Move all zeroes to the end

LIST
 ↓
INDEX
 ↓
TRAVERSAL
 ↓
COMPARISON
 ↓
MODIFICATION
 ↓
PROBLEM SOLVING
"""


# 6️⃣ Important English Terms
"""
List = তালিকা
Element = উপাদান / item
Index = অবস্থান নম্বর
Ordered = ক্রমানুসারে
Mutable = পরিবর্তনযোগ্য
Duplicate = একই value পুনরাবৃত্তি
Length = মোট element সংখ্যা
Access = কোনো element নেওয়া
Modify = পরিবর্তন করা
Traverse = একে একে সব element দেখা

"""


# 🧠 আজকের Mental Model
"""
Python List
     ↓
Multiple values store করে
     ↓
Ordered
     ↓
Index আছে
     ↓
Mutable
     ↓
Duplicate allowed
     ↓
DSA-তে Array-এর মতো ব্যবহার করি

1. List = multiple values রাখার container
2. List ordered
3. List mutable
4. Duplicate allowed
5. Index starts from 0

"""


num = [1, 2, 3, 4, 5]
print(len(num))
names = ["Mamun", 28, 4.06, True]
print(names)



# 🟢 Short Paragraph
"""
A Python list is an ordered and mutable collection that allows us to store multiple values in a single variable.
Each element in a list has a position called an index, and indexing starts from 0 in Python.
A list can contain  duplicate values and can also different types of data, such as integers, strings, floats, and boolean.
Since lists are mutable, we can change, add, or remove elements after creating them.
Lists are very important in DSA because we often use them like arrays to store data, access elements, traverse through them, compare values, and solve different problems.

"""