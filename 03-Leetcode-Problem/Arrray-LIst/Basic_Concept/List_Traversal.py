

# 1️⃣ Traversal কী?
# একটি collection-এর প্রতিটি element একে একে visit করা।
numbers = [10, 20, 30, 40, 50]
# 10 → 20 → 30 → 40 → 50 - List Traversal



# 2️⃣ কেন Traversal দরকার?
# 1. Maximum খুঁজতে
max = [10, 7, 15, 40, 17] # প্রতিটি element check করতে হবে।

# 2. Sum করতে
sum = [1, 2, 3, 4, 5] # সবগুলো element যোগ করতে হবে।

# 3. Count করতে
count = [2, 3, 4, 2, 5, 2] # কতবার 2 আছে সেটা দেখতে হবে।

# 4. Search করতে
search = [10, 20, 30, 40] # 30 আছে কিনা দেখতে হবে।



# 3️⃣ Method 1 — Direct Value Traversal
numbers = [10, 20, 30, 40, 50]

for number in numbers:   # numbers list-এর প্রতিটি value একে একে number variable-এ রাখো।
   print(number)

# All numbers print
numbers = [10, 20, 30, 40, 50]

for number in numbers:
   print(number)




# 4️⃣ Dry Run
numbers = [10, 20, 30]
for number in numbers:
   print(number)

"""
First iteration
number = 10
print(10)

Second iteration
number = 20
print(20)

Third iteration
number = 30
print(30)

শেষে list-এ আর কোনো element নেই।
Loop শেষ।
"""


# 5️⃣ এখানে Index দরকার নেই
# আমরা index ব্যবহার করছি না।
# আমাদের শুধু value দরকার।

# যদি প্রশ্ন হয়:
# প্রতিটি number print করো।

for number in numbers:
   print(number)



# 6️⃣ Method 2 — Index দিয়ে Traversal
numbers = [10, 20, 30]

for i in range(len(numbers)): # এখানে i হলো index।
   print(numbers[i])

# Iteration 1: i = 0 
# numbers[0] = 10

# Iteration 2: i = 1
# numbers[1] = 20

# Iteration 3: i = 2
# numbers[2] = 30

# Loop End.


num1 = [10, 20, 30, 40, 50]
for i in range(1, len(num1)):
   print(num1[i])

num2 = [10, 20, 30, 40, 50]
for i in range(1, len(num2) - 1):
   print(num2[i])



# 7️⃣ দুই পদ্ধতির পার্থক্য
"""
Method 1:
for number in numbers:
    print(number)

এখানে আমরা পাই:
value

Method 2:
for i in range(len(numbers)):
    print(numbers[i])

এখানে আমরা পাই:
index
+
value

"""
# Situation 1 — শুধু Value দরকার 
# যদি তোমাকে বলা হয়: Print all numbers.
for number in numbers:  # কারণ এখানে index দরকার নেই।
   print(number)

### Just value(element)
arr = [10, 20, 30, 40]
for element in arr:
   print(element)

arr = [1, 2, 3,  4, 5]
for li in arr:
   print(li)


# Situation 2 — Index দরকার
numbers = [100, 200, 300, 400, 500]
for i in range(len(numbers)):
   print(f"Index:{i} = {numbers[i]}")

### Value + index
arr = [1, 2, 3,  4, 5]
for i in range(len(arr)):
   print(i)

arr = [10, 20, 30, 40]
for i in range(len(arr)):
   print(arr[i])

arr = [1, 2, 3,  4, 5]
for i in range(len(arr)):
   print(i, arr[i])

# Index + value
numbers = ["Mamun", 20, "Rahim", 40, 50]
for i in range(len(numbers)):
   print(i)

numbers = ["Mamun", 20, "Rahim", 3.14, True]
for i in range(len(numbers)):
   print(f"Index:{i} = {numbers[i]}")



# 8️⃣ কখন Index দরকার হয়?
"""
1. Modify the array
2. Replace an element
3. Compare with another index
4. Need previous/next element
5. Store the index
6. Use two pointers
7. Work with positions

"""



# 9️⃣ Modify করার জন্য Index
# আমরা প্রত্যেকটা number-এর সাথে 10 যোগ করতে চাই।
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
   numbers[i] += 10

print(numbers)



# 🔟 Traversal + Condition
numbers = [10, 15, 20, 25, 30]

for number in numbers:
   if number % 2 == 0:
      print(f"Even = {number}")

"""
Traversal
   ↓
Check condition
   ↓
Do something
"""
# Even numbers print
numbers = [15, 20, 17, 9, 6]

for number in numbers:
   if number % 2 == 0:
      print("Even:", number)



# 1️⃣1️⃣ Traversal + Counting
numbers = [1, 2, 2, 5, 4, 2]
count = 0

for number in numbers:
   if number == 2:
      count += 1

print("Total Count:", count)
"""
Traversal
+
Condition
+
Counter
"""
# Total numbers count
numbers = [5, 2, 5, 7, 5, 9]
count = 0

for number in numbers:
   if number == 5:
      count += 1

print(f"Total: {count}")



# 1️⃣2️⃣ Traversal + Maximum
numbers = [10, 25, 7, 40, 30]

maximum = numbers[0]

for number in numbers:
   if number > maximum:
      maximum = number

print("Maximum number:", maximum)

# Traversal + Minimum
numbers = [10, 25, 7, 40, 30]

minimum = numbers[0]

for number in numbers:
   if number < minimum:
      minimum = number

print(f"Minimum number: {minimum}")



# 1️⃣3️⃣ Time Complexity
numbers = [10, 20, 30, 40, 50]
# n = 5
# আমরা প্রতিটি element একবার করে visit করছি।
# 10 → visit
# 20 → visit
# 30 → visit
# 40 → visit
# 50 → visit

# if n = 100 , work = 100 times
# if n = 1000, work = 1000 times 
# if n = 1000000, work = 1 million times 
# So time complexity = 0(n)



# 1️⃣4️⃣ Space Complexity

for number in numbers:
    print(number)

# যদি আমরা নতুন কোনো list তৈরি না করি, তাহলে অতিরিক্ত memory খুব কম।
# তাই auxiliary space: O(1)



# 1️⃣5️⃣ 📝 7-Step Interview Framework
"""
1. Input কী?
arr = [10, 20, 30, 40]

2. Output কী?
Problem অনুযায়ী:
30

অথবা:
True / False

অথবা:
count

3. Logic কী?
Array traverse করে প্রতিটি element-এর উপর প্রয়োজনীয় operation করব।

4. Dry Run
প্রতিটি element একবার করে visit করব।

5. Time Complexity
O(n)
কারণ nটি element traverse করছি।

6. Space Complexity
সাধারণ traversal-এ অতিরিক্ত data structure না নিলে:
O(1)

7. Interview Explanation
I traverse the array from start to end and process each element once. 
Since every element is visited once, the time complexity is O(n).

"""


# 1️⃣6️⃣⭐ আজকের 8টি Key Point
"""
1. Traversal = প্রতিটি element একে একে visit করা।

2. for x in arr
   → যখন শুধু value দরকার।

3. for i in range(len(arr))
   → যখন index দরকার।

4. arr[i]
   → নির্দিষ্ট index-এর value।

5. Traversal সাধারণত O(n)।

6. Traversal + Condition
   → Search / Count / Filter.

7. Traversal + Compare
   → Maximum / Minimum.

8. Traversal + Index
   → Modify / Position-based problems.

"""


# 1️⃣7️⃣ Short Paragraph
"""
"List Traversal means visiting each element of a list one by one.
Usually from the beginning to the end.
In Python, we can traverse a list directly using 'for x in arr'
when we only need the values, or we can use 'for i in range(len(arr))'
when we need both the index and the value.
Traversal is important in problem solving because many tasks, 
such as searching, counting, finding the maximum and minimum, 
calculating a sum, comparing values, and modifying elements,
require us to examine the elements of a list. 
We can also combine traversal with conditions to perform specific operations,
such as finding even numbers or counting occurrences of a target value.
Since we usually visit each element once, the time complexity of a simple list traversal is 0(n),
while the extra space is generally 0(1) if we do no create another data structure."

বাংলা অর্থ:
List traversal বলতে একটি List-এর প্রতিটি element-কে সাধারণত শুরু থেকে শেষ পর্যন্ত এক এক করে visit করা বোঝায়। 
Python-এ যদি শুধু value দরকার হয়, তাহলে for x in arr ব্যবহার করে সরাসরি List traverse করা যায়। 
আর যদি index এবং value দুটোই দরকার হয়, তাহলে for i in range(len(arr)) ব্যবহার করা যায়। 
Problem solving-এ traversal খুবই গুরুত্বপূর্ণ, কারণ search করা, কোনো value কতবার আছে তা count করা, 
maximum বা minimum বের করা, sum হিসাব করা, value compare করা এবং element modify করার মতো 
অনেক কাজেই List-এর elementগুলো পরীক্ষা করতে হয়। 
আমরা traversal-এর সাথে condition ব্যবহার করে, 
যেমন শুধু even number বের করা বা কোনো target কতবার আছে তা count করার মতো কাজও করতে পারি। 
যেহেতু সাধারণ traversal-এ List-এর প্রতিটি element সাধারণত একবার করে visit করা হয়, 
তাই এর Time Complexity O(n) এবং নতুন কোনো data structure তৈরি না করলে সাধারণত extra Space Complexity O(1) হয়।
"""



