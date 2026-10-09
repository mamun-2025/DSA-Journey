

"""
🟢 Lesson 20 — Array Access, Update & Basic Complexity

আজকের Lesson 20-এ আমরা Array/List-এর operation এবং তাদের Time Complexity একসাথে consolidate করব।

এটা খুব গুরুত্বপূর্ণ কারণ Stage 2-এর পরের LeetCode problem-গুলোতে code লেখার পাশাপাশি তোমাকে বুঝতে হবে:

“এই operation কত দ্রুত?”

আজকের lesson শেষে তুমি একটি Python list-এর common operation দেখে দ্রুত বলতে পারবে—O(1), O(n), নাকি O(n log n)।



1️⃣ আজকের Learning Goal

আজ আমরা শিখব:
Array Access → O(1)
Array Update → O(1)
Search → O(n)
Append → O(1) amortized
Pop Last → O(1) amortized
Pop First → O(n)
Insert Beginning → O(n)
Remove by Value → O(n)
Traversal → O(n)
Reverse → O(n)
Sort → O(n log n)

শেষে একটি Array Complexity Cheat Sheet তৈরি করব।



2️⃣ Array/List Access — O(1)

ধরি:

arr = [10, 20, 30, 40, 50]

আমরা যদি লিখি:

print(arr[3])

Output:

40

এখানে Python সরাসরি index 3-এর element access করতে পারে।

arr[3]
  ↓
index 3
  ↓
40

এখানে পুরো list traverse করার দরকার নেই।

তাই:

Time Complexity = O(1)




3️⃣ কেন Access O(1)?

List-এর index:

index:
  0   1   2   3   4

value:
 10  20  30  40  50

যদি চাই:

arr[4]

Python-কে:

10
20
30
40
50

এক এক করে দেখতে হয় না।

সরাসরি index ব্যবহার করে element access করা যায়।

তাই:

O(1) = Constant Time



4️⃣ গুরুত্বপূর্ণ পার্থক্য
arr[3]

এবং:

for x in arr:
    if x == 40:
        ...

এক জিনিস নয়।

Index দিয়ে Access:
arr[3]
O(1)
Value Search:
40 in arr
O(n)

কারণ 40 কোথায় আছে সেটা আগে থেকে জানা নেই।




5️⃣ Array Update — O(1)

ধরি:

arr = [10, 20, 30, 40]

আমরা লিখলাম:

arr[2] = 100

Result:

[10, 20, 100, 40]

এখানেও index জানা আছে:

index 2
 ↓
30
 ↓
100

তাই:

Time Complexity = O(1)



6️⃣ Access + Update

এই দুইটা খুব ভালোভাবে মনে রাখবে:

arr[index]
→ Access
→ O(1)
arr[index] = value
→ Update
→ O(1)

Interview-এ খুব common প্রশ্ন।



7️⃣ Search — O(n)

ধরি:

arr = [10, 20, 30, 40, 50]

আমরা খুঁজছি:

target = 50

Linear Search:

for x in arr:
    if x == target:
        return True

Worst case-এ:

10 → check
20 → check
30 → check
40 → check
50 → check

৫টি element দেখতে হলো।

তাই:

Time Complexity = O(n)



8️⃣ Search কেন O(n)?

কারণ target-এর position আগে থেকে জানা নেই।

ধরি:

[10, 20, 30, 40, 50]

যদি target:

10

হয় → খুব দ্রুত পাওয়া যায়।

Best case:

O(1)

কিন্তু target যদি শেষ element হয়:

50

তাহলে সবগুলো দেখতে হবে।

Worst case:

O(n)

DSA-তে সাধারণত worst-case complexity report করা হয়।

তাই:

Linear Search = O(n)



9️⃣ Append — O(1) Amortized

ধরি:

arr = [10, 20, 30]

লিখলাম:

arr.append(40)

Result:

[10, 20, 30, 40]

Element শেষে যোগ হচ্ছে।

সাধারণ ক্ষেত্রে:

Append = O(1) amortized



🔟 amortized কেন?

Python list internally একটি dynamic array।

কখনও list-এর allocated space শেষ হয়ে গেলে Python-কে নতুন জায়গা allocate করে existing elements copy করতে হতে পারে।

সেই particular operation expensive হতে পারে।

কিন্তু অনেক append operation-এর average cost ধরলে:

O(1) amortized

তাই interview-এ সবচেয়ে নিরাপদভাবে বলবে:

"append() is O(1) amortized."



1️⃣1️⃣ Pop Last — O(1) Amortized
arr = [10, 20, 30, 40]
arr.pop()

Result:

[10, 20, 30]

শেষ element সরানো হয়েছে।

সাধারণত অন্য elements shift করার দরকার নেই।

তাই:

pop() from end = O(1) amortized



1️⃣2️⃣ Pop First — O(n)

এখন:

arr = [10, 20, 30, 40]

লিখলাম:

arr.pop(0)

Result:

[20, 30, 40]

কিন্তু কী হলো?

প্রথম element 10 সরানোর পর:

20 → index 0
30 → index 1
40 → index 2

Elements shift করতে হয়েছে।

তাই:

pop(0) = O(n)



1️⃣3️⃣ Visualize pop(0)

Before:

index:
  0   1   2   3
  ↓   ↓   ↓   ↓
[10, 20, 30, 40]

10 remove:

20 → 0
30 → 1
40 → 2

After:

[20, 30, 40]

এই shifting-এর কারণেই:

O(n)



1️⃣4️⃣ Insert at Beginning — O(n)

ধরি:

arr = [20, 30, 40]

আমরা চাই:

arr.insert(0, 10)

Result:

[10, 20, 30, 40]

কিন্তু existing elements shift করতে হবে:

20 → 1
30 → 2
40 → 3

তাই:

Insert at beginning = O(n)




1️⃣5️⃣ Append বনাম Insert

এটি খুব গুরুত্বপূর্ণ:

Append
arr.append(50)

শেষে যোগ:

O(1) amortized
Insert beginning
arr.insert(0, 50)

শুরুতে যোগ:

O(n)

কারণ shifting।



1️⃣6️⃣ Remove by Value — O(n)

ধরি:

arr = [10, 20, 30, 40]

লিখলাম:

arr.remove(30)

Python-কে প্রথমে 30 খুঁজতে হবে।

10 → no
20 → no
30 → YES

তারপর remaining elements shift করতে হতে পারে।

তাই:

remove(value) = O(n)



1️⃣7️⃣ Remove বনাম Pop

খুব গুরুত্বপূর্ণ comparison:

Operation	কী দিয়ে কাজ করে	Complexity
pop()	last index	O(1) amortized
pop(i)	index	O(n) generally
remove(x)	value	O(n)

উদাহরণ:

arr.pop()

শেষ element।

arr.pop(2)

index 2।

arr.remove(30)

value 30।



1️⃣8️⃣ Traversal — O(n)

ধরি:

arr = [10, 20, 30, 40, 50]

Code:

for x in arr:
    print(x)

প্রতিটি element একবার visit হচ্ছে।

10
20
30
40
50

তাই:

Traversal = O(n)



1️⃣9️⃣ Reverse — O(n)

Python:

arr.reverse()

অথবা two-pointer:

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

প্রায় n/2 swaps হবে।

Big-O-তে:

n/2
→ O(n)

তাই:

Reverse = O(n)

Auxiliary space:

O(1)

যদি in-place algorithm ব্যবহার করি।



2️⃣0️⃣ Sort — O(n log n)

ধরি:

arr = [40, 10, 30, 20]
arr.sort()

Result:

[10, 20, 30, 40]

Python-এর sorting algorithm Timsort-এর typical/worst-case time complexity:

O(n log n)

তাই DSA-তে আমরা সাধারণভাবে:

Sorting = O(n log n)

ধরি n = 1000।

Sorting সাধারণত linear-এর চেয়ে বেশি কাজ করবে, কিন্তু naive O(n²) sorting-এর তুলনায় বড় input-এ অনেক বেশি efficient হতে পারে।



2️⃣1️⃣ কেন Sort করে Max বের করা ভালো নয়?

ধরি:

arr = [10, 50, 20, 30, 40]

আমাদের শুধু maximum দরকার।

Approach 1 — Traverse
current_max = arr[0]

for x in arr:
    if x > current_max:
        current_max = x

Complexity:

O(n)
Approach 2 — Sort
arr.sort()
maximum = arr[-1]

Complexity:

O(n log n)

যখন শুধু max দরকার, sorting unnecessary।

তাই:

যে কাজ O(n)-এ সম্ভব, শুধু সেই কাজের জন্য O(n log n) sorting করা উচিত নয়।




2️⃣2️⃣ Complete Complexity Table

এটা তোমার Stage 2-এর সবচেয়ে গুরুত্বপূর্ণ table:

Operation	Complexity
arr[i] Access	O(1)
arr[i] = x Update	O(1)
Linear Search	O(n)
x in arr	O(n)
append(x)	O(1) amortized
pop() last	O(1) amortized
pop(i)	O(n) generally
pop(0)	O(n)
insert(0, x)	O(n)
remove(x)	O(n)
Traversal	O(n)
Reverse	O(n)
Sort	O(n log n)



2️⃣3️⃣ 🔥 Pattern দিয়ে মনে রাখো
Direct Index
arr[i]
O(1)
Search
for x in arr:
O(n)
Add at End
arr.append(x)
O(1) amortized
Remove at End
arr.pop()
O(1) amortized
Modify Beginning
arr.insert(0, x)
O(n)
Remove Beginning
arr.pop(0)
O(n)
Sort
arr.sort()
O(n log n)



2️⃣4️⃣ 🔥 কেন Beginning-এ Insert/Remove Slow?

Python List-কে একটি row of boxes হিসেবে ভাবো:

[10][20][30][40]

শুরুতে নতুন element ঢোকাতে হলে:

[5][10][20][30][40]

পুরনোগুলোকে ডানদিকে সরাতে হয়।

তাই:

O(n)

কিন্তু শেষে:

[10][20][30][40][50]

শুধু নতুন জায়গায় element যোগ করলেই হয়।

তাই:

O(1) amortized



2️⃣5️⃣ Array বনাম Linked List — ছোট্ট Connection

এটা এখন শুধু ধারণা হিসেবে রাখো।

Python list-এর:

End append → O(1) amortized
Beginning insert → O(n)

এ কারণেই অন্য data structure যেমন Linked List কিছু নির্দিষ্ট insertion/deletion workload-এর জন্য useful হতে পারে।

তবে Python-এর সাধারণ backend development-এ list অনেক বেশি ব্যবহৃত হবে।

এখন আমাদের লক্ষ্য:

কোন operation কেন O(1) বা O(n), সেটা বোঝা।




2️⃣6️⃣ একটি Combined Example
arr = [10, 20, 30, 40]

x = arr[2]

arr[1] = 100

arr.append(50)

arr.pop()

for number in arr:
    print(number)

Complexity আলাদা করি:

arr[2]
→ O(1)

arr[1] = 100
→ O(1)

arr.append(50)
→ O(1) amortized

arr.pop()
→ O(1) amortized

for number in arr
→ O(n)

সবগুলো sequential।

তাই total:

O(1) + O(1) + O(1) + O(1) + O(n)

Dominant term:

O(n)



2️⃣7️⃣ 🔥 Sequential Complexity আবার মনে রাখো

যদি code হয়:

for x in arr:
    ...

for x in arr:
    ...

তাহলে:

O(n) + O(n)
= O(2n)
= O(n)

Constant বাদ যায়।

কিন্তু:

for x in arr:
    for y in arr:
        ...

হলে:

O(n × n)
= O(n²)



2️⃣8️⃣ Interview Questions 🎤
Q1. What is the time complexity of accessing an element in a Python list by index?

“Accessing an element by index takes O(1) time because Python lists support direct index-based access.”

Q2. What is the complexity of searching for a value in a list?

“Searching for a value in a Python list takes O(n) time in the worst case because we may need to check every element.”

Q3. Why is append() O(1) amortized?

“Python lists are dynamic arrays. Most append operations take constant time, although occasionally the list may need to resize and copy elements. Averaged over many operations, append is O(1) amortized.”

Q4. Why is pop(0) O(n)?

“Removing the first element requires shifting the remaining elements to fill the empty position, so it takes O(n) time.”

Q5. Why is arr[i] = value O(1)?

“The index is already known, so the element can be updated directly without traversing the list.”

Q6. Why is sorting usually O(n log n)?

“Efficient comparison-based sorting algorithms generally require O(n log n) time. Python's built-in list sorting uses Timsort, which has O(n log n) worst-case time.”



📝 2️⃣9️⃣ One-Page Master Note
🟢 LESSON 20 — ARRAY COMPLEXITY

ACCESS
arr[i]
→ O(1)


UPDATE
arr[i] = value
→ O(1)


SEARCH
x in arr
→ O(n)


TRAVERSAL
for x in arr
→ O(n)


APPEND
arr.append(x)
→ O(1) amortized


POP LAST
arr.pop()
→ O(1) amortized


POP BY INDEX
arr.pop(i)
→ O(n) generally


POP FIRST
arr.pop(0)
→ O(n)


INSERT BEGINNING
arr.insert(0, x)
→ O(n)


REMOVE BY VALUE
arr.remove(x)
→ O(n)


REVERSE
arr.reverse()
→ O(n)


SORT
arr.sort()
→ O(n log n)


MAIN RULE:

Known Index
→ O(1)

Need to Search
→ O(n)

Need to Shift Elements
→ O(n)

Need to Sort
→ O(n log n)


Sequential:
O(n) + O(n)
→ O(n)


Nested:
O(n) × O(n)
→ O(n²)


"""