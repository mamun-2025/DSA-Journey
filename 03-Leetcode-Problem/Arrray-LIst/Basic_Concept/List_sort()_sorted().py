

# 1️⃣ Sorting কী?
# Sorting মানে হলো data-কে একটি নির্দিষ্ট order-এ সাজানো।
numbers = [40, 20, 50, 10, 30]

numbers.sort()
print(numbers)
"""
Ascending order:
[10, 20, 30, 40, 50]

Descending order:
[50, 40, 30, 20, 10]

সাধারণভাবে:
Ascending
↓
ছোট → বড়

Descending
↓
বড় → ছোট

"""



# 2️⃣ sort() কী?
# Python List-এর sort() method existing list-কে in-place sort করে।
arr = [9, 5, 1, 7, 3]

arr.sort() # arr-এর নিজের order পরিবর্তন হয়েছে।
print(arr)



# 3️⃣ sort() = In-place
# sort() original list পরিবর্তন করে।
arr = [500, 300, 100, 400, 200]

arr.sort()
print(arr)



# 4️⃣ sort() কী Return করে?
numbers = [30, 10, 20]

result = numbers.sort()
print(result)

"""
sort()
↓
original list modify করে
↓
নতুন list return করে না
↓
return = None
"""



# 5️⃣ Ascending Order
numbers = [30, 10, 50, 40, 20]

numbers.sort()
print(numbers)



# 6️⃣ Descending Order
numbers = [30, 10, 50, 40, 20]

numbers.sort(reverse=True)
print(numbers)
# reverse=True
# এর অর্থ:
# Sorting order উল্টে দাও।




# 7️⃣ reverse=True মানে কী?
"""
এখানে একটা বিষয় পরিষ্কার রাখা দরকার।

numbers.sort(reverse=True)
এটা শুধু:
sort → তারপর reverse

এই ধারণা দিয়ে ভাবা যায়, কিন্তু Python implementation internally কীভাবে sorting করে সেটা আলাদা বিষয়।

তোমার জন্য এখন গুরুত্বপূর্ণ:
reverse=False
→ ascending

reverse=True
→ descending

"""
numbers = [30, 10, 50, 40, 20]

numbers.sort()
numbers.sort(reverse=False) 
# Two same (reverse = False (ascending)-small to big)
print(numbers)


numbers = [30, 10, 50, 40, 20]
numbers.sort(reverse=True)  
# reverse = True (descending)-big to small
print(numbers)




# 8️⃣ sorted() কী?
# sorted() একটি built-in function।
numbers = [40, 10, 30, 20]

result = sorted(numbers)
print(result)
# sorted() original list পরিবর্তন করে না; একটি নতুন sorted list তৈরি করে।




# 9️⃣ sort() vs sorted()
"""
| Feature                 | `sort()`       | `sorted()`        |
| ----------------------- | -------------- | ----------------- |
| Type                    | List method    | Built-in function |
| Original list পরিবর্তন? | ✅ Yes          | ❌ No              |
| New list তৈরি?          | ❌              | ✅                 |
| Return                  | `None`         | Sorted list       |
| Ascending               | Default        | Default           |
| Descending              | `reverse=True` | `reverse=True`    |

"""



# 🔟 Visual Difference
"""
# sort()
numbers
   ↓
[40, 10, 30, 20]

numbers.sort()

   ↓

numbers
   ↓
[10, 20, 30, 40]

একই list পরিবর্তিত হয়েছে।


# sorted()
numbers
   ↓
[40, 10, 30, 20]

sorted(numbers)
       ↓
[10, 20, 30, 40]

Original:

numbers
   ↓
[40, 10, 30, 20]

অপরিবর্তিত থাকে।

"""



# 1️⃣1️⃣ কখন sort() ব্যবহার করব?
# যখন: Original list পরিবর্তন করতে আমার সমস্যা নেই।
numbers = [5, 2, 8, 1]

numbers.sort()
print(numbers)
# যদি original order দরকার না হয় → sort() ভালো।



# 1️⃣2️⃣ কখন sorted() ব্যবহার করব?
# যখন: Original list-টি রেখে একটি sorted copy দরকার।
numbers = [5, 2, 8, 1]

sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)




# 1️⃣3️⃣ sorted() + Descending
numbers = [10, 40, 20, 30]

result = sorted(numbers, reverse=True)
print(result)




# 1️⃣4️⃣ String Sorting
# অর্থাৎ strings-ও sort করা যায়।
# Output সাধারণত lexicographic/alphabetical order অনুযায়ী:
names = ["Benet", "Alfred", "Danny", "Cathay"]

names.sort()
print(names)



# 1️⃣5️⃣ Duplicate থাকলে?
# Sorting ≠ Remove Duplicate
numbers = [2, 1, 5, 3, 2, 6, 2]

numbers.sort()
print(numbers)

"""
Duplicate values remove হয়নি।

এটা খুব গুরুত্বপূর্ণ:
sort()
→ শুধু order পরিবর্তন করে
duplicate remove করে না


Duplicate remove করতে আলাদা logic লাগবে।
এটা আমরা সামনে Remove Duplicates problem-এ করব।

"""



# 1️⃣6️⃣ Time Complexity
"""
Python-এর built-in sorting algorithm-এর সাধারণ worst-case time complexity:
O(n log n)

তাই:
sort()
→ O(n log n)

sorted()
→ O(n log n)

Interview-এর জন্য এইটা মনে রাখো।

"""




# 1️⃣7️⃣ Space Complexity
"""
এখানে একটু careful হতে হবে।

sorted()
এটি নতুন sorted list তৈরি করে।

তাই result-এর জন্য:
O(n)
additional/result space লাগে।

sort()
এটি in-place sorting method। 
Python-এর sorting implementation internally temporary memory ব্যবহার করতে পারে, 
তাই এটাকে algorithmically একেবারে "zero memory" বলা ঠিক নয়।

Junior interview-এর practical level-এ:

sort()
→ in-place
→ extra memory implementation-dependent

sorted()
→ new list
→ O(n) result space

এখন তোমার DSA notes-এ এই distinction রাখাই ভালো।

"""



# 1️⃣8️⃣ key= — খুব গুরুত্বপূর্ণ
names = ["Mansur", "Ali", "Hasan", "K2"]

names.sort(key=len) # Length অনুযায়ী sort করতে চাই:
print(names)
"""
Python sorting-এর একটি powerful feature হলো:

key=
এটি বলে দেয়:
কোন property/value অনুযায়ী sorting করতে হবে।

names.sort(key=len)
এর মানে:

প্রতিটি string-এর length দেখো
↓
length অনুযায়ী sort করো

"""



# 1️⃣9️⃣Dictionary/Object Data Sort
students = [
   {"name": "Rahim", "age": 22},
   {"name": "Karim", "age": 25},
   {"name": "Hasan", "age": 19}
]

students.sort(key=lambda student: student["age"]) # প্রতিটি student dictionary থেকে age value নিয়ে sorting করো।
print(students)
# এটা পরে Django QuerySet-এর ordering বুঝতেও conceptually সাহায্য করবে |



# 2️⃣0️⃣ Descending + key
# বড় age থেকে ছোট age:
students = [
   {"name": "Rahim", "age": 22},
   {"name": "Karim", "age": 25},
   {"name": "Hasan", "age": 19}
]

students.sort(
   key=lambda student: student["age"],
   reverse=True
)
print(students)




# 2️⃣1️⃣ sort() + sorted() +  reverse() এক জিনিস নয়
# reverse()
numbers = [50, 40, 10, 30, 20]

numbers.reverse()
print(numbers)
# শুধু বর্তমান order উল্টেছে।

# sort()
numbers = [50, 40, 10, 30, 20]

numbers.sort()
print(numbers)
# Value অনুযায়ী সাজিয়েছে।

# sorted()
numbers = [50, 40, 10, 30, 20]

result = sorted(numbers)
print(result)
# numbers → original থাকে
# result  → sorted list



# 2️⃣2️⃣ 🎤 Interview Questions
"""
1. Difference between sort() and sorted() ?
= sort() is a list method that sorts the original list in place, 
  while sorted() is a built-in function that returns a new sorted list without modifying the original list.

2. What does list.sort() return?
= It returns None.

3. What is the typical worst-case time complexity of Python sorting?
= It's time complexity 0(n log n).

4. How do you sort in descending order?
= arr.sort(reverse=True) 
  or sorted_arr = sorted(arr, reverse=True)

5. Does sorting remove duplicate?
= No, Sorting != Duplicate Removal

6. How do you sort strings by length?
= names.sort(key=len)

"""




# 2️⃣3️⃣






















# 2️⃣2️⃣
