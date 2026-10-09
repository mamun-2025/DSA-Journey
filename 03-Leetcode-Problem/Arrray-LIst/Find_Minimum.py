

# Leetcode Problem
# ArithmeticProgression_form_sequence
class Solution:
   def canMakeArithmeticProgression(self, arr: list[int])-> bool:

      arr.sort()
      current_difference = arr[1] - arr[0]

      for i in range(2, len(arr)):
         if arr[i] - arr[i-1] != current_difference:
            return False

      return True


solution = Solution()

result = solution.canMakeArithmeticProgression([1, 4, 7, 10])

print(result)

"""
First, I sort the array.
Then calculate the difference between the first two elements.
After that, I compare every consecutive difference with the initial difference.
If any difference is different, I return false.
Otherwise, I return true.

"""



# 1️⃣ Problem Statement
# List-এর মধ্যে সবচেয়ে ছোট সংখ্যাটি খুঁজে বের করা।
numbers = [10, 25, 7, 40, 15]


# 2️⃣ Input কী?
numbers = [10, 25, 7, 40, 15]
# অর্থাৎ একটি Array/List।


# 3️⃣ Output কী?
# একটি single value: 7


# 🧠 4️⃣ Basic Logic
"""
আমরা প্রতিটি element একে একে দেখব।
প্রথম element-কে আপাতত minimum ধরে নেব।
current_min = 10

তারপর পরের element-এর সাথে compare করব।
25 < 10 ❌

তাই:
current_min = 10

তারপর:
7 < 10 ✅

তাই:
current_min = 7

তারপর:
40 < 7 ❌

তারপর:
15 < 7 ❌

Final:
Minimum = 7

"""


# 🔥 5️⃣ Running Minimum কী?
"""
Running Minimum মানে:
এখন পর্যন্ত যতগুলো element দেখেছি, তাদের মধ্যে সবচেয়ে ছোট value।

Example:
[10, 25, 7, 40, 15]

প্রতিটি step:

Element	Running Minimum
10	         10
25	         10
7	         7
40	         7
15	         7

শেষে:
Running Minimum = 7

"""



# 6️⃣ প্রথম Implementation
numbers = [10, 25, 7, 40, 15]

current_min = numbers[0]

for number in numbers:
   if number < current_min:
      current_min = number

print(current_min)



# 🧠 7️⃣ Code Line-by-Line
"""
Step 1 — List
numbers = [10, 25, 7, 40, 15]
আমাদের input।


Step 2 — Initial Minimum
current_min = numbers[0]
প্রথম element:
10
কে initial minimum ধরছি।
current_min = 10


Step 3 — Traversal
for number in numbers:
প্রতিটি element একবার করে visit করছি।
এটাই: Traversal


Step 4 — Comparison
if number < current_min:
বর্তমান number কি বর্তমান minimum-এর চেয়ে ছোট?


Step 5 — Update
যদি ছোট হয়:
current_min = number
নতুন minimum সেট হবে।


Step 6 — Final Answer
print(current_min)
সব element দেখা শেষ হলে আমরা minimum পেয়ে যাব।

"""



# 🔥 8️⃣ Complete Dry Run
"""
Array:
[10, 25, 7, 40, 15]

Initial:
current_min = 10

Iteration 1
number = 10
current_min = 10
Check:
10 < 10 ❌
No update।
current_min = 10

Iteration 2
number = 25
Check:
25 < 10 ❌
No update।
current_min = 10

Iteration 3
number = 7
Check:
7 < 10 ✅
Update:
current_min = 7

Iteration 4
number = 40
Check:
40 < 7 ❌
No update।
current_min = 7

Iteration 5
number = 15
Check:
15 < 7 ❌
No update।
current_min = 7

Final:
7

"""



# 📊 9️⃣ Dry Run Table
"""
| Step | `number` | `current_min` আগে | Comparison | `current_min` পরে |
| ---: | -------: | ----------------: | ---------- | ----------------: |
|    1 |       10 |                10 | 10 < 10 ❌  |                10 |
|    2 |       25 |                10 | 25 < 10 ❌  |                10 |
|    3 |        7 |                10 | 7 < 10 ✅   |                 7 |
|    4 |       40 |                 7 | 40 < 7 ❌   |                 7 |
|    5 |       15 |                 7 | 15 < 7 ❌   |                 7 |


"""



# ⚠️ 1️⃣0️⃣ কেন current_min = 0 করা উচিত নয়?
"""
ধরো:
numbers = [10, 25, 7, 40]

যদি লিখি:
current_min = 0

তাহলে:
10 < 0 ❌
25 < 0 ❌
7 < 0 ❌
40 < 0 ❌

Result:
0
কিন্তু 0 list-এর মধ্যেই নেই!

সঠিক answer:
7

তাই:
current_min = numbers[0]
ব্যবহার করা safer।

"""


# 🔥 1️⃣1️⃣ Negative Numbers
numbers = [-15, -8, -25, -3, -40]

numbers = [-10, -20, -5, -30]

current_min = numbers[0]

for number in numbers:
   if number < current_min:
      current_min = number

print(current_min)

"""

# 🧠 Negative Number মনে রাখার Trick

Number line:
← smaller                  larger →
-30    -20    -10    -5    0

বামদিকে যত বেশি:
তত ছোট

তাই:
-30
হলো minimum।

"""


# 1️⃣2️⃣ Single Element
numbers = [50]

current_min = numbers[0]

for number in numbers:
   if number < current_min:
      current_min = number

print(current_min)

"""
Initial:
current_min = 50
আর কোনো ছোট element নেই।

Answer:
50
সঠিক।
"""



# 1️⃣3️⃣ Duplicate Minimum
numbers = [5, 2, 8, 2, 10]

current_min = numbers[0]

for number in numbers:
   if number < current_min:
      current_min = number

print(current_min)

"""
Minimum:
2

দুইবার থাকলেও answer শুধু:
2
আমরা minimum-এর value খুঁজছি, কতবার আছে সেটা নয়।

"""



# 1️⃣4️⃣ min() Built-in Function
numbers = [10, 25, 7, 40, 15]

result = min(numbers)
print(result)

"""
🧠 তাহলে Loop দিয়ে শেখার কারণ কী?

কারণ DSA-তে আসল skill হলো:

নিজে algorithmic logic তৈরি করতে পারা।

আমরা এখানে শিখছি:

Initialize
↓
Traverse
↓
Compare
↓
Update
↓
Return

এই pattern পরবর্তীতে শুধু minimum-এর জন্য নয়।

এটি ব্যবহার হবে:

Maximum
Minimum
Search
Count
Frequency
Best value
Smallest value
Largest value

এমনকি আরও advanced algorithms-এর মধ্যেও।

"""



# 1️⃣5️⃣ Function বানাই
def find_min(arr):
   current_min = arr[0]

   for num in arr:
      if num < current_min:
         current_min = num 

   return current_min

minimum = find_min([10, 25, 40, 7, 15])
print(minimum)

numbers = [10, 25, 40, 7, 15]
result = find_min(numbers)
print("Minimum Number:", result)



# 1️⃣6️⃣ Empty List
numbers = []

# IndexError
# কারণ list-এ কোনো element নেই।
# তাই function-এ check করতে পারি:

def find_min(arr):
   if not arr:
      return None 

   current_min = arr[0]

   for number in arr:
      if number < current_min:
         current_min = number

   return current_min


numbers = [10, 20, 40, 5, 15]

result = find_min(numbers)
print(result)


print(find_min([]))
# Output:
# None
# তবে LeetCode problem-এ input কখনো empty হবে কি না, 
# সেটা problem statement থেকে দেখতে হবে।



# 🔥 1️⃣7️⃣ Maximum vs Minimum
# Maximum
numbers = [100, 200, 1000, 700, 900]
current_max = numbers[0]

for number in numbers:
   if number > current_max:
      current_max = number

print(current_max)


# Minimum
numbers = [2, 5, 3, 1, 6]
current_min = numbers[0]

for number in numbers:
   if number < current_min:
      current_min = number

print(current_min)
"""
শুধু comparison-এর direction বদলেছে।

Maximum
>
 
Minimum
<

এটাই মূল difference।
"""



# 📊 1️⃣8️⃣ Comparison Table
"""
| Concept | Maximum           | Minimum           |
| ------- | ----------------- | ----------------- |
| Initial | `arr[0]`          | `arr[0]`          |
| Compare | `x > current_max` | `x < current_min` |
| Update  | বড় হলে           | ছোট হলে           |
| Final   | Largest value     | Smallest value    |
| Time    | O(n)              | O(n)              |
| Space   | O(1)              | O(1)              |

"""



# 🧠 1️⃣9️⃣ Time Complexity
"""
ধরো array size:

n = len(arr)

আমরা প্রতিটি element একবার visit করছি।

Element 1 → compare
Element 2 → compare
Element 3 → compare
...
Element n → compare

তাই:

Time Complexity = O(n)

"""



# 🧠 2️⃣0️⃣ Space Complexity
"""
আমরা শুধু কয়েকটি variable ব্যবহার করছি:

current_min
number

কোনো নতুন array তৈরি করছি না।

তাই auxiliary space:

Space Complexity = O(1)

"""



# 2️⃣1️⃣ Sorting করে Minimum বের করা কেন unnecessary?
numbers = [40, 5, 30, 10]

numbers.sort()
print(numbers[0])
"""
কিন্তু problem শুধু minimum চেয়েছে।

Sorting করার complexity:
O(n log n)

অন্যদিকে শুধু traversal:
O(n)

তাই:
Minimum → O(n)
Sorting → O(n log n)

শুধু minimum-এর জন্য পুরো array sort করা unnecessary work।

"""


# 🔥 2️⃣2️⃣ min() বনাম Manual Loop
"""
| Approach     |       Time |                    Space | উদ্দেশ্য                     |
| ------------ | ---------: | -----------------------: | ---------------------------- |
| `min(arr)`   |       O(n) |           O(1) auxiliary | Practical Python             |
| Manual loop  |       O(n) |                     O(1) | DSA understanding            |
| Sort + first | O(n log n) | implementation-dependent | Unnecessary for only minimum |

"""



# 2️⃣3️⃣ 7-Step DSA Framework
"""
Problem

Find the minimum element in an array.

1. Input
arr = [10, 25, 7, 40, 15]
2. Output
7
3. Logic

প্রথম element-কে current minimum ধরে:

current_min = arr[0]

তারপর traversal করে:

if x < current_min:

হলে update করব।

4. Dry Run
10 → min = 10
25 → min = 10
7  → min = 7
40 → min = 7
15 → min = 7
5. Time Complexity
O(n)
6. Space Complexity
O(1)
7. Interview Explanation

I initialize the minimum with the first element of the array. 
Then I traverse the array once and compare each element with the current minimum. 
If I find a smaller element, I update the minimum. 
This takes O(n) time and O(1) auxiliary space.

"""



# 🎤 2️⃣4️⃣ Interview Questions
"""
1. How do you find the minimum element?
= I traverse the array while maintaining a running minimum.
  If the current element is smaller than the running minimum, I update it.

2. Why initialize with the first element?
= কারণ array-এর actual value দিয়ে শুরু করলে negative values-এর ক্ষেত্রেও algorithm সঠিক থাকে।

3. Why not initialize with 0?
= কারণ সব values positive বা negative যেকোনো কিছু হতে পারে।

Example:
[-10, -20, -5]

Minimum:
-20

4. Time Complexity?
= O(n)

5. Space Complexity?
= O(1)

6. Can you find minimum without sorting?
= হ্যাঁ।
  একবার traversal করলেই যথেষ্ট।
  O(n)

"""




# 📝 2️⃣5️⃣ Short Paragraph
"""
Notebook Master Note
🟢 FIND MINIMUM

Input:
[10, 25, 7, 40, 15]

Initialize:
current_min = arr[0]

Traversal:
for x in arr:

Comparison:
if x < current_min:

Update:
current_min = x

Output:
7

Time:
O(n)

Space:
O(1)


আজকের সবচেয়ে গুরুত্বপূর্ণ Pattern
ARRAY
  ↓
TRAVERSAL
  ↓
COMPARISON
  ↓
RUNNING MINIMUM
  ↓
UPDATE
  ↓
ANSWER

আর Maximum-এর সাথে একসাথে মনে রাখো:

Find Maximum
→ if x > current_max

Find Minimum
→ if x < current_min

এই দুইটি pattern এখন তোমার Array Problem Solving-এর foundation-এর অংশ।
"""
