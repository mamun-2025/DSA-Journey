

# Leetcode Problem
# Binary_search
class Solution:
   def search(self, nums: list[int], target: int)-> int:
      left = 0
      right = len(nums) - 1 

      while left <= right:
         mid = (left + right) // 2

         if nums[mid] == target:
           return mid  

         elif nums[mid] < target:
            left = mid + 1 

         else:
            right = mid - 1 

      return -1



numbers = [-1, 0, 3, 5, 9, 12]
solution = Solution()
result = solution.search(numbers, 9)
print(result)


"""
I use binary search on the sorted array.
I maintain left and right boundaries and calculate the middle index.
If the middle value equals the target, I return its index.
If it is smaller, I search the right half;
otherwise, I search the left half.
The gives 0(log n) time and 0(1) space.

"""



# 1️⃣ Linear Search কী?
# এক লাইনে / একটার পর একটা।
# Linear Search-এ আমরা List-এর elementগুলোকে শুরু থেকে শেষ পর্যন্ত একে একে check করি।
numbers = [10, 20, 30, 40, 50]
target = 30

"""
আমরা এভাবে খুঁজব:

10 → 20 → 30
          ↑
        Found!

অর্থাৎ:

প্রথম element
      ↓
দ্বিতীয় element
      ↓
তৃতীয় element
      ↓
...
      ↓
target পাওয়া গেছে

"""


# 2️⃣ Problem কী?
"""

আমাদের একটি array/list দেওয়া থাকবে:

numbers = [10, 20, 30, 40, 50]

এবং একটি target:

target = 30

আমাদের কাজ:

30 list-এর মধ্যে আছে কি না খুঁজে বের করা।

"""



# 3️⃣ Input কী?
"""
দুটি জিনিস:

Array/List
Target

Example:

numbers = [10, 20, 30, 40, 50]
target = 30

"""



# 4️⃣ Output কী?
"""

এখানে দুই ধরনের output হতে পারে।

Option 1 — Found / Not Found
Found

অথবা:

Not Found
Option 2 — Index return করা
2

কারণ:

index:    0   1   2   3   4
          ↓   ↓   ↓   ↓   ↓
numbers: 10  20  30  40  50
                  ↑
               target

Python-এ index 2।

DSA-তে আমরা সাধারণত index return করার version শিখব।

"""



# 5️⃣ Basic Logic
"""
আমাদের logic খুব simple:

Start
  ↓
প্রথম element check
  ↓
target-এর সাথে compare
  ↓
মিলে গেলে index return
  ↓
না মিললে next element
  ↓
শেষ পর্যন্ত search
  ↓
না পেলে -1 return

এখানে -1 সাধারণত বোঝায়:

Target পাওয়া যায়নি।

"""



# 6️⃣ Basic Code
numbers = [10, 20, 30, 40, 50]
target = 30

for i in range(len(numbers)):
   if numbers[i] == target:
      print(i)

## Index 
def linear_search(arr, target):
   for i in range(len(arr)):
      if arr[i] == target:
         return i

   return -1


numbers = [10, 20, 30, 40, 50]
result = linear_search(numbers, 30)
print(result)



# 7️⃣ Code Line by Line
"""
Step 1
def linear_search(arr, target):

Function দুইটি input নেয়:
arr
target

Step 2
for i in range(len(arr)):

এখানে আমরা index দিয়ে traverse করছি।

যদি:
arr = [10, 20, 30, 40]

তাহলে:
i = 0
i = 1
i = 2
i = 3

Step 3
if arr[i] == target:
বর্তমান index-এর value target-এর সমান কিনা check করছি।

Step 4
return i
যদি target পাওয়া যায়, সঙ্গে সঙ্গে index return করছি।
এখানে গুরুত্বপূর্ণ বিষয়: return হওয়ার পর loop আর চলবে না।

Step 5
return -1
পুরো list search করার পরও target না পাওয়া গেলে:
-1
return করবে।

"""



# 8️⃣ 🔥 Dry Run
"""
ধরি:
arr = [10, 20, 30, 40, 50]
target = 40

আমাদের code:
for i in range(len(arr)):
    if arr[i] == target:
        return i

Dry Run:
i	arr[i]	arr[i] == 40
0	10	❌
1	20	❌
2	30	❌
3	40	✅

এখন:
return 3

Output:
3

"""



# 9️⃣ Target প্রথমেই থাকলে?
def linear_search(arr, target):
   for i in range(len(arr)):
      if arr[i] == target:
         return i 

   return -1

numbers = [50, 40, 30, 20, 10]
result = linear_search(numbers, 50)
print(result)

"""
Dry Run:

i = 0
arr[0] = 50
50 == 50
      ↓
    True
      ↓
 return 0

Output:

0
এখানে পুরো list traverse করতে হয়নি।
"""



# 🔟 Target একদম শেষে থাকলে?
"""
arr = [10, 20, 30, 40, 50]
target = 50

আমাদের check করতে হবে:

10 ❌
20 ❌
30 ❌
40 ❌
50 ✅

তাই:

4
"""



# 1️⃣1️⃣ Target না থাকলে?
"""
arr = [10, 20, 30, 40]
target = 50

সবগুলো check হবে:

10 ❌
20 ❌
30 ❌
40 ❌

শেষে:

return -1

Output:

-1
"""



# 1️⃣2️⃣ কেন -1?
"""

Python list-এর valid index:

0, 1, 2, 3, ...

-1 কিন্তু Python-এ valid index হিসেবে ব্যবহার করলে last element বোঝায়:

arr[-1]

তবে search function-এর return value হিসেবে -1 ব্যবহার করা একটি common convention:

return -1
→ target not found

এখানে context অনুযায়ী বুঝতে হবে যে আমরা -1-কে special signal হিসেবে ব্যবহার করছি, index হিসেবে নয়।
"""




# 1️⃣3️⃣ Alternative: Value Return
# কখনো আমাদের index দরকার নেই। শুধু জানতে চাই:
# target আছে কি না?
def linear_search(arr, target):
   for i in range(len(arr)):
      if arr[i] == target:
         return True

   return False

numbers = [10, 20, 30, 40]
result = linear_search(numbers, 20)
print(result)




# 1️⃣4️⃣ Index Search vs Boolean Search
# Target-এর position দরকার	= index
# শুধু আছে কি না দরকার = True/False
# Interview/DSA problem অনুযায়ী version নির্বাচন করবে।




# 1️⃣5️⃣ Python-এর in Operator
# Python-এ খুব সহজে লিখতে পারি:
arr = [10, 20, 30, 40]
print(30 in arr)
print(50 in arr)



# 1️⃣6️⃣ index() Method
arr = [10, 20, 30, 40]
index = arr.index(30)
print(index)
# কিন্তু target না থাকলে:
# arr.index(50)
# ValueEror হবে।
# তাই DSA শেখার সময় manual implementation বোঝা গুরুত্বপূর্ণ।




# 1️⃣7️⃣ Duplicate থাকলে কী হবে?
arr = [10, 20, 30, 20, 40]
target = 20

def linear_search(arr, target):
   for i in range(len(arr)):
      if arr[i] == target:
         return i 

   return -1

result = linear_search(arr, target)
print(result)

# প্রথম 20 পাওয়া যাবে:
# index 1

# তাই output:
# 1
# কেন index 3 নয়?
# কারণ আমরা first occurrence পেলেই return করছি।



# 1️⃣8️⃣ যদি সব occurrence দরকার হয়?
def linear_search(arr, target):
   result = []

   for i in range(len(arr)):
      if arr[i] == target:
         result.append(i)

   return result

arr = [10, 20, 10, 30, 10]
target = 10
res = linear_search(arr, target)
print(res)



# 1️⃣9️⃣ 🔥 Time Complexity
"""
এটাই আজকের সবচেয়ে গুরুত্বপূর্ণ অংশ।

ধরি array-এর size:
n

Best Case:
Target প্রথম element-এই পাওয়া গেল।

[10, 20, 30, 40]
 ↑
target

শুধু ১টি element check করতে হলো।

তাই:
Best Case = O(1)


Worst Case:
Target একদম শেষে আছে অথবা target নেই।

10 → 20 → 30 → 40 → 50
                     ↑

সব n elements check করতে হবে।

তাই:
Worst Case = O(n)


Average Case:
সাধারণভাবে target মাঝামাঝি কোথাও পাওয়া যেতে পারে।

তবুও complexity:
Average Case = O(n)
কারণ Big-O-তে linear growth হিসেবে ধরা হয়।

"""



# 2️⃣0️⃣ Complexity Summary
"""
Case	Time
Best	O(1)
Average	O(n)
Worst	O(n)

Space:
O(1)

কারণ আমরা অতিরিক্ত বড় কোনো data structure ব্যবহার করছি না।
"""



# 2️⃣1️⃣ কেন Linear Search O(n)?
"""
ধরি:
arr = [10, 20, 30, 40, 50, 60]

Target:
60

তাহলে:
1 → 10
2 → 20
3 → 30
4 → 40
5 → 50
6 → 60

৬টি element → ৬টি check।

যদি n = 1,000,000 হয় এবং target শেষে থাকে, প্রায় 1,000,000 element check করতে হতে পারে।

তাই:
O(n)

"""


# 2️⃣2️⃣ Linear Search কি Sorted Array-এর জন্যই?
"""
না।

এটাই Linear Search-এর একটি সুবিধা।

এটি sorted বা unsorted—দুই ধরনের list-এই কাজ করে।

Example:

[50, 10, 90, 20, 5]

এখানেও Linear Search কাজ করবে।

কিন্তু sorted array থাকলে আমরা পরবর্তীতে Binary Search ব্যবহার করতে পারি, যা অনেক ক্ষেত্রে:

O(log n)

সময় নিতে পারে।
"""




# 2️⃣3️⃣ Linear Search বনাম Binary Search
"""
আজ শুধু basic comparison:

Feature	      Linear Search	  Binary Search

Search method	 একে একে	      মাঝখান থেকে
Sorted required?	❌ না	      ✅ সাধারণত হ্যাঁ
Best	           O(1)	       O(1)
Worst	           O(n)	       O(log n)
সহজতা	         সহজ	       তুলনামূলক complex

Binary Search আমরা পরে আলাদাভাবে গভীরভাবে শিখব।
"""



# 2️⃣4️⃣ 🔥 Real-Life Example
"""

ধরো একটি বইয়ের shelf-এ ১০০টি বই আছে এবং তুমি "Python" বইটি খুঁজছ।

তুমি যদি একটার পর একটা বইয়ের নাম দেখো:
Book 1 → Python? ❌
Book 2 → Python? ❌
Book 3 → Python? ❌
...
Book 57 → Python? ✅

এটাই Linear Search।

কিন্তু যদি বইগুলো alphabetical order-এ সাজানো থাকে 
এবং তুমি মাঝামাঝি থেকে search করে অর্ধেক বাদ দিতে পারো, 
সেটা Binary Search-এর ধারণার দিকে যায়।

"""



# 2️⃣6️⃣ 🧠 Master Pattern
"""
Linear Search:

Initialize
    ↓
Traverse
    ↓
Compare
    ↓
Found?
 ↙      ↘
Yes      No
 ↓        ↓
Return   Continue
Index
    ↓
শেষে
    ↓
-1

"""



# 2️⃣7️⃣ Common Mistake ❌
"""
এই code:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(i)

এখানে target পাওয়া গেলেও function কোনো value return করছে না।

যদি function-এর expected output index হয়, তাহলে:

return i

ব্যবহার করা উচিত।

"""



# 2️⃣8️⃣ আরেকটি Mistake ❌
"""
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        else:
            return -1

এটা ভুল।

কারণ প্রথম element target না হলেই function শেষ হয়ে যাবে।

Example:

arr = [10, 20, 30]
target = 30

প্রথম check:

10 == 30 → False

তখনই:

return -1

হয়ে যাবে।

সঠিক:
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

-1 অবশ্যই loop-এর বাইরে থাকবে।

"""



# 2️⃣9️⃣ আরেকটি গুরুত্বপূর্ণ Mistake ❌
"""
এটা:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

        return -1

এখানেও return -1 loop-এর ভেতরে চলে গেছে।

সঠিক indentation:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

Python-এ indentation logic-এর অংশ।

"""



# 3️⃣0️⃣ Interview Question 🎤
"""
Q: What is Linear Search?

Answer:

“Linear Search is a searching algorithm where we check each element sequentially from the beginning until we find the target or reach the end of the array.”

Q: What is the time complexity?

“The best-case time complexity is O(1) when the target is the first element, while the average and worst-case complexity is O(n).”

Q: Does Linear Search require a sorted array?

“No. Linear Search can work on both sorted and unsorted arrays.”

Q: What do you return if the target is not found?

“I return -1 as a signal that the target does not exist in the array.”

"""




# 3️⃣1️⃣ 📝 1-Page Interview Note
"""
🟢 LINEAR SEARCH

Goal:
Array-এর মধ্যে target খুঁজে বের করা।

Method:
একটি একটি করে element check করা।

Code:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


Example:

arr = [10, 20, 30, 40]
target = 30

Output:
2


If not found:
-1


Pattern:

Traversal
    ↓
Compare
    ↓
Match?
    ↓
Yes → return index
No  → continue
    ↓
End → return -1


Complexity:

Best:
O(1)

Average:
O(n)

Worst:
O(n)

Space:
O(1)


Important:
return i
→ first occurrence-এর index

return -1
→ target not found

Sorted array required?
No.


Core Pattern:
Traverse → Compare → Early Return


🧠 আজকের মূল শিক্ষা

এখন Array problem দেখলে তোমার মাথায় একটি প্রশ্ন আসা উচিত:

“আমাকে কি পুরো array traverse করতে হবে, নাকি target পাওয়া মাত্র থামতে পারব?”

Linear Search-এর মূল pattern:

ARRAY
  ↓
TRAVERSAL
  ↓
COMPARE
  ↓
FOUND?
  ↓
EARLY RETURN

"""



# Short Paragraph
"""
Linear Search is a fundamental searching technique used to find a specific value in a Python list 
by checking the elements one by one from the beginning to the end.
We usually compare each element with the target, and when a match is found,
we immediately return its index using an early return. 
If the target is not found after checking the entire list, 
we return -1 as a signal that the value does not exist in the list. 
Linear Search works with both sorted and unsorted lists, 
and if there are duplicate values, it normally returns the index of the first occurrence 
because the function stops as soon as it finds a match. 
The best-case time complexity is O(1) when the target is the first element, 
while the average and worst-case time complexity are O(n) 
because we may need to check many or all elements. 
The algorithm usually uses O(1) extra space. 
he key pattern is to traverse the list, 
compare each element with the target, return the index immediately 
when a match is found, and return -1 after the loop if no match exists. 
Unlike Binary Search, Linear Search does not require the list to be sorted, 
although Binary Search can be more efficient on suitable sorted data.


বাংলা অর্থ:

Linear Search হলো একটি fundamental searching technique, 
যেটি Python List-এর মধ্যে নির্দিষ্ট কোনো value খুঁজে বের করার জন্য ব্যবহার করা হয়। 
এখানে List-এর element-গুলোকে শুরু থেকে শেষ পর্যন্ত একটি একটি করে check করা হয় 
এবং প্রতিটি element-কে target-এর সাথে compare করা হয়। 
কোনো element target-এর সাথে মিলে গেলে আমরা সঙ্গে সঙ্গে তার index return করি—এটাকে early return বলা হয়। 
আর পুরো List search করার পরও target পাওয়া না গেলে -1 return করি, 
যা এখানে বোঝায় যে target List-এর মধ্যে নেই। 
Linear Search sorted এবং unsorted—দুই ধরনের List-এর ক্ষেত্রেই কাজ করে। 
List-এ duplicate value থাকলে সাধারণত প্রথম matching occurrence-এর index return হয়, 
কারণ প্রথম match পাওয়ার পরই return হয়ে যায় এবং loop আর চলতে থাকে না। 
এর best-case time complexity O(1), যখন target প্রথম element-এই পাওয়া যায়। 
আর average এবং worst-case time complexity O(n), 
কারণ অনেকগুলো বা পুরো List-এর element check করতে হতে পারে। 
এর অতিরিক্ত space complexity সাধারণত O(1)। Linear Search-এর মূল pattern হলো: List traverse করা → 
প্রতিটি element target-এর সাথে compare করা → match পেলে সঙ্গে সঙ্গে index return করা → 
পুরো List search করেও না পেলে -1 return করা। 
Binary Search-এর বিপরীতে Linear Search-এর জন্য List sorted হওয়া বাধ্যতামূলক নয়, 
যদিও উপযুক্ত sorted data-এর ক্ষেত্রে Binary Search আরও efficient হতে পারে।

"""
