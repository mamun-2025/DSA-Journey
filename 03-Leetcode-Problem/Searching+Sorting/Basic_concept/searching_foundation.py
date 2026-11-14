

"""
1. Searching কী?
Searching হলো কোনো Collection বা Data Structure-এর মধ্যে নির্দিষ্ট একটি Data বা Element খুঁজে বের করার প্রক্রিয়া।

সহজ ভাষায়:

ধরো, তোমার কাছে একটি List আছে:
numbers = [10, 25, 30, 45, 50]


এখন তুমি জানতে চাও, এই List-এর মধ্যে 30 আছে কি না।

অথবা:
- 30 কোন Index-এ আছে?
- 100 List-এর মধ্যে আছে কি না?
- কোনো নাম বা সংখ্যা কোথায় রয়েছে?
এই কাজগুলো করার পদ্ধতিকে Searching বলে।

Real-life Example
ধরো, তোমার কাছে ১০০ জন শিক্ষার্থীর একটি তালিকা আছে।

তুমি Rahim নামের একজন শিক্ষার্থীকে খুঁজছ।

তুমি কী করবে?
- প্রথম শিক্ষার্থীর নাম দেখবে।
- না মিললে দ্বিতীয় শিক্ষার্থীর নাম দেখবে।
- এভাবে একে একে পরীক্ষা করবে।
- Rahim-কে পেলে Search বন্ধ করবে।
এটাই Searching-এর একটি সহজ উদাহরণ।



2. Searching কেন প্রয়োজন?
Programming-এ Searching অত্যন্ত গুরুত্বপূর্ণ।

বাস্তব Software-এর উদাহরণ:
Software	Searching-এর ব্যবহার
E-commerce	Product খোঁজা
Banking	Account খোঁজা
Student Management	Student ID খোঁজা
Social Media	User খোঁজা
Database	নির্দিষ্ট Record খোঁজা
Django Application	নির্দিষ্ট Product বা Order খোঁজা

তোমার ShopSphere E-commerce Project-এ ধরো, একজন Customer Product Search করল।
Customer
   ↓
Search "Laptop"
   ↓
Find Matching Products
   ↓
Display Results


এই পুরো প্রক্রিয়ার পেছনে Searching-এর ধারণা কাজ করে।



3. Linear Search কী?
First Searching Algorithm
Definition:

Linear Search is a searching algorithm that checks each element one by one until the target element is found or the collection ends.

বাংলা অর্থ:

Linear Search হলো এমন একটি Searching Algorithm, যেখানে একটি Collection-এর প্রতিটি Element একটির পর একটি পরীক্ষা করা হয়, যতক্ষণ না Target পাওয়া যায় অথবা Collection শেষ হয়।
Example
numbers = [10, 20, 30, 40, 50]target = 30

আমাদের Target হলো 30।

এখন আমরা একে একে পরীক্ষা করব।
Linear Search — Visual Dry Run
SEARCH PROGRESS
Step 0 of 5

10
Index 0
20
Index 1
30
Index 2
40
Index 3
50
Index 4

Target: 30। Start চাপলে Search শুরু হবে।

PreviousNext StepReset

আমরা দেখলাম:
Index 0 → 10 ≠ 30
Index 1 → 20 ≠ 30
Index 2 → 30 = 30

Target Found!

অর্থাৎ, Target পেতে আমাদের ৩টি Element পরীক্ষা করতে হয়েছে।

"""

# 4. Linear Search — Python Implementation
# Linear Search: Using for loop
numbers = [10, 20, 30, 40, 50]
target = 30

for i in range(len(numbers)):
   if numbers[i] == target:
      print("Target is found at index:", i)
      break

else:
   print("Target is not found.")



# Linear Search: Using Function
def linear_search(numbers, target):

   for i in range(len(numbers)):

      if numbers[i] == target:
         return i 

   return -1


numbers = [10, 30, 20, 40, 50]

result = linear_search(numbers, 30)
print("Target is found at index:", i)

result = linear_search(numbers, 100)
print("Target 100 is not found.")      


"""
5. Linear Search-এর Time Complexity

এখন সবচেয়ে গুরুত্বপূর্ণ বিষয়।

ধরো:
numbers = [10, 20, 30, 40, 50]

Target যদি প্রথম Element হয়:
10 → Found
Comparison লাগবে ১টি।

Target যদি শেষ Element হয়:
10 → 20 → 30 → 40 → 50
Comparison লাগবে ৫টি।

Target যদি List-এ না থাকে:
10 → 20 → 30 → 40 → 50 → Not Found
এক্ষেত্রেও ৫টি Comparison লাগবে।

তিন ধরনের Case
Case	পরিস্থিতি	Complexity
Best Case	প্রথম Element-এ পাওয়া যায়	O(1)
Average Case	মাঝামাঝি পাওয়া যায়	O(n)
Worst Case	শেষ Element বা Not Found	O(n)

O(n) মানে কী?
n হলো মোট Element-এর সংখ্যা।

Elements	Worst-case comparisons
10	10
100	100
1,000	1,000
10,000	10,000
100,000	100,000

অর্থাৎ, Input Size বাড়লে Searching-এর কাজও প্রায় একই অনুপাতে বাড়ে।

Linear Search — Growth
Worst-case comparisons for Linear Search.

n বাড়লে Worst-case comparisons-ও n-এর সঙ্গে বাড়ে।

Space Complexity:
Linear Search-এর এই Implementation-এ অতিরিক্ত কোনো বড় List বা Data Structure তৈরি হচ্ছে না।

তাই:
- Time Complexity: O(n) — Worst Case
- Space Complexity: O(1)

"""



# 6. এবার Binary Search-এর ধারণা
"""
Linear Search-এ আমরা একে একে Element পরীক্ষা করেছি।

কিন্তু একটি প্রশ্ন:

প্রতিবার একটি করে Element পরীক্ষা না করে যদি অর্ধেক Element বাদ দিতে পারি?

তাহলে Searching অনেক দ্রুত হতে পারে।

এটাই Binary Search-এর মূল ধারণা।
Binary Search-এর জন্য কী প্রয়োজন?
সাধারণ Binary Search-এ Array/List Sorted থাকতে হবে।

উদাহরণ:
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11

আমরা মাঝের Element পরীক্ষা করব।
- Middle Element যদি Target হয় → Found।
- Middle Element Target-এর চেয়ে ছোট হলে → বাম পাশ বাদ।
- Middle Element Target-এর চেয়ে বড় হলে → ডান পাশ বাদ।

প্রতিবার Search Space অর্ধেক হয়ে যায়।
Binary Search — Visual Understanding

Interactive Binary Search
TARGET = 11
Step 1

1
0
3
1
5
2
7
3
9
4
11
5
13
6
15
7

Blue = Active Search Space · Green = Middle

Middle = 7। 7 < 11, তাই বাম পাশ বাদ।
Next Step
এখানে প্রথমে ৭ পরীক্ষা করেছি।
7 < 11

তাই ৭ এবং তার বাম পাশের সব Element বাদ।

এরপর:
11 = 11


Target পাওয়া গেল।

মাত্র ২টি Comparison!

7. Linear Search vs Binary Search
বিষয়	Linear Search	Binary Search
Searching	One by one	Half by half
Sorted Data	প্রয়োজন নেই	সাধারণত প্রয়োজন
Best Case	O(1)	O(1)
Worst Case	O(n)	O(log n)
Space	O(1)	O(1)
Implementation	সহজ	তুলনামূলক কঠিন

কেন O(n) থেকে O(log n)?
ধরো, তোমার কাছে 1,024টি Element রয়েছে।

Linear Search-এর Worst Case:
1,024 Comparisons

Binary Search:
1024
  ↓
512
  ↓
256
  ↓
128
  ↓
64
  ↓
32
  ↓
16
  ↓
8
  ↓
4
  ↓
2
  ↓
1


এখানে সর্বোচ্চ ১১টি ধাপে একটি Element পর্যন্ত পৌঁছানো সম্ভব।

কারণ:

2^{10}=1024

অর্থাৎ:

log_2(1024)=10


Binary Search-এর Worst-case Complexity হলো O(log n)।
Comparison: 1,024 Elements
10–11

Binary Search — সর্বোচ্চ প্রায় ১১টি comparison

1,024
Linear Search — Worst Case

"""
class Solution:
   def binarySearch(self, nums: list[int], target: int) -> int:
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


"""
এখানে:
- left → Search Space-এর প্রথম Index।
- right → Search Space-এর শেষ Index।
- mid → মাঝের Index।

প্রতিটি Condition বুঝি
Condition 1:
if nums[mid] == target:    return mid

মাঝের Element Target-এর সমান হলে Index Return করব।

Condition 2:
elif nums[mid] < target:    left = mid + 1

মাঝের Element Target-এর চেয়ে ছোট হলে Target ডান পাশে থাকতে পারে।

তাই বাম পাশ বাদ দেব।

Condition 3:
else:    right = mid - 1

মাঝের Element Target-এর চেয়ে বড় হলে Target বাম পাশে থাকতে পারে।

তাই ডান পাশ বাদ দেব।

Loop শেষ:
return -1

Target পাওয়া না গেলে -1 Return করব।

"""


"""
Q1. What is Linear Search?

Answer: Linear Search is an algorithm that checks each element one by one until the target is found or the collection ends.

Q2. What is Binary Search?

Answer: Binary Search is an efficient searching algorithm that repeatedly divides a sorted search space into two halves.

Q3. Why is Binary Search faster than Linear Search?

Answer: Binary Search eliminates half of the remaining search space in each iteration, resulting in O(log n) time complexity.

Q4. Why does Binary Search require sorted data?

Answer: Because sorting allows us to determine which half of the search space can be safely eliminated.

Q5. What is the Space Complexity of Iterative Binary Search?

Answer: O(1), because it uses only a constant amount of extra space.

"""
