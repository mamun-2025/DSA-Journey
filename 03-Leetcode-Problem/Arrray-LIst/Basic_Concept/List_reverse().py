

# 1️⃣ reverse() কী?
# List-এর elements-এর order উল্টে দেয়।
numbers = [10, 20, 30, 40, 50]

numbers.reverse()
print(numbers)


# 2️⃣ reverse() Original List পরিবর্তন করে
numbers = [1, 2, 3, 4]

numbers.reverse()
print(numbers)

# অর্থাৎ numbers-এর নিজস্ব order পরিবর্তন হয়েছে।
# এটাকে বলে: In-place modification


# 3️⃣ In-place কী?
# In-place মানে:
# নতুন আলাদা result list তৈরি না করে existing list-টাকেই পরিবর্তন করা।

# Before:
# numbers
#    ↓
# [1, 2, 3, 4]

# After:
# numbers
#    ↓
# [4, 3, 2, 1]

# একই list object পরিবর্তিত হয়েছে।


# 4️⃣ reverse() কী Return করে?
# append()
numbers = [10, 20, 30]

numbers.append(40)
result = numbers.append(40)
print(numbers)
print(result)


# insert()
numbers = [10, 20, 30]

numbers.insert(0, 5)
result = numbers.insert(0, 5)
print(numbers)
print(result)


# reverse()
numbers = [10, 20, 30]

numbers.reverse()
result = numbers.reverse()
print(numbers)
print(result)
# reverse()
# → list modify করে
# → নতুন list return করে না
# → return = None



# 5️⃣ Dry Run
"""
ধরো:
numbers = [10, 20, 30, 40]

আমরা:
numbers.reverse()
করলাম।

Conceptually:
10 ↔ 40
20 ↔ 30

ফলে:
[40, 30, 20, 10]

"""



# 6️⃣ Reverse-এর ভিতরের Basic Idea
numbers = [10, 20, 30, 40, 50]

left = 0
right = 4

"""
Reverse operation-কে আমরা Two Pointer দিয়ে চিন্তা করতে পারি।

ধরো:
[10, 20, 30, 40, 50]

দুটি pointer:
left = 0
right = 4

Visual:
Index:   0    1    2    3    4
Value:  10   20   30   40   50
         ↑                   ↑
       left                right

প্রথমে:
10 ↔ 50

List:
[50, 20, 30, 40, 10]

তারপর:
left = 1
right = 3
20 ↔ 40

List:
[50, 40, 30, 20, 10]

তারপর pointers মাঝখানে আসে:
left = 2
right = 2
কাজ শেষ।

"""


# 🔥 7️⃣ Two Pointer দিয়ে Reverse
# Python-এর built-in reverse() না ব্যবহার করে আমরা নিজেরাও reverse করতে পারি।
numbers = [10, 20, 30, 40, 50]

left = 0
right = len(numbers) - 1

while left < right:
   numbers[left], numbers[right] = numbers[right], numbers[left]

   left += 1
   right -= 1

print(numbers)
"""
এখানে কী হচ্ছে?

প্রথমে:
left = 0
right = 4

Swap:
10 ↔ 50

Result:
[50, 20, 30, 40, 10]

তারপর:
left = 1
right = 3

Swap:
20 ↔ 40

Result:
[50, 40, 30, 20, 10]

তারপর:
left = 2
right = 2

এখন:
left < right

হলো:
2 < 2 → False

Loop শেষ।


# Real-Life Analogy
ধরো ৫ জন মানুষ লাইনে দাঁড়িয়ে:
Rahim → Karim → Hasan → Sakib → Rafi

লাইন উল্টে দিলে:
Rafi → Sakib → Hasan → Karim → Rahim

Reverse করার basic idea:
First ↔ Last
Second ↔ Second Last
Middle stays
এটাই two-pointer reverse-এর মূল ধারণা।



# এই Pattern কেন গুরুত্বপূর্ণ?
কারণ এটা শুধু reverse-এর জন্য নয়।
Two Pointers DSA-এর একটি অত্যন্ত গুরুত্বপূর্ণ pattern।

আজ আমরা শুধু basic idea নিচ্ছি:
left → শুরু
right → শেষ

দুজন একে অপরের দিকে এগিয়ে যায়
পরের Stage-এ আমরা Two Pointer আরও গভীরভাবে শিখব।
"""


# 8️⃣ Time Complexity
"""
ধরো:
n = 10
Reverse করার সময় প্রায় অর্ধেক elements-এর pair swap করতে হয়।

যদি:
n = 100
তাহলে প্রায় 50 pair।

যদি:
n = 1000
তাহলে প্রায় 500 pair।

Big-O অনুযায়ী:
O(n/2) = O(n)

তাই:
reverse() → O(n)


# Space Complexity
In-place reverse করলে নতুন list তৈরি করতে হয় না।

Two-pointer version:
left = 0
right = ...
শুধু কয়েকটি variable ব্যবহার করছি।

তাই extra/auxiliary space:
O(1)

⭐ Interview answer
Time = O(n)
Space = O(1)

"""



# 9️⃣ reverse() vs reversed()
numbers = [10, 20, 30]

numbers.reverse()
print(numbers)

# numbersed()
numbers = [10, 20, 30]

result = reversed(numbers)
print(result)
print(list(result))
# কারণ reversed() original list-কে in-place পরিবর্তন করে না; 
# এটি একটি reverse iterator দেয়।
"""
🧠 Mental Model
reverse()
↓
Original list change
↓
In-place
↓
Returns None


আর:
reversed()
↓
Reverse iterator
↓
Original list unchanged

"""



# 🔟 [::-1] দিয়েও Reverse করা যায়
numbers = [1, 2, 3, 4]

result = numbers[::-1]
print(result)
# কারণ slicing একটি নতুন list তৈরি করে।
"""
reverse()
→ in-place

[::-1]
→ নতুন list
"""



# 📊 1️⃣1️⃣ Comparison Table
"""
| Method           | Original List Change? | Result   |    Extra Space |
| ---------------- | --------------------- | -------- | -------------: |
| `arr.reverse()`  | ✅ Yes                 | `None`   | O(1) auxiliary |
| `reversed(arr)`  | ❌ No                  | Iterator | Iterator-based |
| `arr[::-1]`      | ❌ No                  | New List |           O(n) |
| Two-pointer swap | ✅ Yes                 | In-place |           O(1) |

"""



# 1️⃣2️⃣ Reverse + Index
numbers = [10, 20, 30, 40]

numbers.reverse()
print(numbers)
"""
Reverse করার পরে:
[40, 30, 20, 10]

নতুন index:
Index:   0    1    2    3
Value:  40   30   20   10

অর্থাৎ reverse করলে values-এর positions পরিবর্তিত হয়।
"""



# 1️⃣3️⃣ Reverse কি Sorting?
numbers = [10, 100, 20, 50]

numbers.reverse()
print(numbers)
# এটা sorted নয়।
# এটা শুধু বর্তমান order উল্টে দিয়েছে।

# sorting
numbers.sort()
print(numbers)
"""
reverse → order উল্টানো
sort → order অনুযায়ী সাজানো
"""

# Reverse the arr in-place simple python
arr = [10, 20, 30, 40, 50]

arr.reverse()
print(arr)

# Reverse the arr in-place two pointer
arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr) - 1

while left < right:
   arr[left], arr[right] = arr[right], arr[left]

   left += 1
   right -= 1

print(arr)
# Time complexity = 0(n)
# Space complexity = 0(1)



# 1️⃣4️⃣ 🎯 Interview Questions
"""
Q1. What does reverse() do?
= reverse() reverses the order of elements in a Python list in place.

Q2. What does reverse() return?
= It returns None.

Q3. What is the time complexity?
= O(n).

Q4. What is the extra space complexity?
= O(1), because the list can be reversed in place.

Q5. Difference between reverse() and reversed()?
= reverse() modifies the original list in place, while reversed() returns a reverse iterator without modifying the original list.

Q6. Can an array be reversed without extra array?
= Yes. We can use two pointers and swap elements from both ends.


Reverse Array
      ↓
Two Pointers
      ↓
left + right
      ↓
swap
      ↓
left++, right--
      ↓
O(n) Time
O(1) Space

“Reverse করতে হলে শুরু ও শেষ থেকে একসাথে এগিয়ে এসে pair-wise swap করা যায়।”

"""



# 1️⃣5️⃣ Short Paragraph
"""
The reverse() method is used to reverse the order of elements in a Python list. 
It modifies the original list in place, which means it does not create a separate result list,
and it returns None. For example, calling numbers.reverse() on [1, 2, 3, 4] 
changes the list to [4, 3, 2, 1]. 
Reversing a list can also be understood using the two-pointer technique, 
where one pointer starts at the beginning and another starts at the end, 
and their elements are swapped while the pointers move toward the center. 
This approach takes O(n) time and O(1) extra space. 
It is important to distinguish reverse() from reversed() and [::-1]: reverse() changes the original list, 
reversed() returns a reverse iterator without changing the original list, 
and [::-1] creates a new reversed list. 
Also, reversing a list is not the same as sorting it; 
reverse only changes the current order of the elements.


বাংলা অর্থ:
reverse() method ব্যবহার করা হয় Python List-এর elements-এর order উল্টে দেওয়ার জন্য। 
এটি original List-কে সরাসরি পরিবর্তন করে, অর্থাৎ আলাদা কোনো result List তৈরি করে না এবং এর return value হলো None। 
যেমন, [1, 2, 3, 4] List-এর ওপর numbers.reverse() ব্যবহার করলে List হয়ে যাবে [4, 3, 2, 1]। 
একটি List কীভাবে reverse করা যায়, সেটি two-pointer technique দিয়েও বোঝা যায়। 
সেখানে একটি pointer List-এর শুরু থেকে এবং আরেকটি শেষ থেকে শুরু করে, 
দুই পাশের elements swap করতে করতে মাঝের দিকে এগিয়ে যায়। 
এই approach-এর Time Complexity O(n) এবং Extra Space O(1)। 
এখানে reverse(), reversed() এবং [::-1]-এর পার্থক্যও গুরুত্বপূর্ণ: 
reverse() original List পরিবর্তন করে, reversed() original List পরিবর্তন না করে একটি reverse iterator দেয়, 
আর [::-1] একটি নতুন reversed List তৈরি করে। 
আর মনে রাখতে হবে, reverse করা আর sort করা এক জিনিস নয়—reverse() শুধু বর্তমান order উল্টে দেয়, 
কিন্তু sort() elements-কে নির্দিষ্ট order অনুযায়ী সাজায়।

"""
