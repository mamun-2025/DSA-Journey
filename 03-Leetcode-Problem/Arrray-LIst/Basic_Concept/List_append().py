

# 1️⃣ append() কী?
# append() ব্যবহার করা হয়: List-এর শেষে একটি নতুন element যোগ করার জন্য।
# Syntax: list.append(value)

# Example:
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# append() দিয়ে একাধিকবার যোগ করা:
numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)

print(numbers)



# 2️⃣ Empty List + append()
result = []

for i in range(1, 10):
   result.append(i * 2)

print(result)

##
result = []
for number in [10, 20, 30]:
   result.append(number * 2)

print(result)



# 3️⃣ খুব গুরুত্বপূর্ণ — append() কী return করে?
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)


# কারণ append() list পরিবর্তন করে, কিন্তু নতুন list return করে না।
numbers = [10, 20, 30]
result = numbers.append(40)
print(result) # Output: None

# ✅ সঠিক
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)



# 4️⃣ append() একবারে একটি element যোগ করে
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

# TypeError: list.append() takes exactly one argument (2 given)
numbers = [1, 2, 3]
# numbers.append(4, 5)
# print(numbers) 
# এটা কাজ করবে না।
# কারণ append() একটি argument নেয়।



# 5️⃣ কিন্তু List append করলে কী হয় ?
numbers = [1, 2, 3]
numbers.append([4, 5])
print(numbers)
# আমরা 4 এবং 5 আলাদা করে যোগ করিনি।
# পুরো [4, 5]-কে একটি element হিসেবে যোগ করেছি।

numbers = [1, 2, 3]
numbers.append([4, 5])
print(numbers)
print(len(numbers))
"""
Length:
len(numbers)

হবে:
4

কারণ element হলো:
1
2
3
[4, 5]
মোট 4টি element।
"""


# 6️⃣ append() বনাম extend()
# append()
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# exytend()
numbers = [10, 20, 30]
numbers.extend([100, 200])
print(numbers)

"""
Mental Model:
append()
→ পুরো object-কে একটি element হিসেবে যোগ করে

extend()
→ iterable-এর elements আলাদা আলাদাভাবে যোগ করে
"""


# 7️⃣ append() + Traversal
# Even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = []

for number in numbers:
   if number % 2 == 0:
      result.append(number)
print(result)

# Odd numbers 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = []

for number in numbers:
   if number % 2 != 0:
      result.append(number)

print(result)



# 8️⃣ append() + String
# append() শুধু number-এর জন্য নয়।
names = []

names.append("Mamun")
names.append("Habib")
names.append("Jhon")
names.append("Michael")
print(names)



# 9️⃣ append() + Dictionary
# এমনকি dictionary-ও element হিসেবে append করা যায়।
users = []

users.append({"name": "Mamun"})
users.append({"age": 28})
users.append({"Blood": "B+"})
users.append({"City": "Madaripur"})
users.append({"Student": True})
users.append({"CGPA": 3.50})
print(users)
# এটা Django/backend development-এও conceptually কাজে লাগে—
# যখন আমরা একাধিক record/object/result সংগ্রহ করি।



# 🔟 append() Time Complexity
"""
এখন আসি DSA-এর গুরুত্বপূর্ণ অংশে।

সাধারণভাবে:
arr.append(value)

এর amortized / average time complexity:
O(1)

অর্থাৎ average ক্ষেত্রে list-এর শেষে নতুন element যোগ করা constant time-এর operation।

কিন্তু কেন সবসময় সরাসরি O(1) নয়?
Python list internally dynamic array-এর মতো কাজ করে।

ধরো:
[10, 20, 30, 40]

কিছু অতিরিক্ত capacity থাকতে পারে।
তখন নতুন element:
append(50)
সহজেই যোগ করা যায়।

কিন্তু capacity পূর্ণ হয়ে গেলে Python-কে বড় memory area allocate করে elements সরাতে হতে পারে।
সেই নির্দিষ্ট operation-এ বেশি সময় লাগতে পারে।

তাই interview-এ বলবে:
Appending to a Python list is O(1) amortized time.

"""


# 1️⃣1️⃣ Space Complexity
"""
যদি আমরা list-এ নতুন element যোগ করি, list-এর size বাড়ে।

তাই overall storage:
O(n)
হতে পারে।

তবে কোনো নির্দিষ্ট append() operation-এর auxiliary space নিয়ে কথা বললে 
বিষয়টি implementation-dependent; beginner/interview context-এ মূল complexity হিসেবে সাধারণত:
append → O(1) amortized time

এটাই বেশি গুরুত্বপূর্ণ।
"""



# 1️⃣2️⃣ Some Example
##
numbers = [-5, 2, 4, -7, 9, 1]

result = []

for number in numbers:
   if number > 0:
      result.append(number)

print(result)


## 
numbers = [-5, 2, 4, -7, 9, 1]
for number in numbers:
   if number > 0:
      print("Positive")
   elif number < 0:
      print("Negative")
   else:
      print("Zero")


## Important Pattern
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = []

for element in arr:
   if element % 2 == 0:
      result.append(element)

print(result)

##
result = []
result.append(100)
result.append(200)
result.append(300)
print(result)

##
numbers = [10, 13, 16, 27, 40, 23]

result = []

for number in numbers:
   if number % 2 == 0:
      result.append(number)

print(result)



# 1️⃣3️⃣ 🧠 আজকের One-Minute Revision: 
"""
append()
   ↓
List-এর শেষে element যোগ করে
   ↓
Original list modify করে
   ↓
Return value = None
   ↓
Average/Amortized Time = O(1)

সবচেয়ে গুরুত্বপূর্ণ pattern:

result = []

for x in arr:
    if condition:
        result.append(x)

"""









# 1️⃣4️⃣ Short Paragraph Interview questions
"""
🎯 Interview Questions
Q1. What does append() do?

Answer:
append() adds one element to the end of a Python list.

Q2. Does append() modify the original list?

Answer:
Yes. append() modifies the list in place.

Q3. What does append() return?

Answer:
It returns None.

Q4. What is the time complexity of append()?

Answer:
Python list append is O(1) amortized time.

Q5. What is the difference between append() and extend()?

Answer:
append() adds its argument as a single element, while extend() adds the elements from an iterable individually.



🎯 Paragraph
The append() method is used to add a new element to the end of a Python List.
It changes the original list directly and does not return a new list.
So we should use list.append(value) instead of assigning its result back to the list.
The append() method adds one element at a time, and if we append another list, the entire list is added as a single element.
A common pattern in problem solving is to create an empty result list, traverse the original list, process each element, 
and use append() to store the elements that meet a specific condition.
For example, we can use this pattern to create a new list containing only even or positive numbers.
Appending an element to a Python list takes 0(1) amortized time because 
Python lists use a dynamic-arry-like structure.
The key idea is that append() adds one item to the end of a list and is very useful for building result lists during problem solving.

বাংলা অর্থ

append() method ব্যবহার করা হয় Python List-এর শেষে একটি নতুন element যোগ করার জন্য। 
এটি original List-কে সরাসরি পরিবর্তন করে এবং নতুন কোনো List return করে না। 
তাই list.append(value) ব্যবহার করতে হবে; append()-এর result আবার List-এর মধ্যে assign করা উচিত নয়। 
append() একবারে একটি element যোগ করে এবং যদি আমরা একটি List-কে append করি, 
তাহলে পুরো List-টি একটি মাত্র element হিসেবে যোগ হয়। 
Problem solving-এ একটি খুব গুরুত্বপূর্ণ pattern হলো একটি empty result List তৈরি করা, 
original List traverse করা, প্রতিটি element process করা এবং 
কোনো element নির্দিষ্ট condition পূরণ করলে সেটিকে append() দিয়ে result List-এ যোগ করা। 
যেমন, এভাবে আমরা শুধু even number বা positive number নিয়ে একটি নতুন List তৈরি করতে পারি। 
Python List-এ একটি element append করতে O(1) amortized time লাগে, 
কারণ Python List dynamic-array-এর মতো কাজ করে। 
সহজভাবে মনে রাখবে: append() List-এর শেষে একটি item যোগ করে এবং problem solving-এর সময় result List তৈরি করতে এটি খুবই গুরুত্বপূর্ণ।

"""