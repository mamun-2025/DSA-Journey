


# Leetcode problem
# How-many_numbers_smaller_than_current_number
class Solution:
   def samllerNumbersThanCurrent(self, nums: list[int])-> list[int]:

      result = []

      for current in nums:
         count = 0

         for num in nums:
            if num < current:
               count += 1

         result.append(count)

      return result



# 1️⃣ Problem কী?
# ধরো আমাদের একটি list আছে:
numbers = [10, 20, 10, 10, 30, 20, 40]
"""
আমরা জানতে চাই:

10 কতবার আছে?

উত্তর:

10 → 3 times

এখানে 10 হলো আমাদের target।

"""



# 2️⃣ Input কী?
# একটি List/Array
# একটি Target value
numbers = [10, 20, 10, 10, 30, 20, 40]
target = 10




# 3️⃣ Output কী?
# Target কতবার এসেছে।
# 3




# 4️⃣ মূল Logic
"""
এখানে আমাদের basic pattern:

List
 ↓
Traverse
 ↓
প্রতিটি element target-এর সাথে compare
 ↓
মিলে গেলে counter বাড়াও
 ↓
শেষে counter return

সবচেয়ে গুরুত্বপূর্ণ line:

count += 1

এর অর্থ:

count = count + 1

"""




# 5️⃣ প্রথমে Counter বুঝি
"""
ধরি:
count = 0

শুরুতে কোনো occurrence পাওয়া যায়নি।
তাই:
count = 0

যখন target পাওয়া যাবে:
count += 1

তখন:
0 → 1
1 → 2
2 → 3

অর্থাৎ count ধীরে ধীরে result তৈরি করছে।
এটাকে বলা হয় Counter Variable।

"""



# 6️⃣ Basic Code
numbers = [10, 20, 10, 30, 10, 40]

target = 10

count = 0 

for num in numbers:
   if num == target:
      count += 1

print("Total Count:", count)




# 7️⃣ Code Line by Line
"""
Step 1
numbers = [10, 20, 10, 30, 10, 40]
আমাদের list।

Step 2
target = 10
আমরা 10 খুঁজছি।

Step 3
count = 0
এখন পর্যন্ত 10 পাওয়া যায়নি।

Step 4
for number in numbers:
List-এর প্রতিটি element একে একে নেব।

Step 5
if number == target:
প্রতিটি element target-এর সমান কিনা check করব।

Step 6
count += 1

যদি target-এর সাথে মিলে যায়, count এক বাড়বে।

Step 7
print(count)

শেষে মোট occurrence দেখাব।

"""



# 8️⃣ 🔥 Dry Run
"""
List:
numbers = [10, 20, 10, 30, 10, 40]

target = 10
শুরু:
count = 0

| Step | number | `number == 10` | count |
| ---- | -----: | -------------- | ----: |
| 1    |     10 | ✅ True         |     1 |
| 2    |     20 | ❌ False        |     1 |
| 3    |     10 | ✅ True         |     2 |
| 4    |     30 | ❌ False        |     2 |
| 5    |     10 | ✅ True         |     3 |
| 6    |     40 | ❌ False        |     3 |


শেষে:
count = 3

তাই output:
3

"""




# 9️⃣ Function হিসেবে লিখি
# DSA-তে function আকারে লেখা বেশি useful:
def count_occurrences(numbers, target):
   count = 0

   for num in numbers:
      if num == target:
         count +=1 

   return count 


numbers = [10, 20, 10, 30, 10, 40]
total_count = count_occurrences(numbers, 10)
print("Total Count:", total_count)



# 🔟 আরেকটি Example
"""
numbers = [5, 2, 5, 7, 5, 9, 5]
target = 5

এখানে 5 আছে:

4 times

Dry Run:

5 → count = 1
2 → count = 1
5 → count = 2
7 → count = 2
5 → count = 3
9 → count = 3
5 → count = 4

Final:

4

"""



# 1️⃣1️⃣ Target না থাকলে কী হবে?
def count_occurrences(arr, target):
   count = 0

   for num in arr:
      if num == target:
         count += 1

   return count


numbers = [10, 20, 30, 40]
target = 50

total_count = count_occurrences(numbers, target)
print(total_count)
# কোনো element 50 নয়।

# তাই:
# count = 0

# Output:
# 0
# এটাই logical result।



# 1️⃣2️⃣ Empty List হলে?
numbers = []
target = 10

count = 0

for num in numbers:
      if num == target:
         count += 1


print(count)

# Loop একবারও চলবে না।




# 1️⃣3️⃣ Negative Number হলেও কাজ করবে
numbers = [-10, -20, -10, -30, -10, -40]

target = -10

count = 0

for number in numbers:
   if num == numbers:
      count += 1

print(count)



# 1️⃣4️⃣ Python-এর Built-in Method
# list.count(value) ব্যবহার করলে সহজে count করা যায়।
numbers = [10, 20, 10, 30, 10, 20]

total_count = numbers.count(10)
print("Total Count:", total_count)
print(numbers.count(20))




# 1️⃣5️⃣ তাহলে Manual Loop কেন শিখছি?
"""
বাস্তবে Python code লিখলে:

numbers.count(10)

খুব convenient।

কিন্তু DSA শেখার সময় আমাদের জানতে হবে ভেতরের logic কীভাবে কাজ করে।

অর্থাৎ:

numbers.count(10)

এর conceptual idea:

count = 0

for number in numbers:
    if number == 10:
        count += 1

এই pattern বুঝে গেলে পরবর্তীতে অনেক problem সহজ হবে।
"""




# 1️⃣6️⃣ 🔥 গুরুত্বপূর্ণ Pattern
"""
আজকের মূল pattern:

Traversal
    ↓
Condition
    ↓
Counter
    ↓
Update

Code:

count = 0

for x in arr:
    if condition:
        count += 1

এই pattern খুব গুরুত্বপূর্ণ।

"""



# 1️⃣7️⃣ Count Occurrences বনাম Frequency Count
"""
Count Occurrences

একটি নির্দিষ্ট value কতবার এসেছে?

arr = [1, 2, 1, 3, 1]

প্রশ্ন:

1 কতবার এসেছে?

উত্তর:

3
Frequency Count

সব value কতবার এসেছে?

arr = [1, 2, 1, 3, 1, 2]

Result:

1 → 3
2 → 2
3 → 1

এখানে আমরা পরে Dictionary / HashMap ব্যবহার করব।

যেমন:

{
    1: 3,
    2: 2,
    3: 1
}

👉 এটা আমাদের Stage 3 — Set + Dictionary/HashMap-এর খুব গুরুত্বপূর্ণ foundation।

"""




# 1️⃣8️⃣ Time Complexity
"""

আমাদের algorithm:

for number in numbers:

প্রতিটি element একবার visit করছি।

যদি list-এর size হয় n:

n elements → n visits

তাই:

Time Complexity
O(n)
"""





# 1️⃣9️⃣ Space Complexity
"""

আমরা শুধু:

count

নামক একটি variable ব্যবহার করছি।

অতিরিক্ত কোনো list/set/dictionary তৈরি করছি না।

তাই:

Auxiliary Space
O(1)

"""





# 2️⃣0️⃣ কেন O(n)?
"""

ধরি:

numbers = [1, 2, 3, 4, 5]

৫টি element → ৫টি check।

n = 5

যদি:

numbers = [1, 2, 3, ..., 1000]

তাহলে প্রায় 1000টি element check করতে হবে।

অর্থাৎ input size বাড়লে কাজও proportionally বাড়ে।

তাই:

O(n)

"""





# 2️⃣1️⃣ Common Mistake ❌
"""
অনেক beginner এভাবে লিখতে পারে:

count = 0

for number in numbers:
    if number == target:
        count = number

এটা ভুল।

কারণ আমরা count বাড়াতে চাই।

সঠিক:

count += 1
কেন?

ধরি:

numbers = [5, 5, 5]
target = 5

ভুল code:

count = 0
5 → count = 5
5 → count = 5
5 → count = 5

Final:

5

কিন্তু occurrence হলো:

3

সঠিক code:

count = 0
5 → count = 1
5 → count = 2
5 → count = 3

"""




# 2️⃣2️⃣ আরেকটি Common Mistake ❌
"""
এটা:

count = 0

for number in numbers:
    if number == target:
        count =+ 1

এটা:

count =+ 1

আর:

count += 1

এক জিনিস নয়।

সঠিক:
count += 1

মানে:

count = count + 1

"""




# 2️⃣3️⃣ Interview Explanation 🎤
"""
I initialize a counter to zero and traverse the array once.
For each element, I compare it with target value. 
If they are equal, I increment the counter.
Finally I really the counter.
The time complexity 0(n) and space ccomplexity 0(1).
"""




# 2️⃣5️⃣ 📝 1-Page Interview Note
"""
🟢 COUNT OCCURRENCES

Goal:
একটি array/list-এ target value কতবার আছে তা বের করা।

Pattern:
Traversal → Condition → Counter → Update

Code:

def count_occurrences(arr, target):
    count = 0

    for x in arr:
        if x == target:
            count += 1

    return count

Example:

arr = [10, 20, 10, 30, 10]
target = 10

Output:
3

Important:
count += 1
means
count = count + 1

Edge Cases:
[] → 0
target না থাকলে → 0
negative values → works
duplicates → count করা হয়

Time:
O(n)

Space:
O(1)

Python built-in:
arr.count(target)

Core Pattern:
Initialize → Traverse → Compare → Count → Return
"""




