

# 🟢 1. Write Pointer — In-place
class Solution:
   def moveZeroes(self, nums: list[int])-> None:

      write = 0

      for read in range(len(nums)):
         if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

      while write < len(nums):
         nums[write] = 0
         write += 1


arr = [0, 1, 0, 3, 12]
solution = Solution()
solution.moveZeroes(arr)
print(arr)
   


# 🟢 2. Swap-based Two Pointer
class Solution:
   def move_Zeros(self, arr: list[int])-> int:

      write = 0

      for read in range(len(arr)):
         if arr[read] != 0:
            arr[write], arr[read] = arr[read], arr[write]
            write += 1

      return arr 


arr = [0, 1, 0, 3, 12]
solution = Solution()
print(solution.move_Zeros(arr))




# 🔵 3. result = [] ব্যবহার করলে?
def moveZeros(arr):
   result = []

   for x in arr:
      if x != 0:
         result.append(x)

   while len(result) < len(arr):
      result.append(0)

   return result

arr = [0, 1, 0, 3, 12]
print(moveZeros(arr))
      



# 1️⃣ Problem কী?
"""
আমাদের একটি array দেওয়া থাকবে।

Array-এর সব 0-কে শেষে move করতে হবে, কিন্তু non-zero element-গুলোর original order ঠিক রাখতে হবে।

Example:
arr = [0, 1, 0, 3, 12]

Expected:

[1, 3, 12, 0, 0]

খেয়াল করো:

Non-zero:
1 → 3 → 12

তাদের order পরিবর্তন হয়নি।

শুধু 0-গুলো শেষে চলে গেছে।

"""



# 2️⃣ Input কী?
# একটি integer array:
# [0, 1, 0, 3, 12]



# 3️⃣ Output কী?
# একই array-তে zero-গুলো শেষে থাকবে:
# [1, 3, 12, 0, 0]



# 4️⃣ সবচেয়ে গুরুত্বপূর্ণ তিনটি Requirement
"""
এই problem-এ তিনটি বিষয় মনে রাখবে:

Requirement 1

সব 0 শেষে যাবে।

Requirement 2

Non-zero elements-এর order preserve করতে হবে।

1 → 3 → 12

এটাই থাকবে।

Requirement 3

Array-টি in-place modify করতে হবে।

অর্থাৎ নতুন array তৈরি না করে original array পরিবর্তন করা।

"""




# 5️⃣ প্রথমে সহজ চিন্তা
"""
ধরি:

[0, 1, 0, 3, 12]

আমরা non-zero element-গুলোকে সামনে আনব:

1
3
12

তারপর বাকি জায়গাগুলো:

0
0

তাই conceptually:

Non-zero elements → সামনে
Zero elements     → শেষে

"""




# 6️⃣ এখানে Two Pointer কেন?
"""

আমরা একটি pointer ব্যবহার করব:

position

এর কাজ:

পরবর্তী non-zero element কোথায় বসবে সেটা track করা।

আর একটি loop দিয়ে পুরো array traverse করব।

তাই এখানে দুই ধরনের pointer/position:

read pointer
write pointer

"""



# 7️⃣ Read Pointer কী?
"""
read pointer array-এর প্রতিটি element check করবে।

যেমন:

[0, 1, 0, 3, 12]
 ↑
read

তারপর:

[0, 1, 0, 3, 12]
    ↑
   read

তারপর:

[0, 1, 0, 3, 12]
       ↑
      read

অর্থাৎ:

read → পুরো array traverse করবে

"""



# 8️⃣ Write Pointer কী?
"""

write pointer বলে দেবে:

পরবর্তী non-zero value কোথায় বসবে?

শুরুতে:

write = 0

অর্থাৎ প্রথম non-zero element-এর জায়গা:

index 0

"""



# 9️⃣ মূল Algorithm
"""
Algorithm:

write = 0

array traverse করো

যদি arr[read] != 0:
    arr[write] = arr[read]
    write += 1

তারপর write থেকে শেষ পর্যন্ত 0 বসাও

এটাই মূল idea।

"""



# 🔟 Code — Basic Two-Pass Approach
def move_zeroes(arr):
    write = 0

    # Step 1: Move non-zero elements forward
    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write] = arr[read]
            write += 1

    # Step 2: Fill remaining positions with zero
    while write < len(arr):
        arr[write] = 0
        write += 1

    return arr


arr = [0, 1, 0, 3, 12]

print(move_zeroes(arr))



# 1️⃣1️⃣ এখন Code Line by Line বুঝি
"""
Step 1
write = 0

এর অর্থ:

প্রথম non-zero element index 0 থেকে বসানো শুরু হবে।

Step 2
for read in range(len(arr)):

এখানে read:

0 → 1 → 2 → 3 → 4

সব index visit করবে।

Step 3
if arr[read] != 0:

আমরা শুধু non-zero value চাই।

যদি:

arr[read] == 0

তাহলে skip।

যদি:

arr[read] != 0

তাহলে সামনে বসাব।

"""



# 1️⃣2️⃣ এই Line-টাই Main
"""
arr[write] = arr[read]

ধরি:

arr = [0, 1, 0, 3, 12]

read = 1
write = 0

তখন:

arr[0] = arr[1]

অর্থাৎ:

arr[0] = 1

Array:

[1, 1, 0, 3, 12]

এখানে সাময়িকভাবে duplicate 1 দেখা যাচ্ছে।

এটা সমস্যা নয়।

কারণ পরে আমরা বাকি জায়গাগুলো 0 দিয়ে overwrite করব।

"""



# 1️⃣3️⃣ 🔥 Full Dry Run
"""
Input:

arr = [0, 1, 0, 3, 12]

Start:

write = 0
Iteration 1
read = 0
arr[read] = 0

Condition:

0 != 0

False।

তাই কিছু করব না।

write = 0

Array:

[0, 1, 0, 3, 12]
Iteration 2
read = 1
arr[read] = 1

Condition:

1 != 0

True।

তাই:

arr[write] = arr[read]

অর্থাৎ:

arr[0] = arr[1]

Array:

[1, 1, 0, 3, 12]

তারপর:

write += 1

তাই:

write = 1
Iteration 3
read = 2
arr[2] = 0

Condition false।

কিছু করব না।

write = 1

Array:

[1, 1, 0, 3, 12]
Iteration 4
read = 3
arr[3] = 3

Non-zero।

তাই:

arr[1] = arr[3]

Array:

[1, 3, 0, 3, 12]

তারপর:

write = 2
Iteration 5
read = 4
arr[4] = 12

Non-zero।

তাই:

arr[2] = arr[4]

Array:

[1, 3, 12, 3, 12]

তারপর:

write = 3

"""



# 1️⃣4️⃣ এখন কী হলো?
"""
আমাদের non-zero elements সঠিক জায়গায় এসেছে:

[1, 3, 12, ?, ?]

এখন:

write = 3

Array length:

5

তাই index:

3
4

এগুলোতে 0 বসাতে হবে।

"""



"""
1️⃣5️⃣ Second Loop
while write < len(arr):
    arr[write] = 0
    write += 1
প্রথমবার:
write = 3

তাই:

arr[3] = 0

Array:

[1, 3, 12, 0, 12]

তারপর:

write = 4
দ্বিতীয়বার:
arr[4] = 0

Final:

[1, 3, 12, 0, 0]



1️⃣6️⃣ Dry Run Table
Step	read	value	write	Action
1	0	0	0	Skip
2	1	1	0	arr[0]=1
3	2	0	1	Skip
4	3	3	1	arr[1]=3
5	4	12	2	arr[2]=12

এরপর:

write = 3

Fill zero:

index 3 → 0
index 4 → 0

Final:

[1, 3, 12, 0, 0]



1️⃣7️⃣ 🔥 এখানে আসল Pattern

এই problem-এর সবচেয়ে গুরুত্বপূর্ণ pattern:

READ
 ↓
Check
 ↓
Non-zero?
 ↓
YES
 ↓
WRITE
 ↓
write += 1

অর্থাৎ:

Read Pointer
     ↓
Traverse
     ↓
Find useful element
     ↓
Write Pointer
     ↓
Place it




1️⃣8️⃣ কেন write pointer দরকার?

ধরি:

[0, 0, 5, 0, 8]

Non-zero:

5
8

আমরা চাই:

[5, 8, 0, 0, 0]

read শুধু খুঁজবে:

0 → 0 → 5 → 0 → 8

কিন্তু প্রশ্ন:

5 কোথায় বসবে?

উত্তর:

write = 0

তারপর 8 কোথায়?

write = 1

তাই write হচ্ছে:

Next available position for a non-zero element.




1️⃣9️⃣ Example 2
arr = [1, 0, 2, 0, 3]

Expected:

[1, 2, 3, 0, 0]

Non-zero sequence:

1 → 2 → 3

Order preserved।




2️⃣0️⃣ Example 3 — No Zero
arr = [1, 2, 3, 4]

সবগুলো non-zero।

তাই:

[1, 2, 3, 4]

কোনো পরিবর্তন প্রয়োজন নেই।




2️⃣1️⃣ Example 4 — All Zero
arr = [0, 0, 0]

কোনো non-zero নেই।

তাই:

[0, 0, 0]




2️⃣2️⃣ Example 5 — Zero at End
arr = [1, 2, 3, 0, 0]

Expected:

[1, 2, 3, 0, 0]

Already correct।




2️⃣3️⃣ Example 6 — Negative Numbers
arr = [0, -1, 0, -5, 3]

Non-zero values:

-1, -5, 3

Output:

[-1, -5, 3, 0, 0]

কারণ condition:

arr[read] != 0

Negative value-ও non-zero।




2️⃣4️⃣ Complexity

আমাদের প্রথম loop:

for read in range(len(arr)):

প্রায় n বার চলে।

তাই:

O(n)

দ্বিতীয় loop-ও সর্বোচ্চ n বার চলতে পারে।

তাই:

O(n) + O(n)

Big-O:

O(n)
Time Complexity:

O(n)




2️⃣5️⃣ Space Complexity

আমরা ব্যবহার করছি:

read
write

দুটি variable।

কোনো নতুন array তৈরি করছি না।

তাই:

Auxiliary Space = O(1)

এবং array-টি in-place modify হচ্ছে।




2️⃣6️⃣ result = [] ব্যবহার করলে?

সহজ approach হতে পারে:

def move_zeroes(arr):
    result = []

    for x in arr:
        if x != 0:
            result.append(x)

    while len(result) < len(arr):
        result.append(0)

    return result

এটা কাজ করবে।

কিন্তু:

Space = O(n)

কারণ নতুন list:

result = []

তৈরি করেছি।

আর আমাদের মূল approach:

Time  → O(n)
Space → O(1)

এটাই in-place optimization।




2️⃣7️⃣ আরও Compact Two-Pointer Version

আরেকটি গুরুত্বপূর্ণ approach হলো swap-based Two Pointer।

def move_zeroes(arr):
    write = 0

    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write], arr[read] = arr[read], arr[write]
            write += 1

    return arr

Test:

arr = [0, 1, 0, 3, 12]

print(move_zeroes(arr))

Output:

[1, 3, 12, 0, 0]




2️⃣8️⃣ এই Version কীভাবে কাজ করে?

এখানে:

read

পুরো array scan করে।

আর:

write

পরবর্তী non-zero-এর position ধরে রাখে।

যখন non-zero পাওয়া যায়:

arr[write], arr[read] = arr[read], arr[write]

তখন non-zero সামনে চলে আসে।




2️⃣9️⃣ Dry Run — Swap Version

Input:

[0, 1, 0, 3, 12]

Start:

write = 0
read = 0
value = 0

Skip।

write = 0
read = 1
value = 1

Swap:

arr[0] ↔ arr[1]

Result:

[1, 0, 0, 3, 12]

Then:

write = 1
read = 2
value = 0

Skip।

write = 1
read = 3
value = 3

Swap:

arr[1] ↔ arr[3]

Result:

[1, 3, 0, 0, 12]

Then:

write = 2
read = 4
value = 12

Swap:

arr[2] ↔ arr[4]

Result:

[1, 3, 12, 0, 0]

Final।




3️⃣0️⃣ দুই Approach-এর পার্থক্য
Approach 1 — Copy non-zero + Fill zero
arr[write] = arr[read]

তারপর:

arr[write] = 0
Approach 2 — Swap
arr[write], arr[read] = arr[read], arr[write]

দুটোই:

Time  = O(n)
Space = O(1)

কিন্তু DSA শেখার জন্য দুটো concept বোঝা ভালো।




3️⃣1️⃣ কেন Non-zero order নষ্ট হচ্ছে না?

এটা খুব গুরুত্বপূর্ণ।

Input:

[0, 1, 0, 3, 12]

Read pointer সবসময়:

left → right

direction-এ যাচ্ছে।

তাই non-zero পাওয়া যায়:

1
3
12

এই order-এই।

আর write pointer তাদের sequentially বসায়:

index 0 → 1
index 1 → 3
index 2 → 12

তাই order preserve হয়।



3️⃣2️⃣ 🔥 Important English Keywords
English	বাংলা অর্থ
Move	সরানো
Zeroes	শূন্যগুলো
Non-zero	শূন্য নয় এমন
Preserve order	ক্রম ঠিক রাখা
In-place	একই array-তে পরিবর্তন
Read pointer	পড়ার/scan করার pointer
Write pointer	লেখার position track করা
Traverse	একে একে visit করা
Swap	অদলবদল করা
Position	অবস্থান
Shift	সরিয়ে দেওয়া
Stable order	আগের order বজায় রাখা



3️⃣3️⃣ Interview Question 🎤
Q: How would you move all zeroes to the end of an array?

তুমি বলতে পারো:

“I use a write pointer to track the next position where a non-zero element should be placed. I traverse the array with a read pointer. Whenever I find a non-zero element, I place it at the write position and increment the write pointer. After processing all elements, I fill the remaining positions with zeroes.”

Q: What is the time complexity?

“The time complexity is O(n), because I traverse the array a constant number of times.”

Q: What is the space complexity?

“The auxiliary space complexity is O(1), because I modify the array in-place and don't use an additional array.”

Q: Why do you need two pointers?

“The read pointer scans every element, while the write pointer tracks where the next non-zero element should be placed.”


"""




# 3️⃣4️⃣ 📝 1-Page Interview Note
"""
🟢 LESSON 18 — MOVE ZEROES

Problem:

[0, 1, 0, 3, 12]

↓

[1, 3, 12, 0, 0]


Requirements:

1. Zero → End
2. Non-zero order → Preserve
3. In-place modification


Main Pattern:

READ POINTER
     ↓
Traverse
     ↓
Find non-zero
     ↓
WRITE POINTER
     ↓
Place non-zero
     ↓
write += 1
     ↓
Fill remaining positions with 0


Code:

def move_zeroes(arr):
    write = 0

    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write] = arr[read]
            write += 1

    while write < len(arr):
        arr[write] = 0
        write += 1

    return arr


Time:
O(n)

Space:
O(1)


Key Idea:

Read → Find useful element
Write → Put useful element


Important:

write = next position
for read → scan entire array

Pattern:

Traversal
+
Two Pointers
+
In-place Modification

"""
