
# 1️⃣ Index কী?
numbers = [10, 20, 30, 40]
numbers[0] # 10
numbers[1] # 20
numbers[2] # 30
numbers[3] # 40
# Python-এ index 0 থেকে শুরু হয়।
# এটাকে বলে:
# Zero-based indexing



# 2️⃣ Position আর Index এক জিনিস নয়
"""
Human Position:  1    2    3    4
                 ↓    ↓    ↓    ↓
Index:           0    1    2    3
                 ↓    ↓    ↓    ↓
Value:          10   20   30   40

মানুষ বলবে:
10 হলো 1st element

কিন্তু Python বলবে:
10 হলো index 0-এ।

তাই:
numbers[0]
দিলে প্রথম element পাওয়া যাবে।
"""
numbers = [10, 20, 30]
print(numbers[0])



# 3️⃣ Positive Indexing
# বাম দিক থেকে index করলে তাকে positive indexing বলতে পারি।
numbers = [10, 20, 30, 40]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])



# 4️⃣ Negative Indexing
# ডান দিক থেকে index করলে তাকে Negative indexing বলতে পারি।
numbers = [10, 20, 30, 40]
print(numbers[-1]) # 40
print(numbers[-2]) # 30
print(numbers[-3]) # 20
print(numbers[-4]) # 10
"""
Positive Index:
Index:     0    1    2    3
           ↓    ↓    ↓    ↓
Value:    10   20   30   40

Negative Index:
Index:    -4   -3   -2   -1
           ↓    ↓    ↓    ↓
Value:    10   20   30   40
"""



# 5️⃣ Index দিয়ে Element Access
numbers = [10, 20, 30, 40]
first = numbers[0]
print(first)

last = numbers[-1]
print(last)



# 6️⃣ Index দিয়ে Element Modify করা
numbers = [10, 20, 30, 40]
numbers[1] = 50
print(numbers)



# 7️⃣ Index দিয়ে Data Update করার Pattern
# list[index] = new_value
num = [10, 20, 30, 40]
num[2] = 300
print(num)



# 8️⃣ Index Out of Range
numbers = [10, 20, 30]
# print(numbers[3])
"""
IndexError: list index out of range
কারণ index 4 নেই।
"""

# Remember
# যদি list-এর length হয় n, তাহলে positive index:
# 0 from n-1
num = [10, 20, 30, 40]
print(len(num)) # length = 4

# But index = n-1 = 4-1 =3
index = len(num) - 1
print(index)



# 9️⃣ কেন list[index] O(1)?
numbers = [10, 20, 30, 40, 50]
numbers[3]
# Python-কে:
# 10 → 20 → 30 → 40
# এভাবে একটার পর একটা search করতে হয় না।
# Index ব্যবহার করে সরাসরি নির্দিষ্ট element access করা যায়।
# Time Complextiy = 0(1)
# Python list supports direct access by index, so accessing arr[i] takes 0(1).

"""
ধরো একটি apartment building:

Room 0 → Rahim
Room 1 → Karim
Room 2 → Hasan
Room 3 → Sakib

তুমি যদি বলো:
আমাকে Room 2-এর মানুষকে দেখাও।

তাহলে পুরো building search করতে হবে না।
সরাসরি:
Room 2 → Hasan

ঠিক একইভাবে:
people[2]
দিয়ে সরাসরি index 2-এর element পাওয়া যায়।
"""
people = ["Mamun", "Rahim", "Hasan", "Karim"]
print(people[2] )


# 🧠 1-Page Note
"""
Python List Indexing
────────────────────
List:
numbers = [10, 20, 30, 40]

Positive Index:
0 → 10
1 → 20
2 → 30
3 → 40

Negative Index:
-4 → 10
-3 → 20
-2 → 30
-1 → 40

Access:
numbers[2] → 30

Modify:
numbers[2] = 100

Result:
[10, 20, 100, 40]

Invalid:
numbers[4] → IndexError

Complexity:
arr[i] → O(1)


1. Python List index starts from 0.
2. arr[0] → first element.
3. arr[-1] → last element.
4. arr[index] = value → element update.
5. arr[i] → O(1) direct access.
"""


# 🎯 7-Step Problem Solving Connection
"""
Array/List problem দেখলে এখন প্রথমে ভাববে:

1. Input কী?
arr = [10, 20, 30, 40]

2. Output কী?
ধরো last element:
40

3. Logic কী?
arr[-1]

4. Dry Run
arr[-1]
 ↓
last element
 ↓
40

5. Time Complexity
O(1)

6. Space Complexity
O(1)

7. Interview Explanation
I use the index to directly access the required element. 
Python lists support constant-time index access, 
so the time complexity is O(1).

"""


# 🟢 Short Paragraph
"""
List indexing is the way we access a specific element from a Python List.
Python uses zero-based indexing, which means the first element has index 0,
the second has index 1, and so on.
We can access the element using the syntax list[index], and Python also supports negative indexing, 
where -1 refers to the last element, -2 to the second-last element, and so on.
Since lists are mutable, we can also modify an element by assigning a new value to a specific index.
If we try to access an index that does not exist, Python raises an IndexError.
List elements can be accessed directly by their index,
so accessing an element such as arr[i] generally takes 0(1) constant time.

বাংলা অর্থ:
List indexing হলো Python List-এর নির্দিষ্ট কোনো element access করার পদ্ধতি। 
Python zero-based indexing ব্যবহার করে, যার অর্থ প্রথম element-এর index হলো 0, 
দ্বিতীয়টির 1, এভাবে পরবর্তী element-এর index বাড়তে থাকে। 
আমরা list[index] syntax ব্যবহার করে কোনো element access করতে পারি। 
Python-এ negative indexing-ও রয়েছে, যেখানে -1 দিয়ে শেষের element, 
2 দিয়ে দ্বিতীয় শেষের element এবং এভাবে পিছনের দিক থেকে element access করা যায়। 
যেহেতু List mutable, তাই নির্দিষ্ট index-এ নতুন value assign করে কোনো element পরিবর্তনও করা যায়। 
যদি এমন কোনো index access করার চেষ্টা করি যেটি List-এর মধ্যে নেই, তাহলে Python IndexError দেখায়। 
Index ব্যবহার করে List-এর element সরাসরি access করা যায়, 
তাই arr[i]-এর মতো কোনো element access করতে সাধারণত O(1) constant time লাগে।

"""