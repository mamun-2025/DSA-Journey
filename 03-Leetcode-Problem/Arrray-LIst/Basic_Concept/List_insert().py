

# 1️⃣ insert() কী?
# নির্দিষ্ট index/position-এ একটি element যোগ করার জন্য।
# Syntax: list.insert(index, value)
numbers = [10, 20, 30]

numbers.insert(0, 5)
print(numbers)

# দুটি জিনিস দিতে হয়:
# index → কোথায় যোগ হবে
# value → কী যোগ হবে

##
numbers = [10, 20, 30]

numbers.insert(1, 15)
print(numbers)
"""
Visualize করি

আগে:

Index:   0    1    2
Value:  10   20   30

আমরা:

numbers.insert(1, 15)

করলাম।

15 যাবে index 1-এ।

আগের 20 এবং 30 ডানদিকে সরে যাবে।

Before:

10   20   30
     ↑
   index 1


After:

10   15   20   30
     ↑
   index 1

"""

## 
numbers = [10, 20, 30]

numbers.insert(3, 100)
print(numbers)



# 2️⃣ append() vs insert()
# append()
numbers = [10, 20, 30]

numbers.append(40)
print(numbers)
# সবসময় শেষে যোগ করে:


# insert()
numbers = [10, 20, 30]

numbers.insert(1, 200)
print(numbers)

"""
🧠 Mental Model:

append(value)
      ↓
    শেষে

insert(index, value)
      ↓
 নির্দিষ্ট position

"""



 # 3️⃣Insert করার পরে পুরনো Elements কী হয়?
"""
এটা খুব গুরুত্বপূর্ণ।

ধরো:
numbers = [10, 20, 30, 40]

আমরা:
numbers.insert(1, 15)
করলাম।

তখন:
Before:
Index:   0    1    2    3
Value:  10   20   30   40

15 index 1-এ ঢুকবে।

তাই:
After:
Index:   0    1    2    3    4
Value:  10   15   20   30   40

অর্থাৎ:
20 → right shift
30 → right shift
40 → right shift

এই shifting-এর কারণেই insert() সাধারণত O(n)।
"""



# 4️⃣ Time Complexity
"""
এখন DSA-এর গুরুত্বপূর্ণ অংশ।

numbers.insert(0, 5)
এখানে শুরুতে নতুন element ঢোকাতে হবে।

ধরো:
[10, 20, 30, 40, 50]

5 শুরুতে ঢোকালে:
5, 10, 20, 30, 40, 50

পুরনো elements-গুলোকে shift করতে হবে।
10 → right
20 → right
30 → right
40 → right
50 → right

তাই:
Time Complexity = O(n)

insert() সাধারণত O(n)
যে index-এ insert করো, তার পরে থাকা elements shift করতে হতে পারে।

তাই সাধারণভাবে:
insert() → O(n)

বিশেষ করে:
arr.insert(0, value)

এটি O(n)।

"""



# 5️⃣ append() কেন দ্রুততর?
"""
ধরো:
arr.append(50)
শেষে যোগ হচ্ছে।

সাধারণ ক্ষেত্রে আগের elements shift করার দরকার হয় না।
তাই:

append()
→ O(1) amortized

অন্যদিকে:
arr.insert(0, 50)
শুরুতে যোগ হচ্ছে।

তাই:
insert(0, 50)
→ O(n)

⭐ গুরুত্বপূর্ণ Comparison
Operation	   সাধারণ Complexity
_________      ________________
append(x)	   O(1) amortized
insert(0, x)	O(n)
insert(i, x)	O(n) সাধারণভাবে

"""


# 6️⃣ Insert Return কী করে?
# কারণ insert() list-কে in-place modify করে এবং None return করে।
numbers = [10, 20, 30]

result = numbers.insert(0, 5)
print(result)



# 7️⃣ Negative Index দিয়ে Insert
# এখানে -1 অবস্থানটি শেষ element-এর আগে insert করার effect দেয়।
numbers = [10, 20, 30]

numbers.insert(-1, 50)
print(numbers)



# 8️⃣ Index List-এর Length-এর চেয়ে বড় হলে?
numbers = [10, 20, 30]

numbers.insert(5, 40)
print(numbers)
# তাহলে সাধারণত Python value-টিকে list-এর শেষে যোগ করবে।



# 9️⃣ Empty List-এ Insert
numbers = []

numbers.insert(0, 100)
numbers.insert(1, 200)
print(numbers)



# 🔟 Duplicate Element Insert করা যায়
# List duplicate allow করে।
numbers = [10, 20, 30]

numbers.insert(1, 20)
print(numbers)



# 1️⃣1️⃣insert() + Traversal
numbers = [1, 2, 3]

for i in range(len(numbers)):
   numbers.insert(i, 0)

print(numbers)

# এটা তুমি যেমন ভাবছ তেমন সহজভাবে কাজ করবে না, 
# কারণ list-এর length এবং indexes loop চলার সময় পরিবর্তিত হচ্ছে।
# এ ধরনের mutation problem পরে আমরা আলাদাভাবে practice করব।

names = ["Mamun", "Habib", "Rudro"]

names.insert(1, "Nondita")
print(names)
"""
Real-Life Analogy

ধরো একটি লাইনে:
Rahim → Karim → Hasan

তুমি Karim-এর আগে একজন নতুন মানুষ:
Sakib
দাঁড় করালে:
Rahim → Sakib → Karim → Hasan

Sakib-এর জায়গা তৈরি করতে Karim এবং Hasan-কে এক ধাপ করে পিছনে যেতে হয়েছে।

Python list-এর insert()-ও conceptually একই কাজ করে।
Insert
 ↓
Position তৈরি
 ↓
Existing elements shift
 ↓
New element বসে

"""



# 1️⃣2️⃣ append() vs insert() — Real DSA Meaning
arr = [5, 10, 15, 20, 25]

arr.insert(0, 0)
print(arr)

arr.insert(1, 100)
print(arr)

"""
এই দুইটা operation দেখে list-এর একটি গুরুত্বপূর্ণ property বোঝা যায়।

শেষে কাজ:
arr.append(x)

সাধারণত:
O(1) amortized

শুরুতে কাজ:
arr.insert(0, x)

সাধারণত:
O(n)

কারণ Python list array-like structure হওয়ায় elements shift করতে হয়।

এটাই পরে আমাদের বুঝতে সাহায্য করবে কেন:
Queue-এর জন্য list.pop(0) efficient নয়।

সেখানে deque বেশি উপযোগী।

"""
# Insert 25 at index 2
arr = [5, 10, 15, 20]

arr.insert(2, 25)
print(arr)



# 1️⃣3️⃣ 🎯 Interview Questions
"""
1. What does insert() do?
= insert() adds an element at a specified index in a python list.

2. What is the systax?
= list.insert(index, value)

3. What does insert() return?
= It returns None and modifies the list in place.

4. What is the time complexity of insert()?
= Generally 0(n), because existing element may need to be shifted.

5. Difference between append() and insert()?
= append() adds an element at the end, while insert adds an element at a specified index.


⭐ আজকের Master Note
insert(index, value)
│
├── নির্দিষ্ট index-এ value যোগ করে
│
├── Existing elements shift করতে পারে
│
├── Original list modify করে
│
├── Return value = None
│
└── Time Complexity = O(n) সাধারণভাবে


🔥 সবচেয়ে গুরুত্বপূর্ণ তিনটি operation এখন:
append(x)
→ শেষে যোগ
→ O(1) amortized


pop()
→ শেষে remove
→ O(1) amortized


insert(0, x)
→ শুরুতে যোগ
→ O(n)

"""



# 1️⃣4️⃣ Short Paragraph
"""
The insert() method is used to add a new element at a specific index in a Python list. 
Its's syntax is list.insert(index, value), where the index specifies the position and
the value is the element we want to add.
Unlike append(), which always adds an element to the end of the list,
insert() can add an element at any specified position, such as the beginning or the middle.
When an element is inserted into the middle or beginning of a list,
the existing elements may need to shift to the right to make space for the new element,
so insert() generally takes 0(n) time.
The method modifies the original list in place and returns None.
If the given index is the larger than length of the list, 
the element is added at the end. Therefore, we use insert() 
when we need to add an element at a particular position, 
while append() is usually preferred when we simply want to add an element to the end.


বাংলা অর্থ:
insert() method ব্যবহার করা হয় Python List-এর নির্দিষ্ট index-এ নতুন element যোগ করার জন্য।
এর syntax হলো list.insert(index, value), যেখানে index বলে দেয় কোন position-এ element যোগ হবে 
এবং value হলো যে element-টি আমরা যোগ করতে চাই। 
append() যেখানে সবসময় List-এর শেষে element যোগ করে, সেখানে insert() List-এর শুরুতে, 
মাঝখানে বা যেকোনো নির্দিষ্ট position-এ element যোগ করতে পারে। 
List-এর শুরুতে বা মাঝখানে নতুন element যোগ করলে আগের element-গুলোকে জায়গা তৈরি করার জন্য ডানদিকে shift করতে হতে পারে। 
এই shifting-এর কারণে insert() সাধারণভাবে O(n) time complexity নেয়। 
insert() original List-কে সরাসরি modify করে এবং None return করে। 
আবার দেওয়া index যদি List-এর length-এর চেয়ে বড় হয়, তাহলে element-টি সাধারণত List-এর শেষের দিকে যোগ হয়। 
তাই, কোনো নির্দিষ্ট position-এ element যোগ করতে হলে insert() ব্যবহার করি, 
আর শুধু List-এর শেষে element যোগ করতে হলে সাধারণত append() ব্যবহার করা হয়।

"""