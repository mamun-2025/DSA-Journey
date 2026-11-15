

# 1. Sorting কী?
"""
Sorting is the process of arranging data in a specific order, such as ascending order and descending order.

Sorting হলো Data-কে একটি নির্দিষ্ট ক্রমে সাজানোর প্রক্রিয়া।

সাধারণত দুই ধরনের Sorting বেশি ব্যবহার হয়:
1. Ascending Order (ছোট থেকে বড়)
2. Descending Order (বড় থেকে ছোট)

"""


# 2. Sorting কেন প্রয়োজন?
"""
ধরো, তোমার কাছে ১০০টি Product রয়েছে।

products = [450, 120, 800, 250, 100, 600]

এখন Customer যদি Price অনুযায়ী Low to High দেখতে চায়, তাহলে কী করবে?

তোমাকে Product-গুলো Price অনুযায়ী Sort করতে হবে।

বাস্তব উদাহরণ:
ব্যবহার	Sorting-এর কাজ
E-commerce	Price Low to High
Student Management	Marks High to Low
Banking	Transaction Date
Social Media	Latest Posts First
Search	Binary Search-এর জন্য Sorted Data
Database	Records Order করা

তোমার ShopSphere Project-এ ধরো:
Customer
   ↓
Select: Price Low to High
   ↓
Sort Products by Price
   ↓
Display Sorted Products

এখানে Sorting ব্যবহার করা হবে।


3. Ascending vs Descending Order
Ascending Order
ছোট থেকে বড়।
numbers = [5, 2, 8, 1, 9
numbers.sort()
print(numbers)

Output:
[1, 2, 5, 8, 9]


Descending Order
বড় থেকে ছোট।

numbers = [5, 2, 8, 1, 9]
numbers.sort(reverse=True)
print(numbers)

Output:
[9, 8, 5, 2, 1]

এখানে reverse=True ব্যবহার করলে Reverse Order-এ Sort হবে।

"""


# 3. Ascending vs Descending Order
# Ascending Order
numbers = [20, 30, 10, 40, 50]

numbers.sort()

print(numbers)

# Descending Order 
numbers = [20, 30, 10, 40, 50]

numbers.sort(reverse=True)

print(numbers)



# 4. Python Sorting — দুটি গুরুত্বপূর্ণ Method
"""
Python-এ Sorting করার জন্য প্রধানত দুটি Built-in Method রয়েছে:
1. list.sort()
2. sorted()
দুটোই Sorting করে, কিন্তু এদের মধ্যে একটি গুরুত্বপূর্ণ পার্থক্য রয়েছে।

Method 1 — list.sort()
Definition:

list.sort() হলো একটি List Method, যা Original List-কে সরাসরি পরিবর্তন করে Sorting করে।

এটিকে বলা হয়:

In-place Sorting
"""
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)

"""
এখন প্রশ্ন:

আগে Original List ছিল:
[50, 10, 40, 20, 30]

কিন্তু এখন:
[10, 20, 30, 40, 50]

কেন?
কারণ sort() Original List-কে পরিবর্তন করেছে।

গুরুত্বপূর্ণ বিষয়
result = numbers.sort()
print(result)

Output:
None

কেন?
কারণ list.sort() Sorted List Return করে না। এটি Original List পরিবর্তন করে এবং Return Value হিসেবে None দেয়।

এই ভুলটি Beginner-রা অনেক সময় করে।
"""
"""
Method 2 — sorted()
Definition:

sorted() হলো Python-এর Built-in Function, 
যা একটি নতুন Sorted List Return করে এবং Original Collection অপরিবর্তিত রাখে।
"""
numbers = [50, 10, 40, 20, 30]

result = sorted(numbers)

print(result)

print(numbers)

"""
এখানে:
- result → নতুন Sorted List।
- numbers → Original List, অপরিবর্তিত।

sort() vs sorted() — Main Difference

বিষয়	sort()	sorted()
Type	         List Method	                         Built-in Function
Original List	পরিবর্তন করে	                        পরিবর্তন করে না
New List	      তৈরি করে না	                         তৈরি করে
Return	      None	                              Sorted List
In-place    	Yes	                              No
ব্যবহার	      Original List পরিবর্তন করতে	         Original List সংরক্ষণ করতে

"""


# 5. Sorting-এর আরও কিছু গুরুত্বপূর্ণ বিষয়
# Reverse Sorting
numbers = [8, 2, 5, 1, 9]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# sorted()-এর ক্ষেত্রেও একইভাবে কাজ করে:
numbers = [8, 2, 5, 1, 9]

result = sorted(numbers)
print(result)
print(numbers)

result = sorted(numbers, reverse=True)
print(result)
print(numbers)



# String Sorting
# Sorting শুধু Number-এর জন্য নয়। String-ও Sort করা যায়।
names = ["Rahim", "Karim", "Abir", "Mamun"]

names.sort()
print(names)

names.sort(reverse=True)
print(names)

result = sorted(names)
print(result)

result = sorted(names, reverse=True)
print(result)
# Python সাধারণত String-এর Unicode ordering অনুযায়ী তুলনা করে।


# Sorting using key
# তুমি নামের Length অনুযায়ী Sort করতে চাও।
student = ["Abir", "Michale", "Ali", "Chiristopher"]

student.sort(key=len)
print(student)

result = sorted(student, key=len)
print(result)

# আরেকটি উদাহরণ:
products = [
   ("Laptop", 80000),
   ("Mouse", 500),
   ("Keyboard", 2500),
   ("Monitor", 12000),
]

products.sort(key=lambda item: item[1])
print(products)
"""
এখানে item[1] হলো প্রতিটি Product-এর Price।
তাই Price অনুযায়ী Sorting হয়েছে।
তোমার ShopSphere Project-এ Product Price, Name বা Date অনুযায়ী Sorting করতে এই key ধারণাটি কাজে লাগবে।
"""

# Stable Sorting
"""
Python-এর Sorting Algorithm হলো Timsort। এটি Stable Sorting Algorithm।
Stable Sorting বলতে বোঝায়:
একই Sorting Key থাকা Element-গুলোর মধ্যে তাদের আগের Relative Order বজায় রাখা।

উদাহরণ:
"""
students = [
    ("Rahim", 80),
    ("Abir", 80),
    ("Karim", 90),
    ("Mamun", 90)
]
students.sort(key=lambda student:student[1])
print(students)
"""
লক্ষ করো:
- 80 নম্বর পাওয়া Rahim আগে ছিল, Abir পরে ছিল। সেই Order বজায় রয়েছে।
- 90 নম্বর পাওয়া Karim আগে ছিল, Mamun পরে ছিল। সেই Order-ও বজায় রয়েছে।
"""



# 6. Sorting-এর Time Complexity
"""
Python-এর list.sort() এবং sorted() সাধারণভাবে Timsort Algorithm ব্যবহার করে।
Timsort একটি Hybrid Sorting Algorithm। 
এটি Merge Sort এবং Insertion Sort-এর ধারণা ব্যবহার করে।

Complexity:
Case	Time Complexity
Best Case	O(n)
Average Case	O(n log n)
Worst Case	O(n log n)

Space Complexity:
- list.sort() → Timsort-এর জন্য অতিরিক্ত Temporary Memory প্রয়োজন হতে পারে।
- sorted() → নতুন List তৈরি করে, তাই O(n) অতিরিক্ত Space লাগে; এর সঙ্গে Sorting-এর Temporary Memory-ও লাগতে পারে।

O(n log n) কেন?
ধরো, তোমার কাছে ৮টি Element আছে।

Sorting Algorithm-গুলো অনেক ক্ষেত্রে Data-কে ছোট ছোট অংশে ভাগ করে সাজানোর ধারণা ব্যবহার করে।
          8 Elements
              |
         Divide / Sort
          /       \
      4 Elements  4 Elements
       /    \       /    \
      2      2     2      2
              |
         Merge / Combine
              |
        Sorted Elements


এ ধরনের Divide and Conquer ভিত্তিক Sorting-এর ক্ষেত্রে সাধারণত:
O(n log n)

Complexity পাওয়া যায়।

মনে রাখবে, Python Timsort সরাসরি সাধারণ Merge Sort-এর মতো কাজ করে না; 
এটি আগে থেকেই থাকা Sorted Runs-ও কাজে লাগায়।
"""



# 7. কখন sort() এবং কখন sorted() ব্যবহার করব?
"""
Use sort()
Original List পরিবর্তন করতে চাইলে।
prices = [500, 100, 300]
prices.sort()

Result: Original List Sorted।


Use sorted()
Original Data সংরক্ষণ করে নতুন Sorted List চাইলে।
prices = [500, 100, 300]
sorted_prices = sorted(prices)

Result: Original List Unchanged।
"""