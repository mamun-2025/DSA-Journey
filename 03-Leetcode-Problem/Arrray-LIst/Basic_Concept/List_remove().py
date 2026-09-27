

# 1️⃣ remove() কী?
# List-এর মধ্যে থাকা নির্দিষ্ট value-এর প্রথম occurrence-টি remove করে।
# Syntax: list.remove(value)
numbers = [10, 20, 30]

numbers.remove(20)
print(numbers)



# 2️⃣ remove() কীভাবে কাজ করে?
numbers = [10, 20, 30, 40]

numbers.remove(30)

# Python conceptually
"""
Search
  ↓
10 == 30 ? No
  ↓
20 == 30 ? No
  ↓
30 == 30 ? Yes
  ↓
Remove 30

Final:
[10, 20, 40]
অর্থাৎ remove()-এর আগে Python-কে value খুঁজতে হয়।

"""



# 3️⃣ Duplicate থাকলে কী হয়?
numbers = [10, 20, 20, 30]
numbers.remove(20)
print(numbers)
# শুধু প্রথম 20 remove হয়েছে।
# দ্বিতীয় 20 থেকে যায়।



# 4️⃣ remove() Return কী করে?
numbers = [100, 200, 300, 400]

result = numbers.remove(200)
print(result)
# remove()
# → list modify করে
# → removed value return করে না
# → return = None

"""
Metal Model: 

pop()
 ↓
INDEX
 ↓
remove by position
 ↓
returns removed value


remove()
 ↓
VALUE
 ↓
remove by value
 ↓
returns None

⭐ আজকের সবচেয়ে গুরুত্বপূর্ণ rule:
pop() = index/position-based removal
remove() = value-based removal


⭐ আজকের Master Note
remove()
│
├── Value দিয়ে কাজ করে
│
├── প্রথম matching occurrence remove করে
│
├── Original list modify করে
│
├── Return value = None
│
├── Value না থাকলে → ValueError
│
└── Time Complexity = O(n)
"""



# 5️⃣ Value না থাকলে কী হয়?
numbers = [10, 20, 30]

# numbers.remove(100)
# print(numbers)
# ValueError: list.remove(x): x not in list

# যদি নিশ্চিত না হও value আছে কিনা:
numbers = [10, 20, 30]

if 20 in numbers:
   numbers.remove(20)

print(numbers)
# এখানে আগে check করছি:
# 20 in numbers
# তারপর remove করছি।



# 6️⃣ String List-এ remove()
names = ["Mamun", "Karim", "Hasan"]

names.remove("Mamun")
print(names)



# 7️⃣ Mixed Data-তে remove()
data = ["Mamun", 28, 3.50, "Bepari", True]

data.remove(True)
print(data)

data.remove(3.50)
print(data)

data.remove("Mamun")
print(data)



# 8️⃣ List Object Remove করা
data = [[1,2], [3,4], [5,6]]

data.remove([3,4])
print(data)

# Output:
# [[1, 2], [5, 6]]
# কারণ [3, 4] একটি element হিসেবে ছিল।



# 9️⃣ remove() কি Index জানে?
"""
না।

তুমি যদি লেখো:
numbers.remove(2)

Python ধরে নেবে:
Value 2 remove করো।

এটা বলছে না:
Index 2 remove করো।

যদি index 2 remove করতে চাও:
numbers.pop(2)

"""

# Remove the value 30 form the list
arr = [10, 20, 30, 40, 50]

arr.remove(30)
print(arr)



# 🎯 Interview Questions
"""
1. What does remove() do?
= remove() remvoes the first occurrence of a specified value from a Python list.

2. Does remove() use index or value?
= It uses value.

3. What does remove return?
= It returns None.

4. What happens if the value doesn't exist?
= Python raises a ValueError.

5. What is the time complexity?
= remove() generally 0(n) because it may need to search the list and shift elements.

"""



# 🔟 Time Complexity
"""

এখন DSA-এর গুরুত্বপূর্ণ অংশ।

ধরো:
numbers = [10, 20, 30, 40, 50]

আমরা লিখলাম:
numbers.remove(40)

Python-কে প্রথমে search করতে হতে পারে:
10 → no
20 → no
30 → no
40 → yes

তারপর 40 remove করতে হবে এবং পরের elements shift করতে হতে পারে।

তাই সাধারণভাবে:
Time Complexity = O(n)

🔥 কেন O(n)?

কারণ value-এর অবস্থান আগে থেকে জানা নেই।

যদি:
numbers.remove(10)
হয়, প্রথম element-এই পাওয়া যাবে।

Best case:
O(1)

কিন্তু যদি value শেষের দিকে থাকে:
numbers.remove(50)
তাহলে অনেকগুলো element check করতে হবে।

Worst case:
O(n)
আর shifting-ও লাগতে পারে।

Interview-এ সাধারণভাবে বলবে:
remove() takes O(n) time in the worst case.



Best Case বনাম Worst Case:
ধরো:
arr = [10, 20, 30, 40, 50]

Best Case
arr.remove(10)
প্রথম element-এই value পাওয়া গেল।

Search:
10

তবে removal-এর পর বাকি elements shift করতে হয়, 
তাই overall operation-কে শুধু search-এর best-case দিয়ে বিচার করা উচিত নয়। 
Python list-এর remove সাধারণভাবে O(n) হিসেবে ধরা হয়।

Worst Case
arr.remove(50)

Search:
10 → 20 → 30 → 40 → 50
তারপর removal।

Overall:
O(n)

"""



# Short Paragraph
"""
The remove() method is used to remove the first occurrence of a
specified value from a Python list. Unlike pop(), which removes an element
by index and returns the removed value, remove() works with the 
itself and returns None. If the list contains duplicate values, 
only the first matching occurrence is removed.
If the specified value does not exist in the list, Python raises a ValueError.
The remove() operation generally takes 0(n) time because 
Python may need to search through the list to find the value and 
then shift the remaining elements after removing it.
It modifies the original list and usually requires 0(1) auxiliary space.
Therefore, we use remove() when we know the value we want to remove,
while we use pop() when we want ot remove an element based on its position or index.


বাংলা অর্থ:
remove() method ব্যবহার করা হয় Python List থেকে নির্দিষ্ট কোনো value-এর প্রথম occurrence remove করার জন্য। 
pop() যেখানে index ব্যবহার করে element remove করে এবং removed value return করে,
 সেখানে remove() সরাসরি value ব্যবহার করে এবং এর return value হলো None। 
 List-এ একই value একাধিকবার থাকলে remove() শুধুমাত্র প্রথম matching value-টি remove করে। 
 আর যে value remove করতে চাই সেটি List-এর মধ্যে না থাকলে Python ValueError দেখায়। 
 remove() সাধারণত O(n) সময় নেয়, কারণ Python-কে value খুঁজে বের করার জন্য List-এর elementগুলো search করতে হতে পারে 
 এবং remove করার পর বাকি elementগুলোকে shift করতে হতে পারে। 
 এটি original List-কে পরিবর্তন করে এবং সাধারণত O(1) auxiliary space ব্যবহার করে। 
 তাই সহজভাবে মনে রাখবে: যখন আমরা জানি কোন value remove করতে চাই, 
 তখন remove() ব্যবহার করি; আর যখন position বা index অনুযায়ী element remove করতে চাই, তখন pop() ব্যবহার করি।

"""
