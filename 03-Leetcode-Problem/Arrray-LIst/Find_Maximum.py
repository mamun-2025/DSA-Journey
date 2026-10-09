


# Leetcode Problem
# Third_maximum Number

# OOP 
class Solution:
   def thirdMax(self, nums: list[int]) -> int:
      unique_nums = sorted(set(nums), reverse=True)

      if len(unique_nums) >= 3:
         return unique_nums[2]

      else:
         return unique_nums[0]


solution = Solution()

result = solution.thirdMax([2, 2, 1, 3])
print(result)


class Solution:
   def thirdMax(self, nums: list[int])-> int:
      first = None 
      second = None 
      thrid = None 

      for num in nums:

         if num == first or num == second or num == thrid:
            continue

         if first is None or num > first:
            third = second 
            second = first
            first = num 

         elif second is None or num > second:
            third = second
            second = num 

         elif third is None or num > third:
            third = num 

      if third is None:
         return first

      return third 


"""
I maintain the three largest distinct values while traversing the array once.
I skip duplicates, and whenever I find a larger value, 
I shift the existing values down. 
This allows me to solve the problem in 0(n) time and 
0(1) extra space without sorting.

"""


# 1️⃣ Problem Statement
# List-এর মধ্যে সবচেয়ে বড় সংখ্যাটি খুঁজে বের করা।

numbers = [10, 20, 7, 40, 15]


# 2️⃣ Input কী?
# Input হলো একটি list/array:

numbers = [10, 25, 7, 40, 15]


# 3️⃣ Output কী?
# একটি single value:
# 40


# 🧠 4️⃣ প্রথম Logic — একে একে Compare
# আমরা প্রতিটি number দেখব এবং বর্তমান maximum-এর সাথে compare করব।

"""
ধরো:
[10, 25, 7, 40, 15]

প্রথম number:
10

তাই:
current_max = 10

তারপর 25:
25 > 10

তাই:
current_max = 25

তারপর 7:
7 > 25 ❌

তাই maximum থাকবে:
25

তারপর 40:
40 > 25 ✅

তাই:
current_max = 40

শেষে 15:
15 > 40 ❌

তাই:
current_max = 40

Final answer:
40

"""


# 🔥 5️⃣ Running Maximum কী?
"""
Running Maximum মানে:
এখন পর্যন্ত যতগুলো element দেখেছি, তাদের মধ্যে সবচেয়ে বড় value।

ধরো:
[10, 25, 7, 40, 15]

প্রতিটি step-এ:

Element     Running Maximum
10          10
25          25
7           25
40          40
15          40

শেষের Running Maximum-ই হলো পুরো list-এর maximum।

"""



# 6️⃣ প্রথম Implementation
numbers = [10, 25, 7, 40, 15]

current_max = numbers[0]

for number in numbers:
   if number > current_max:
      current_max = number

print(current_max)



# 🧠 7️⃣ Code Line-by-Line
"""
Step 1
numbers = [10, 25, 7, 40, 15]
আমাদের array।

Step 2
current_max = numbers[0]
প্রথম element:
10
কে initial maximum ধরে নিচ্ছি।
current_max = 10

Step 3
for number in numbers:
প্রতিটি element একবার করে visit করব।
এটাই:
Traversal

Step 4
if number > current_max:
বর্তমান number কি বর্তমান maximum-এর চেয়ে বড়?

Step 5
current_max = number
যদি বড় হয়, তাহলে নতুন maximum হিসেবে সেট করব।

Step 6
print(current_max)
সব element দেখা শেষ হলে final maximum print করব।

"""



# 🔥 8️⃣ Complete Dry Run
"""
Array:

[10, 25, 7, 40, 15]

Initial:

current_max = 10
Iteration 1
number = 10
current_max = 10

Check:

10 > 10 ❌

No change.

current_max = 10
Iteration 2
number = 25

Check:

25 > 10 ✅

Update:

current_max = 25
Iteration 3
number = 7

Check:

7 > 25 ❌

No change:

current_max = 25
Iteration 4
number = 40

Check:

40 > 25 ✅

Update:

current_max = 40
Iteration 5
number = 15

Check:

15 > 40 ❌

No change:

current_max = 40
Final
40

📊 Dry Run Table:
| Step | `number` | `current_max` আগে | Comparison | `current_max` পরে |
| ---: | -------: | ----------------: | ---------- | ----------------: |
|    1 |       10 |                10 | 10 > 10 ❌  |                10 |
|    2 |       25 |                10 | 25 > 10 ✅  |                25 |
|    3 |        7 |                25 | 7 > 25 ❌   |                25 |
|    4 |       40 |                25 | 40 > 25 ✅  |                40 |
|    5 |       15 |                40 | 15 > 40 ❌  |                40 |

Final:
Maximum = 40

"""


# 9️⃣ কেন numbers[0] দিয়ে শুরু করছি?
"""
এখানে একটা গুরুত্বপূর্ণ reason আছে।

আমরা লিখেছি:

current_max = numbers[0]

কারণ আমরা চাই actual data থেকে একটি value দিয়ে শুরু করতে।

ধরো:

numbers = [-10, -20, -5, -30]

যদি লিখি:

current_max = 0

তাহলে সমস্যা হবে।

কারণ:

-10 > 0 ❌
-20 > 0 ❌
-5 > 0 ❌
-30 > 0 ❌

Result হবে:

0

কিন্তু 0 list-এর মধ্যে নেই।

সঠিক maximum:

-5

তাই:

current_max = numbers[0]

একটি safer general approach।

"""



# 🔥 1️⃣0️⃣ Negative Numbers
numbers = [-10, -5, -20, -15, -12]

current_max = numbers[0]

for number in numbers:
   if number > current_max:
      current_max = number

print(current_max)



# 1️⃣1️⃣ Single Element
numbers = [10]

current_max = numbers[0]

for number in numbers:
   if number > current_max:
      current_max = number

print(current_max)



# 1️⃣2️⃣ Duplicate Maximum
arr = [10, 50, 20, 50, 30]

current_max = arr[0]

for x in arr:
   if x > current_max:
      current_max = x 

print(current_max)

"""
দুইবার থাকলেও answer:
50
আমরা শুধু maximum value চাইছি।
"""



# 1️⃣3️⃣ max() দিয়ে সহজভাবে
# Python built-in function 

numbers = [10, 25, 7, 40, 15]

result = max(numbers)
print("Maximum Number:", result)


# 🧠 তাহলে loop কেন শিখছি?
"""
খুব গুরুত্বপূর্ণ প্রশ্ন।

যদি Python-এ:
max(numbers)
দিয়ে কাজ হয়ে যায়, তাহলে DSA-তে loop দিয়ে maximum শেখার দরকার কী?

কারণ DSA-তে তোমাকে algorithmic thinking শিখতে হবে।

max() internally এমন কোনো magic নয় যে data না দেখে answer বের করে।
Conceptually তাকে list-এর values inspect করতে হবে।

আমরা loop দিয়ে সেই logic নিজের হাতে বুঝছি:
Traversal
+
Comparison
+
State Update

এই pattern পরবর্তীতে:
Maximum
Minimum
Count
Search
Frequency
Two Pointer
Sliding Window
Dynamic Programming

ইত্যাদিতে বারবার আসবে।
"""



# 🔥 1️⃣4️⃣ Maximum Finding Pattern
"""
এটাকে একটি reusable pattern হিসেবে মনে রাখো:

Initialize
    ↓
Traverse
    ↓
Compare
    ↓
Update
    ↓
Return


Code:
current_max = arr[0]

for x in arr:
    if x > current_max:
        current_max = x

return current_max

"""




# 1️⃣5️⃣ Function বানাই
# এটাকে reusable function বানাই।
def find_max(arr):
   current_max = arr[0]

   for number in arr:
      if number > current_max:
         current_max = number

   return current_max


numbers = [10, 25, 7, 15, 40]
result = find_max(numbers)

print(numbers)
print(result)



# 🧠 1️⃣6️⃣ এখানে return কেন?
"""
কারণ function-এর কাজ হলো:
Maximum value বের করে caller-এর কাছে ফেরত দেওয়া।

তাই:
return current_max
"""



# 1️⃣7️⃣ print() vs return
"""
এটা interview এবং programming-এর জন্য গুরুত্বপূর্ণ।

print()
print(current_max)
শুধু screen-এ দেখায়।

return
return current_max
Value function-এর বাইরে পাঠায়।

তাই DSA solution-এ সাধারণত:
return current_max
ব্যবহার করব।

"""



# 🔥 1️⃣8️⃣ Empty List সমস্যা
numbers = []

# numbers[0] # IndexError
# কারণ list-এ কোনো element নেই।

# তাই function design করার সময় empty input কী হবে সেটা আগে ভাবতে হবে।

def find_max(arr):
   if not arr:
      return None 

   current_max = arr[0]

   for number in arr:
      if number > current_max:
         current_max = number

   return current_max


numbers = []
result = find_max(numbers)
print(result)

print(find_max([]))



# 🧠 1️⃣9️⃣ Edge Cases
"""
Maximum problem-এ এগুলো check করবে:

Case 1 — Normal
[10, 20, 5, 30]
→ 30

Case 2 — All negative
[-10, -20, -5]
→ -5

Case 3 — Single element
[7]
→ 7

Case 4 — Duplicate maximum
[5, 10, 10, 3]
→ 10

Case 5 — Empty list
[]
→ depends on problem requirement

"""


# 2️⃣0️⃣ কেন sort() করে Last Element নেব না?
numbers = [5, 1, 9, 3, 7]

numbers.sort()
print(numbers[-1])
"""
এতে maximum পাওয়া যাবে।
কিন্তু problem যদি শুধু maximum চায়, তাহলে পুরো list sort করার দরকার নেই।

Sorting:
O(n log n)

Maximum traversal:
O(n)

তাই শুধু maximum দরকার হলে:

Traversal → O(n)

আর sorting:
Sorting → O(n log n)
অপ্রয়োজনীয় কাজ।

"""



# 🔥 2️⃣1️⃣ Algorithm Comparison
"""
| Approach            |       Time |              Extra Space | মন্তব্য                     |
| ------------------- | ---------: | -----------------------: | --------------------------- |
| `max(arr)`          |       O(n) |           O(1) auxiliary | Python built-in             |
| Loop + comparison   |       O(n) |                     O(1) | DSA শেখার জন্য গুরুত্বপূর্ণ |
| Sort + last element | O(n log n) | implementation-dependent | Maximum-এর জন্য unnecessary |

"""



# 2️⃣2️⃣ Time Complexity
"""
ধরো:
n = len(arr)
আমরা প্রতিটি element একবার visit করছি।

arr = [10, 20, 30, 40, 50]
5টি element:
5 comparisons/iterations-এর order

1000 elements:
1000-এর order

তাই:
Time Complexity = O(n)

"""



# 2️⃣3️⃣ Space Complexity
"""
আমরা শুধু:
current_max
number
এর মতো constant number of variables ব্যবহার করছি।
নতুন array তৈরি করছি না।

তাই auxiliary space:
O(1)

"""



# ⭐ 2️⃣4️⃣ আজকের Core Pattern
"""
ARRAY MAXIMUM PATTERN

1. Initialize current_max
2. Traverse array
3. Compare current value with current_max
4. Update if larger
5. Return current_max

Time  → O(n)
Space → O(1)



🟢 FIND MAXIMUM

Input:
[10, 25, 7, 40, 15]

Logic:
current_max = first element

Traverse:
10 → 25 → 7 → 40 → 15

Compare:
if x > current_max:
    update

Output:
40

Time:
O(n)

Space:
O(1)

"""



# 🎤 2️⃣5️⃣ Interview Explanation
"""
I initialize the maximum with the first element of the arry.
Then I traverse the arry once and compare each element with current maximum.
If I find a larger value, I update the maximum.
Since I visit each element once, the time complexity is 0(n),
and the auxiliary space is 0(1).

"""