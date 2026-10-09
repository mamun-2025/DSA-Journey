


"""
🟢 Lesson 19 — Nested Loop & O(n²)

আজকের Lesson 19 খুব গুরুত্বপূর্ণ। কারণ আজ আমরা শুধু nested loop শিখব না—বরং বুঝব:

একটি loop-এর ভিতরে আরেকটি loop থাকলে Time Complexity কেন O(n²) হতে পারে?

এটি DSA-তে অত্যন্ত গুরুত্বপূর্ণ foundation। পরে Brute Force, Pair Problems, Duplicate Detection, Sorting ইত্যাদিতে বারবার আসবে।



1️⃣ Nested Loop কী?

একটি loop-এর ভিতরে আরেকটি loop থাকলে তাকে Nested Loop বলে।

Basic structure:

for i in range(n):
    for j in range(n):
        print(i, j)

এখানে:

Outer Loop
    ↓
Inner Loop

অর্থাৎ:

একবার Outer Loop
    ↓
Inner Loop পুরোটা চলে



2️⃣ সহজ উদাহরণ
for i in range(3):
    for j in range(3):
        print(i, j)

Output:

0 0
0 1
0 2

1 0
1 1
1 2

2 0
2 1
2 2

খেয়াল করো:

i = 0 হলে j পুরো:

0 → 1 → 2

তারপর i = 1 হলে আবার:

0 → 1 → 2

তারপর i = 2 হলে আবার:

0 → 1 → 2



3️⃣ কতবার Inner Loop চলে?

Outer loop:

range(3)

চলে:

3 বার

প্রতিবার inner loop:

3 বার

তাই মোট:

3 × 3 = 9

বার।



4️⃣ 🔥 এখান থেকেই O(n²)

ধরি:

n = 100

Outer loop:

100 বার

Inner loop প্রতিবার:

100 বার

তাহলে:

100 × 100
= 10,000

operations।

সুতরাং:

n × n
= n²

তাই:

Time Complexity = O(n²)




5️⃣ Visual Understanding

ধরি:

n = 4

তাহলে:

        j
       0 1 2 3
     ┌─────────
i = 0│ ● ● ● ●
i = 1│ ● ● ● ●
i = 2│ ● ● ● ●
i = 3│ ● ● ● ●

মোট:

4 × 4 = 16

যদি:

n × n

হয়:

O(n²)



6️⃣ Code Example — Print All Pairs

এখন একটি practical example দেখি।

numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[i], numbers[j])

এখানে প্রত্যেক element-এর সাথে প্রত্যেক element-এর pair তৈরি হচ্ছে।

Output-এর শুরু:

10 10
10 20
10 30
10 40

20 10
20 20
20 30
20 40

30 10
30 20
30 30
30 40

40 10
40 20
40 30
40 40

মোট:

4 × 4 = 16



7️⃣ কিন্তু সব Nested Loop কি O(n²)?

🔥 না।

এটা খুব গুরুত্বপূর্ণ।

শুধু:

"দুইটা loop আছে"

দেখেই সবসময় O(n²) বলা যাবে না।

Loops কীভাবে চলে সেটা দেখতে হবে।

Example 1
for i in range(n):
    for j in range(n):
        print(i, j)

Outer:

n

Inner:

n

Total:

n × n

তাই:

O(n²)



8️⃣ Example 2 — Inner Loop Fixed
for i in range(n):
    for j in range(5):
        print(i, j)

এখানে outer:

n

inner:

5

Total:

n × 5

Big-O-তে constant বাদ যায়:

O(5n)
→ O(n)

তাই:

O(n)

🔥 Nested loop হলেও O(n²) নয়।




9️⃣ Example 3 — Inner Loop Half
for i in range(n):
    for j in range(n // 2):
        print(i, j)

Total:

n × n/2

অর্থাৎ:

n² / 2

Big-O constant বাদ দিলে:

O(n²)



🔟 Example 4 — Inner Loop Depends on Outer Loop
for i in range(n):
    for j in range(i):
        print(i, j)

ধরি:

n = 5

তাহলে:

i = 0 → 0 বার
i = 1 → 1 বার
i = 2 → 2 বার
i = 3 → 3 বার
i = 4 → 4 বার

Total:

0 + 1 + 2 + 3 + 4
= 10

General case:

0 + 1 + 2 + ... + (n-1)

এটি:

n(n-1) / 2

যা asymptotically:

O(n²)



1️⃣1️⃣ কেন j < i ব্যবহার করা হয়?

এটা খুব গুরুত্বপূর্ণ একটি pattern।

ধরি আমরা array-এর প্রতিটি unique pair নিয়ে কাজ করতে চাই।

numbers = [10, 20, 30, 40]

আমরা চাই:

10,20
10,30
10,40
20,30
20,40
30,40

কিন্তু চাই না:

10,10
20,20

এবং চাই না একই pair দুইবার:

10,20
20,10

তখন:

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        print(numbers[i], numbers[j])




1️⃣2️⃣ Dry Run

Array:

numbers = [10, 20, 30, 40]
i = 0
numbers[0] = 10

j:

1 → 2 → 3

Pairs:

10, 20
10, 30
10, 40
i = 1
numbers[1] = 20

j:

2 → 3

Pairs:

20, 30
20, 40
i = 2
numbers[2] = 30

j:

3

Pair:

30, 40
i = 3
j = range(4, 4)

কিছুই চলবে না।

Final pairs:

10,20
10,30
10,40
20,30
20,40
30,40




1️⃣3️⃣ 🔥 Important Pattern — i + 1

এই pattern-টি মনে রাখো:

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):

এটা ব্যবহার করা হয়:

একটি element-এর পরের element-গুলোর সাথে pair তৈরি করতে।

এটি ভবিষ্যতের অনেক DSA problem-এ কাজে লাগবে।




1️⃣4️⃣ Nested Loop দিয়ে Duplicate Detection

Lesson 15-এ আমরা duplicate দেখেছিলাম।

Brute-force version:

def find_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

    return -1

Input:

arr = [4, 2, 7, 2, 9]

Dry Run:

4 vs 2 → different
4 vs 7 → different
4 vs 2 → different
4 vs 9 → different

2 vs 7 → different
2 vs 2 → MATCH

তাই:

2

return হবে।




1️⃣5️⃣ Complexity

Outer loop প্রায়:

n

বার।

Inner loop মোটামুটি:

n

বার পর্যন্ত চলে।

তাই:

n × n

অর্থাৎ:

Time Complexity = O(n²)

Space:

i
j

মাত্র কয়েকটি variable।

তাই:

Space Complexity = O(1)




1️⃣6️⃣ Brute Force বনাম Optimized

Duplicate problem-এ:

Brute Force
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            return arr[i]

Complexity:

Time  → O(n²)
Space → O(1)
Set দিয়ে:
seen = set()

for x in arr:
    if x in seen:
        return x
    seen.add(x)

Complexity:

Time  → O(n) average
Space → O(n)

এখানে আমরা একটি গুরুত্বপূর্ণ concept দেখি:

⚖️ Time-Space Tradeoff
More Space
    ↓
Set ব্যবহার
    ↓
Time কমে

অর্থাৎ:

O(n²), O(1)
        ↓
O(n), O(n)



1️⃣7️⃣ Nested Loop-এর Real-Life Example

ধরো building-এ:

10 জন employee

প্রত্যেক employee-কে প্রত্যেক employee-এর সাথে compare করতে হবে।

তাহলে:

Employee 1 → 10 জনের সাথে
Employee 2 → 10 জনের সাথে
Employee 3 → 10 জনের সাথে
...

প্রায়:

10 × 10 = 100

comparisons।

যদি employee সংখ্যা n হয়:

n × n

তাই:

O(n²)



1️⃣8️⃣ O(n) বনাম O(n²)

ধরি:

n = 1,000
O(n)

প্রায়:

1,000

operations।

O(n²)
1,000 × 1,000
= 1,000,000

operations।

আর:

n = 10,000

হলে:

O(n)
→ 10,000

কিন্তু:

O(n²)
→ 100,000,000

🔥 তাই input বড় হলে O(n²) algorithm দ্রুত expensive হয়ে যায়।




1️⃣9️⃣ Nested Loop দেখলে কী করবে?

Interview-এ code দেখলে সঙ্গে সঙ্গে শুধু:

two loops = O(n²)

বলবে না।

বরং এই প্রশ্নগুলো করবে:

Step 1

Outer loop কতবার চলে?

n?
Step 2

Inner loop কতবার চলে?

n?
n/2?
i?
constant?
Step 3

দুটো multiply/aggregate করো।

যেমন:

n × n
→ O(n²)

অথবা:

n × 5
→ O(n)




2️⃣0️⃣ Nested Loop Complexity Cheat Sheet
Code Pattern	Complexity
for i in range(n)	O(n)
for i in range(n): for j in range(n)	O(n²)
for i in range(n): for j in range(5)	O(n)
for i in range(n): for j in range(n//2)	O(n²)
for i in range(n): for j in range(i)	O(n²)
for i in range(n): for j in range(i+1,n)	O(n²)




2️⃣1️⃣ Triple Nested Loop

এখন যদি:

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)

তাহলে:

n × n × n

অর্থাৎ:

O(n³)

এটা আরও expensive।




2️⃣2️⃣ কিন্তু তিনটি loop মানেই O(n³) নয়

উদাহরণ:

for i in range(n):
    print(i)

for j in range(n):
    print(j)

for k in range(n):
    print(k)

এগুলো nested নয়।

Sequentially চলছে:

n + n + n
= 3n

Big-O:

O(n)

🔥 তাই মনে রাখবে:

Sequential loops → যোগ হয়
Nested loops → সাধারণত multiply হয়




2️⃣3️⃣ Sequential বনাম Nested
Sequential
for i in range(n):
    ...

for j in range(n):
    ...

Complexity:

n + n
= 2n
= O(n)
Nested
for i in range(n):
    for j in range(n):
        ...

Complexity:

n × n
= n²
= O(n²)

এটা interview-এর জন্য অত্যন্ত গুরুত্বপূর্ণ।




2️⃣4️⃣ Nested Loop + Array = Brute Force

অনেক beginner DSA problem-এ আমরা প্রথমে এই approach দেখি:

Array
 ↓
Pick one element
 ↓
Compare with remaining elements
 ↓
Nested Loop
 ↓
Brute Force

Examples:

Duplicate detection
Pair Sum
All pairs
Maximum pair
Minimum pair
Counting combinations
Basic sorting algorithms

তারপর প্রশ্ন আসে:

Can we optimize O(n²) to O(n)?

এখান থেকেই শুরু হয়:

Set
Dictionary
Two Pointers
Sorting
Binary Search



2️⃣5️⃣ 🔥 Lesson 19-এর Core Pattern
Nested Loop
    ↓
Outer Loop
    ↓
Inner Loop
    ↓
Repeated Work
    ↓
n × n
    ↓
O(n²)

কিন্তু সবসময় loop count analyse করতে হবে।




2️⃣6️⃣ Interview Explanation 🎤
Q: What is a nested loop?

“A nested loop is a loop inside another loop. The inner loop executes for each iteration of the outer loop.”

Q: Why can nested loops have O(n²) complexity?

“If the outer loop runs n times and the inner loop also runs n times for each outer iteration, the total number of operations is n times n, which gives O(n²).”

Q: Are all nested loops O(n²)?

“No. The complexity depends on how many times each loop runs. For example, if the inner loop runs a constant number of times, the overall complexity can still be O(n).”

Q: Why is O(n²) called brute force sometimes?

“Because we often directly compare every possible pair or combination without using additional optimization techniques.”




📝 2️⃣7️⃣ One-Page Notes
🟢 LESSON 19 — NESTED LOOP

Nested Loop:
A loop inside another loop.

Example:

for i in range(n):
    for j in range(n):
        ...


Outer Loop = n
Inner Loop = n

Total:
n × n = n²

Time:
O(n²)


Important:

Nested loop ≠ always O(n²)

Example:

for i in range(n):
    for j in range(5):
        ...

n × 5
= O(n)


Variable inner loop:

for i in range(n):
    for j in range(i):
        ...

0 + 1 + 2 + ... + n
= O(n²)


Unique Pair Pattern:

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        ...


Used for:

→ Pair comparison
→ Duplicate detection
→ Brute Force
→ Combination problems


Sequential loops:

n + n
= O(n)


Nested loops:

n × n
= O(n²)


Triple nested:

n × n × n
= O(n³)


Key Rule:

Sequential → Add
Nested → Usually Multiply


Brute Force:
O(n²), O(1)

Optimized with Set:
O(n), O(n)

Concept:
Time-Space Tradeoff

"""