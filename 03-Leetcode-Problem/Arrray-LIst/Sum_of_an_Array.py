


# 1️⃣ Problem Statement
# Array-এর সব elements যোগ করে total বের করা।
from numpy import single


numbers = [10, 20, 30, 40, 50]


# 2️⃣ Input কী?
numbers = [10, 20, 30, 40, 50]
# অর্থাৎ একটি List/Array।



# 3️⃣ Output কী?
"""
একটি single number:
100

Visual:

[10, 20, 30, 40]
        ↓
10 + 20 + 30 + 40
        ↓
       100

"""



# 🧠 4️⃣ Basic Logic
"""
এখানে আমরা একটি variable রাখব:
total = 0

তারপর একে একে প্রতিটি number total-এর সাথে যোগ করব।
total = 0

10 → total = 10
20 → total = 30
30 → total = 60
40 → total = 100

শেষে:
total = 100

এই total variable-টিই হলো Accumulator।

"""



# 🔥 5️⃣ Accumulator কী?
""""
Accumulator হলো এমন একটি variable যেটি loop চলার সময় ধীরে ধীরে result জমা করে।

শব্দটা মনে রাখো:
Accumulate = জমা করা

উদাহরণ:
total = 0

for number in numbers:
    total += number

এখানে:
total
↓
প্রতিটি iteration-এ নতুন value জমা করছে

তাই:

Accumulator = result জমা রাখার variable

"""


# 6️⃣ Code Implementation
numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
   total += number 

print(total)



# 🧠 7️⃣ Code Line-by-Line
"""
Step 1
numbers = [10, 20, 30, 40]

আমাদের input।

Step 2
total = 0

শুরুতে total-এর মধ্যে কিছু নেই।

তাই:

total = 0
Step 3
for number in numbers:

প্রতিটি element একবার করে visit করছি।

এটা হলো:

Traversal

Step 4
total += number

এটা shorthand:

total = total + number

অর্থাৎ:

আগের total
+
বর্তমান number
=
নতুন total
Step 5
print(total)

সব elements যোগ করার পরে final result।

"""



# 🔥 8️⃣ total += number গভীরভাবে বুঝি
"""
ধরো:

total = 10
number = 20

তাহলে:

total += number

মানে:

total = total + number

অর্থাৎ:

10 + 20
= 30

তাই:

total = 30

"""



# 📊 9️⃣ Complete Dry Run
"""
Array:
[10, 20, 30, 40]

Initial:
total = 0

Iteration 1
number = 10

Calculation:
total = 0 + 10
      = 10
Iteration 2
number = 20

Calculation:

total = 10 + 20
      = 30
Iteration 3
number = 30

Calculation:

total = 30 + 30
      = 60
Iteration 4
number = 40

Calculation:

total = 60 + 40
      = 100

Final:

100

"""



# 📋 1️⃣0️⃣ Dry Run Table
"""
| Step | `number` | `total` আগে | Calculation | `total` পরে |
| ---: | -------: | ----------: | ----------- | ----------: |
|    1 |       10 |           0 | 0 + 10      |          10 |
|    2 |       20 |          10 | 10 + 20     |          30 |
|    3 |       30 |          30 | 30 + 30     |          60 |
|    4 |       40 |          60 | 60 + 40     |         100 |

"""



# 🧠 1️⃣1️⃣ কেন total = 0?
"""
এটা খুব গুরুত্বপূর্ণ।

আমরা যোগ করছি।

Addition-এর ক্ষেত্রে neutral value হলো:

0

কারণ:

0 + 10 = 10
0 + 20 = 20

তাই accumulator:

total = 0

দিয়ে শুরু করা natural।

"""




# ⚠️ 1️⃣2️⃣ total = 1 করলে কী হবে?
"""
ভুল।

total = 1

for number in [10, 20, 30]:
    total += number

Calculation:

1 + 10 + 20 + 30
= 61

কিন্তু আসল sum:

10 + 20 + 30
= 60

তাই:

Sum Accumulator
→ শুরু = 0

"""



# 🔥 1️⃣3️⃣ Negative Numbers
numbers = [10, -5, 20, -5]

total = 0

for number in numbers:
   total += number 

print("Total:", total)
# Calculation:
# 10 + (-5) + 20 + (-5)
# = 20



# 1️⃣4️⃣ All Negative Numbers
numbers = [-10, -20, -30]

total = 0

for number in numbers:
   total += number 

print("Total Number:", total)
# তাই total = 0 negative values-এর ক্ষেত্রেও perfectly কাজ করে।



# 1️⃣5️⃣ Zero থাকলে?
numbers = [10, 0, 20, 0, 30]

total = 0

for number in numbers:
   total += number 

print("Total Number: ", total)
# Zero শুধু total পরিবর্তন করে না।



# 1️⃣6️⃣ Duplicate Values
numbers = [10, 20, 10, 20, 30]

total = 0

for number in numbers:
   total += number 

print("Total Number: ", total)

"""
এখানে duplicate values remove হবে না।

মনে রাখো:
Sum
→ সব values যোগ করে

Duplicate Removal
→ আলাদা problem

"""



# 🔥 1️⃣7️⃣ Python-এর sum()
# Python-এ built-in function আছে:
# এটা practical Python programming-এ খুব useful।
numbers = [10, 20, 30, 40]

total = sum(numbers)
print(total)




# 🧠 1️⃣8️⃣ তাহলে Manual Loop কেন শিখছি?
"""
কারণ DSA-তে আমাদের শুধু built-in function ব্যবহার শেখা নয়।

আমাদের জানতে হবে:

Algorithm কীভাবে কাজ করে?

Manual loop:

total = 0

for number in numbers:
    total += number

এখানে আমরা একটি universal pattern শিখছি:

Initialize
↓
Traverse
↓
Process
↓
Update Accumulator
↓
Return

এই pattern পরবর্তীতে অনেক জায়গায় আসবে।

"""



# 🔥 1️⃣9️⃣ Accumulator Pattern-এর Examples
"""
# Sum 
total += number 

# Product
product *= number

# Count 
count += 1

# Maximum
if number > maximum:
   maximum = number 

# Minimum
if number < minimum:
   minimum = number

# Average 
average = total / count

# Frequency Count
frequency[number] += 1

# Prefix Sum
prefix_sum[i] = prefix_sum[i-1] + number 

# Suffix Sum 
suffix_sum[i] = suffix_sum[i+1] + number 

# Cumulative Sum
cumulative_sum[i] = cumulative_sum[i-1] + number 

# Running Total
running_total[i] = running_total[i-1] + number 

# Moving Average
moving_average[i] = (moving_average[i-1] * (window_size - 1) + number) / window_size


"""



# 🧠 2️⃣0️⃣ Function বানাই
def sum_of_array(arr):
   total = 0

   for number in arr:
      total += number 

   return total 


numbers = [10, 20, 30, 40]
result = sum_of_array(numbers)
print("Total Sum:", result)




# 2️⃣1️⃣ Function-এর Logic
"""
array_sum(arr)
      ↓
total = 0
      ↓
traverse arr
      ↓
total += number
      ↓
return total

"""



# 🔥 2️⃣2️⃣ Empty List
numbers = []

total = 0

for number in numbers:
   total += number 

print("Total Number: ", total)

"""
Loop একবারও চলবে না।
তাই:
total = 0

Return হবে:
0

এটা mathematically-ও reasonable:
Empty collection-এর sum = 0.

Python-ও:
sum([])

এর result:
0
দেয়।
"""
numbers = []

result = sum(numbers)
print(result)



# 2️⃣3️⃣ Time Complexity
"""
ধরো:

n = len(arr)

আমরা প্রতিটি element একবার visit করছি।

Element 1 → add
Element 2 → add
Element 3 → add
...
Element n → add

তাই:

Time Complexity = O(n)

"""




# 2️⃣4️⃣ Space Complexity
"""
আমরা শুধু:

total
number

এর মতো constant variables ব্যবহার করছি।

নতুন array তৈরি করছি না।

তাই auxiliary space:

Space Complexity = O(1)

"""




# 📊 2️⃣5️⃣ Complexity Summary
"""
Approach	Time	Auxiliary Space
Manual loop	O(n)	O(1)
sum(arr)	O(n)	O(1) auxiliary
Sort then sum	O(n log n)	unnecessary

শুধু sum বের করার জন্য sorting করার কোনো দরকার নেই।

"""




# ⚠️ 2️⃣6️⃣ একটা Common Mistake
"""
এটা:

total = 0

for number in numbers:
    total = number

Sum নয়।

কারণ এখানে:

total

প্রতিবার overwrite হচ্ছে।

Example:

numbers = [10, 20, 30]

হবে:

total = 10
total = 20
total = 30

Final:

30

কিন্তু sum:

60

সঠিক code:

total += number

কারণ আমরা previous result ধরে রাখছি।

"""



# 🔥 2️⃣7️⃣ = বনাম +=
"""
total = number

মানে:

পুরনো value replace করো।

+=
total += number

মানে:

পুরনো total-এর সাথে নতুন number যোগ করো।

DSA-তে এই difference খুব গুরুত্বপূর্ণ।

"""



# 🧠 2️⃣8️⃣ Maximum / Minimum / Sum একসাথে
# Maximum 
numbers = [10, 5, 40, 20, 15]

current_max = numbers[0]

for number in numbers:
   if number > current_max:
      current_max = number

print("Maximum:", current_max)


# Minimum
arr = [10, 5, 40, 20, 15]

current_min = arr[0]

for number in arr:
   if number < current_min:
      current_min = number 

print("Minimum:", current_min)


# Sum
def sum_of_array(arr):
   total = 0

   for number in arr:
      total += number 

   return total

num = [10, 5, 40, 20, 15]
result = sum_of_array(num)

print("Sum:", result)

"""
তিনটির common structure:

Initialize
↓
Traverse
↓
Process / Compare
↓
Update

"""



# 🎯 2️⃣9️⃣ 7-Step DSA Framework
"""
Problem:
Find the sum of all elements in an array.

1. Input
arr = [10, 20, 30, 40]

2. Output
100

3. Logic
একটি accumulator:
total = 0

তারপর:
for x in arr:
    total += x

4. Dry Run
0 + 10 = 10
10 + 20 = 30
30 + 30 = 60
60 + 40 = 100

5. Time Complexity
O(n)

6. Space Complexity
O(1)

7. Interview Explanation
I initialize a total variable to zero.
Then I traverse the array once.
For each element, I add it to the total.
Since every element is visited exactly once,
the time complexity is 0(n) and the space complexity is 0(1).

"""




# 🎤 3️⃣0️⃣ Interview Questions
""""
Q1. How do you find the sum of an array?

I initialize an accumulator to zero, traverse the array, and add each element to the accumulator.

Q2. Why initialize total with 0?

Because zero is the neutral value for addition, so it doesn't affect the first value being added.

Q3. Time Complexity?
O(n)
Q4. Space Complexity?
O(1)
Q5. Can you solve it using a built-in function?

হ্যাঁ:

sum(arr)
Q6. Why not sort the array first?

কারণ sorting unnecessary।

Sorting → O(n log n)
Sum → O(n)

শুধু sum দরকার হলে একবার traversal যথেষ্ট।

"""




# ⭐ 3️⃣1️⃣ Notebook Master Note
"""
🟢 SUM OF ARRAY

Input:
[10, 20, 30, 40]

Initialize:
total = 0

Traversal:
for x in arr:

Update:
total += x

Output:
100

Time:
O(n)

Space:
O(1)
🔥 আজকের Core Concept
ARRAY
  ↓
TRAVERSAL
  ↓
ACCUMULATOR
  ↓
UPDATE
  ↓
FINAL SUM

Array দেখলে প্রথমে ভাববে: “আমাকে কি পুরো array traverse করতে হবে? 
Traverse করার সময় আমাকে কী maintain/update করতে হবে?”

"""



# 3️⃣2️⃣ Short Paragraph
"""


"""
