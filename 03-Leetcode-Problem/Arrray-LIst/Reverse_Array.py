

# 1️⃣ Reverse Array কী?
"""
ধরি:
arr = [1, 2, 3, 4, 5]

Reverse করলে:
[5, 4, 3, 2, 1]

অর্থাৎ:
প্রথম ↔ শেষ
দ্বিতীয় ↔ দ্বিতীয়-শেষ
তৃতীয় ↔ তৃতীয়-শেষ

Visual:
Before:

1   2   3   4   5
↑               ↑
L               R

After first swap:

5   2   3   4   1
    ↑       ↑
    L       R

After second swap:

5   4   3   2   1
        ↑
      Middle

"""



# 2️⃣ Input কী?
# একটি Array/List:
# arr = [1, 2, 3, 4, 5]




# 3️⃣ Output কী?
# Reversed Array:
# [5, 4, 3, 2, 1]




# 4️⃣ প্রথমে সহজ Python Approach
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)




# 5️⃣ Two Pointers কী?
"""
Two Pointers মানে:

Array-এর দুই জায়গা থেকে দুইটি pointer ব্যবহার করা।

আমরা এখানে ব্যবহার করব:

left
right

শুরুতে:

left = 0
right = len(arr) - 1

যদি:

arr = [1, 2, 3, 4, 5]

তাহলে:

index:  0   1   2   3   4
value:  1   2   3   4   5
        ↑           ↑
       left       right

অর্থাৎ:

left = 0
right = 4

"""





# 6️⃣ মূল Logic
"""
আমাদের algorithm:

Left + Right
    ↓
দুই value swap
    ↓
left += 1
    ↓
right -= 1
    ↓
left < right?
    ↓
Yes → আবার swap
No  → Stop

"""




# 7️⃣ Basic Code:
def reverse_array(arr):
   left = 0
   right = len(arr) - 1

   while left < right:
      arr[left], arr[right] = arr[right], arr[left]

      left += 1
      right -= 1

   return arr 

arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))




# 8️⃣ Code Line by Line
"""
Step 1
left = 0

Array-এর প্রথম index।

Step 2
right = len(arr) - 1

Array-এর শেষ index।

যদি:

arr = [1, 2, 3, 4, 5]

তাহলে:

len(arr) = 5
right = 5 - 1
right = 4

কারণ শেষ index হলো 4।

"""



# 9️⃣ কেন len(arr) - 1?
"""
এটা খুব গুরুত্বপূর্ণ।

যদি:

arr = [10, 20, 30]

তাহলে:

len(arr) = 3

কিন্তু valid index:

0, 1, 2

তাই last index:

3 - 1 = 2

অর্থাৎ:

right = len(arr) - 1

"""




# 🔟 Swap
"""
সবচেয়ে গুরুত্বপূর্ণ line:

arr[left], arr[right] = arr[right], arr[left]

এটা Python-এর multiple assignment ব্যবহার করে দুইটি value swap করে।

ধরি:

arr = [1, 2, 3, 4, 5]

left = 0
right = 4

তাহলে:

arr[0], arr[4] = arr[4], arr[0]

অর্থাৎ:

1 ↔ 5

Result:

[5, 2, 3, 4, 1]

"""



# 1️⃣1️⃣ তারপর Pointer Move
"""
Swap করার পরে:

left += 1

অর্থাৎ:

left = left + 1

এবং:

right -= 1

অর্থাৎ:

right = right - 1

তাই:

left → ডানদিকে যাবে
right → বামদিকে যাবে

"""




# 1️⃣2️⃣ 🔥 Full Dry Run
"""
Input:

arr = [1, 2, 3, 4, 5]

শুরু:

left = 0
right = 4

Array:

index:  0   1   2   3   4
value:  1   2   3   4   5
        ↑           ↑
       left       right
Step 1

Condition:

left < right
0 < 4

True।

Swap:

1 ↔ 5

Array:

[5, 2, 3, 4, 1]

Pointer move:

left = 1
right = 3
Step 2
1 < 3

True।

Swap:

2 ↔ 4

Array:

[5, 4, 3, 2, 1]

Pointer:

left = 2
right = 2
Step 3

Check:

2 < 2

False।

Loop stop।

Final:

[5, 4, 3, 2, 1]

"""



# 1️⃣3️⃣ Dry Run Table
"""
| Step  | left | right | Swap    | Array         |
| ----- | ---: | ----: | ------- | ------------- |
| Start |    0 |     4 | —       | `[1,2,3,4,5]` |
| 1     |    0 |     4 | `1 ↔ 5` | `[5,2,3,4,1]` |
| 2     |    1 |     3 | `2 ↔ 4` | `[5,4,3,2,1]` |
| 3     |    2 |     2 | Stop    | `[5,4,3,2,1]` |

"""




# 1️⃣4️⃣ কেন while left < right?
"""
এটা খুব গুরুত্বপূর্ণ।

আমরা দুই pointer দিয়ে বাইরের দুই element swap করছি।

যখন:

left == right

তখন তারা একই element-এ আছে।

Example:

[1, 2, 3, 4, 5]
        ↑
      middle

Middle element-এর নিজের সাথে swap করার প্রয়োজন নেই।

তাই:

while left < right:

ব্যবহার করি।

"""



# 1️⃣5️⃣ left <= right দিলে?
"""
while left <= right:

দিলেও algorithm সাধারণত ভুল result দেবে না, কারণ middle element নিজেই নিজের সাথে swap হবে।

কিন্তু সেটা unnecessary operation।

তাই standard এবং clean approach:

while left < right:

"""




# 1️⃣6️⃣ Even Number of Elements
"""
ধরি:

arr = [1, 2, 3, 4]

Index:

0   1   2   3
↑           ↑
L           R

First:

1 ↔ 4

Result:

[4, 2, 3, 1]

Then:

2 ↔ 3

Result:

[4, 3, 2, 1]

Pointer:

left = 2
right = 1

Now:

2 < 1 → False

Stop।

"""




# 1️⃣7️⃣ Odd vs Even
"""
Odd
[1, 2, 3, 4, 5]

একটি middle element থাকবে।

Even
[1, 2, 3, 4]

Middle-এ দুইটি element থাকবে।

দুই ক্ষেত্রেই:

while left < right:

কাজ করবে।
"""




# 1️⃣8️⃣ Empty List
"""
arr = []

তাহলে:

left = 0
right = -1

Condition:

0 < -1

False।

কোনো swap হবে না।

Output:

[]

"""




# 1️⃣9️⃣ Single Element
"""
arr = [10]

তাহলে:

left = 0
right = 0

Condition:

0 < 0

False।

Output:

[10]

সঠিক।

"""





# 2️⃣0️⃣ Two Elements
"""
arr = [10, 20]

Start:

left = 0
right = 1

Swap:

10 ↔ 20

Result:

[20, 10]

Pointer:

left = 1
right = 0

Stop।

"""




# 2️⃣1️⃣ In-Place কী?
"""
আজকের algorithm-এর একটি খুব গুরুত্বপূর্ণ term:

In-Place

In-place মানে:

নতুন array তৈরি না করে existing array-টির মধ্যেই modification করা।

আমরা:

arr[left], arr[right] = arr[right], arr[left]

দিয়ে original arr-কেই পরিবর্তন করছি।

অর্থাৎ:

Original Array
      ↓
সেই array-এর মধ্যেই swap
      ↓
Reversed Array

"""




# 2️⃣2️⃣ In-Place Reverse-এর সুবিধা
"""

আমরা নতুন list তৈরি করছি না:

result = []

এমন কিছু নেই।

তাই auxiliary space খুব কম।

Time:
O(n)
Auxiliary Space:
O(1)

"""




# 2️⃣3️⃣ কেন Time O(n)?
"""

ধরি:

n = 5

আমরা প্রায়:

n / 2

টি swap করি।

যেমন:

5 elements → 2 swaps
100 elements → 50 swaps
1000 elements → 500 swaps

Big-O-তে constant 1/2 বাদ দেওয়া হয়।

তাই:

O(n/2)
→ O(n)

"""



# 2️⃣4️⃣ Space Complexity
"""

আমরা ব্যবহার করছি:

left
right

দুটি variable।

Input size যতই বাড়ুক, variable সংখ্যা বাড়ছে না।

তাই:

Space = O(1)

এটাই in-place algorithm-এর একটি বড় advantage।

"""




# 2️⃣5️⃣ arr[::-1] দিয়ে Reverse
"""
arr = [1, 2, 3, 4, 5]

result = arr[::-1]
print(result)
Output:

[5, 4, 3, 2, 1]

কিন্তু এখানে:

নতুন list তৈরি হচ্ছে

তাই extra space লাগে।

Conceptually:

arr
 ↓
slice
 ↓
new list

অন্যদিকে Two Pointer:

arr
 ↓
same array
 ↓
swap

"""




# 2️⃣6️⃣ reverse() বনাম Two Pointer
"""
| Approach              | Original Modify? | Time |    Extra Space |
| --------------------- | ---------------- | ---: | -------------: |
| `arr.reverse()`       | ✅                | O(n) | O(1) auxiliary |
| Two Pointer           | ✅                | O(n) |           O(1) |
| `arr[::-1]`           | ❌                | O(n) |           O(n) |
| `list(reversed(arr))` | ❌                | O(n) |           O(n) |
Python-এর built-in implementation ব্যবহার করা practical code-এ ভালো হতে পারে, 
কিন্তু DSA-তে Two Pointer pattern বোঝা বেশি গুরুত্বপূর্ণ।
"""




# 2️⃣7️⃣ 🔥 Two Pointer-এর আসল Concept
"""
আজ শুধু reverse শেখা উদ্দেশ্য নয়।

তোমার মাথায় এই pattern বসাতে হবে:

Two Ends
 ↓
Left Pointer + Right Pointer
 ↓
Compare / Swap / Process
 ↓
Move Toward Center

Reverse-এর ক্ষেত্রে:

left ↔ right

অর্থাৎ opposite direction থেকে দুই pointer এগিয়ে আসে।

"""



# 2️⃣8️⃣ Real-Life Example
"""

ধরো ৫ জন মানুষ একটি লাইনে দাঁড়িয়ে আছে:

A B C D E

তাদের order reverse করতে চাই:

E D C B A

প্রথমে:

A ↔ E

তারপর:

B ↔ D

C middle-এ আছে, তাই সেটাকে কিছু করতে হবে না।

এটাই Two Pointer Reverse।

"""



# 2️⃣9️⃣ 🔥 এই Pattern পরে কোথায় লাগবে?
"""

Two Pointer খুব গুরুত্বপূর্ণ।

পরবর্তীতে তুমি ব্যবহার করবে:

Palindrome
left → ← right

প্রথম ও শেষ character compare।

Two Sum Sorted Array
left → ← right

sum অনুযায়ী pointer move।

Remove Duplicates

Sorted array-তে pointer ব্যবহার করে in-place modification।

Move Zeroes

একটি pointer position track করবে, আরেকটি traverse করবে।

অর্থাৎ আজকের:

left + right

ভবিষ্যতে আরও অনেক জায়গায় আসবে।

"""




# 3️⃣0️⃣ Common Mistake ❌
"""
Mistake 1
right = len(arr)

এটা ভুল।

কারণ:

arr = [1, 2, 3, 4, 5]

valid index:

0, 1, 2, 3, 4

কিন্তু:

len(arr)

হলো:

5

arr[5] invalid।

সঠিক:

right = len(arr) - 1


3️⃣1️⃣ Common Mistake ❌

Pointer move না করা:

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

এখানে left এবং right কখনো পরিবর্তন হচ্ছে না।

তাই একই swap বারবার হবে।

সঠিক:

left += 1
right -= 1


3️⃣2️⃣ Common Mistake ❌

Condition ভুল:

while left > right:

শুরুতেই:

0 > 4

False।

তাই loop চলবেই না।

সঠিক:

while left < right:


3️⃣3️⃣ Common Mistake ❌

শুধু value swap করে pointer update না করা:

arr[left], arr[right] = arr[right], arr[left]

# left += 1
# right -= 1

Algorithm আটকে যাবে।

Two Pointer-এর standard structure:

while left < right:
    process
    left += 1
    right -= 1

"""




# 3️⃣4️⃣ Interview Question 🎤
"""
Q: How do you reverse an array in-place?

তুমি বলতে পারো:

“I use two pointers, one at the beginning and one at the end of the array. I swap the elements at those positions and then move the left pointer forward and the right pointer backward. I continue until the pointers meet. This reverses the array in-place.”

Q: What is the time complexity?

“The time complexity is O(n), because although I perform about n/2 swaps, we ignore the constant factor in Big-O.”

Q: What is the space complexity?

“The auxiliary space complexity is O(1), because I only use two pointer variables and modify the array in-place.”

Q: Why use left < right?

“Because once the two pointers meet or cross, all necessary swaps have already been completed.”

"""




# 3️⃣5️⃣ 📝 1-Page Interview Note
"""
🟢 LESSON 17 — REVERSE ARRAY

Goal:
Array-কে reverse করা।

Example:

[1, 2, 3, 4, 5]

↓

[5, 4, 3, 2, 1]


Two Pointer:

left = 0
right = len(arr) - 1


Code:

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


Logic:

Left ↔ Right
   ↓
Swap
   ↓
left += 1
right -= 1
   ↓
Repeat
   ↓
left >= right
   ↓
Stop


Time:
O(n)

Space:
O(1)

Why?
Approximately n/2 swaps
→ O(n)


Important:
len(arr) - 1
→ last index

while left < right
→ process until pointers meet

In-place
→ original array modified


Core Pattern:

Two Pointers
→ Opposite Ends
→ Swap
→ Move Toward Center

"""



## Short Paragraph:
"""

"""