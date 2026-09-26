

# 1️⃣ pop() কী?
# List থেকে একটি element remove করার জন্য এবং সেই removed element-টি return করার জন্য।

# Last element delete 
numbers = [10, 20, 30, 40]

numbers.pop()
print(numbers)
# List-এর শেষ element 40 remove করেছে।


# Last element delete and return
numbers = [10, 20, 30, 40]
removed = numbers.pop()
print(removed)
# এবং 40-কে return করেছে।



# 2️⃣ pop() এবং remove() এক নয়
## pop()
# ndex ব্যবহার করে remove করে এবং removed value return করে।
# তুমি চাইলে নির্দিষ্ট index-এর element remove করতে পারো।
numbers = [1, 2, 3, 4]

numbers.pop(0)
print(numbers)

##
numbers = [1, 2, 3, 4]
numbers.pop(1)
print(numbers)

##
numbers = [1, 2, 3, 4]

removed = numbers.pop(1)
print(numbers)
print(removed)


## remove()
# Value ব্যবহার করে প্রথম matching element remove করে।
numbers = [10, 20, 30, 40]

numbers.remove(10)
print(numbers)

##
numbers = [100, 200, 300, 400]

numbers.remove(200)
print(numbers)


## pop() without argument
# যদি কোনো index না দাও: তাহলে last element remove হবে।
numbers = [2, 4, 6, 8]

numbers.pop()
print(numbers)


## Negative Index দিয়ে pop()
numbers = [10, 20, 30, 40, 50]

removed = numbers.pop(-1) # -1 → last element
print(numbers)
print(removed)


"""
remove(value)
    ↓
Value দেখে remove

pop(index)
    ↓
Index দেখে remove
    ↓
Removed value return

"""




# 3️⃣ সবচেয়ে গুরুত্বপূর্ণ — pop() Complexity
"""

এখন DSA-এর আসল বিষয়।

যদি আমরা লিখি:
numbers.pop()
অর্থাৎ last element remove করি।

তাহলে:
Time Complexity = O(1)
কেন?

কারণ list-এর শেষ element remove করার জন্য অন্য elements-কে সরাতে হয় না।


# 1.pop(0) কেন O(n)?
____________________

এখন:
numbers = [10, 20, 30, 40, 50]

যদি লিখি:
numbers.pop(0)
তাহলে 10 remove হবে।

Result:
[20, 30, 40, 50]

কিন্তু এখানে একটা গুরুত্বপূর্ণ কাজ করতে হয়।
Original:

Index:   0    1    2    3    4
Value:  10   20   30   40   50

10 remove হওয়ার পরে:

20 → নতুন index 0
30 → নতুন index 1
40 → নতুন index 2
50 → নতুন index 3

অর্থাৎ বাকি elements-গুলোকে shift করতে হয়।

20 → ←
30 → ←
40 → ←
50 → ←

তাই:
pop(0) = O(n)


# 2.Visual Difference
______________________

pop()
[10, 20, 30, 40]
             ↑
          remove

No shifting
↓
O(1)

pop(0)
[10, 20, 30, 40]
 ↑
remove

20 → index 0
30 → index 1
40 → index 2

Elements shift
↓
O(n)


# 3.Complexity Table
____________________
Operation	Time Complexity
pop()	O(1)
pop(-1)	O(1)
pop(0)	O(n)
pop(i)	সাধারণত O(n)

কেন pop(i) সাধারণত O(n)?

যদি মাঝখান থেকে remove করো, তাহলে পরের elements-গুলো shift করতে হতে পারে।

"""



# 4️⃣ pop() দিয়ে Stack বানানো
# এখানে DSA-এর একটি গুরুত্বপূর্ণ connection আছে।
# Stack-এর principle:
# LIFO — Last In, First Out
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

stack.pop()
print(stack)
# অর্থাৎ:
# append → push
# pop    → remove from top
# এটা পরে Stack শেখার সময় খুব কাজে লাগবে।



# 5️⃣ Common Mistake — Empty List
numbers = []
# numbers.pop()

# তাহলে error হবে:
# IndexError: pop from empty list
# কারণ remove করার মতো কোনো element নেই।


# Safe Check:
numbers = []

if numbers: # মানে list-এ কোনো element আছে কিনা check করা।
   numbers.pop()



# 6️⃣ pop() vs remove()
"""
| Feature           | `pop()`                | `remove()`          |
| ----------------- | ---------------------- | ------------------- |
| কী দিয়ে কাজ করে? | Index                  | Value               |
| Default           | Last element           | নির্দিষ্ট value     |
| Return করে?       | Removed value          | `None`              |
| Example           | `arr.pop(2)`           | `arr.remove(20)`    |
| Main use          | Position-based removal | Value-based removal |

"""


# 7️⃣ nterview Question
"""
1. What does pop() do?
= pop() removes and returns an element form a Python list. Without an index, it removes the last element.

2. What is the compexity of pop()?
= Removing the last element with pop() is 0(1) amortized time.

3. What is the complexity of pop(0)?
= pop(0) takes 0(n) time because the remaining elements need to be shifted.

4. Difference between pop() and remove()?
= pop() removes an element by index and returns the removed value, while remove() removes the first mathing value and returns None.

"""


# 8️⃣ ⭐ আজকের Master Note
"""
pop()
│
├── শেষ element remove
├── removed value return করে
├── pop() → O(1) amortized
│
├── pop(index)
│     └── নির্দিষ্ট index remove
│
├── pop(0)
│     └── O(n)
│         কারণ elements shift করতে হয়
│
└── Empty list হলে → IndexError

🔥 সবচেয়ে গুরুত্বপূর্ণ DSA Rule

List-এর শেষে কাজ করা সাধারণত cheap; 
List-এর শুরুতে element remove/insert করলে shifting-এর কারণে O(n) হতে পারে।

"""



# 9️⃣ Short Paragraph
"""
The pop() method is used to remove an element from a Python list 
and return the removed value.
When we use pop() without an index, it removes the last element, 
while pop(index) removes the element at a specific index.
Unlike remove(), which removes an element by its value,
pop() works with an index and returns the removed element.
Removing the last element with pop() takes 0(1) amortized time
because no other elements need to be shifted, but pop(0) usually takes 0(n) time
because all the remaining elements have to be shifted to new polsitions.
The pop() method is also useful for implementing a stack
because a stack follows the LIFO principle,
meaning the last element added is the first one removed. 
If we try to pop from an empty list, Python raises an IndexError.

বাংলা অর্থ:
pop() method ব্যবহার করা হয় Python List থেকে একটি element remove করার জন্য 
এবং সেই removed value-টি return করার জন্য। 
আমরা যদি কোনো index না দিই এবং শুধু pop() ব্যবহার করি, 
তাহলে List-এর শেষের element remove হয়। আর pop(index) ব্যবহার করলে নির্দিষ্ট index-এর element remove হয়। 
emove()-এর সাথে pop()-এর পার্থক্য হলো, remove() value ব্যবহার করে element remove করে, 
কিন্তু pop() index ব্যবহার করে এবং removed element-টি return করে। 
List-এর শেষের element pop() দিয়ে remove করতে O(1) amortized time লাগে, 
কারণ অন্য element-গুলোকে shift করতে হয় না। 
কিন্তু pop(0) সাধারণত O(n) সময় নেয়, 
কারণ প্রথম element remove করার পর বাকি element-গুলোকে নতুন index-এ shift করতে হয়।
pop() Stack implement করতেও খুব গুরুত্বপূর্ণ, কারণ Stack LIFO (Last In, First Out) principle অনুসরণ করে
—অর্থাৎ সর্বশেষে যোগ করা element-টি প্রথমে বের হয়। 
আর যদি empty List থেকে pop() করার চেষ্টা করি, তাহলে Python IndexError দেখায়।

"""
