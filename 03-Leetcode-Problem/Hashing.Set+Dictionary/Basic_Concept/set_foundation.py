

# 1️⃣ Set কী?
# Python-এর Set হলো এমন একটি collection যেখানে unique values রাখা হয়।
numbers = {10, 20, 20, 30}
result = set(numbers) # তাহলে Set duplicate রাখবে না।
print(result)


# 2️⃣ List বনাম Set
# List
# Duplicate থাকতে পারে:
numbers = [10, 20, 10, 30]

# Set
# Duplicate not supported(unique value/fast lookup)
numbers = {10, 20, 30}
"""
| Feature         | List              | Set |

| Duplicate       | ✅ Allowed       | ❌ Not stored |
| Index           | ✅ Yes           | ❌ No |
| Ordered sequence | ✅ Yes          | Set-কে index-based ordered sequence হিসেবে ব্যবহার করা যায় না |
| Membership      | O(n)             | O(1) average |
| Main purpose    | Sequence         | Unique values / fast lookup |

"""


"""
3️⃣ Set-এর Main Purpose
Set-এর সবচেয়ে গুরুত্বপূর্ণ ব্যবহার:

Membership checking

অর্থাৎ:
“এই value-টা কি এখানে আছে?”

Example:
seen = {10, 20, 30}

Check:
20 in seen

Output:
True

আর:
50 in seen

Output:
False

"""


# 4️⃣ 🔥 List Search বনাম Set Search
# এটা আজকের সবচেয়ে গুরুত্বপূর্ণ concept।

# List Membership checking
numbers = [10, 20, 30, 40, 50]
if 50 in numbers:
   print("found")

# Python-কে list-এর মধ্যে search করতে হতে পারে:
# 10 → 20 → 30 → 40 → 50

# তাই:
# List membership = O(n)


# Set Membership checking
numbers = {10, 20, 30, 40, 50}
if 50 in numbers:
   print("found")

# Set-এর hash-based lookup ব্যবহার করে সাধারণ ক্ষেত্রে দ্রুত membership checking করা যায়।

# তাই:
# Set membership = O(1) average
# 🔥 এই difference-টাই Hashing-এর মূল শক্তি।


# 5️⃣ Set তৈরি করার দুটি উপায়
# Method 1 — Curly Braces
numbers = {10, 20, 30}

# Method 2 - set()
numbers = set()
# এটি একটি empty set তৈরি করে।



# 6️⃣ ⚠️ {} কেন Empty Set নয়?
# {}       → Empty Dictionary
# set()    → Empty Set

# Empty Dictionary
data = {}

# Empty Set:
data = set()



# 7️⃣ Set-এ Element Add করা
numbers = set()

numbers.add(10)
numbers.add(20)
numbers.add(30)

print(numbers)



# 8️⃣ Duplicate Add করলে কী হয়?
numbers = {10, 20, 30}
numbers.add(20)
print(numbers)
"""
কোনো error হবে না।
Set-এর মধ্যে 20 আগে থেকেই আছে।

তাই:
{10, 20, 30}

এই concept খুব গুরুত্বপূর্ণ।

“Set বলে: আমি একই value দ্বিতীয়বার আলাদা element হিসেবে রাখব না।”
"""



# 9️⃣ add() Example
data = set()

data.add(5)
data.add(10)
data.add(5)

print(data)
# 5 দুইবার add করার চেষ্টা করা হলেও একবারই থাকবে।
seen = set()

seen.add(5)
seen.add(10)
seen.add(5)

print(seen)


# 🔟 Set Membership — in
seen = {10, 20, 30}

print(50 in seen)
print(10 in seen)


# 1️⃣1️⃣ not in
# আমরা উল্টোটাও করতে পারি:
seen = {10, 20, 30}

if 10 in seen:
   print("10 is present")

##
seen = {100, 200, 300}

if 500 not in seen:
   print("500 is not present.")



# 1️⃣2️⃣ remove()
numbers = {10, 20, 30}

numbers.remove(20)
print(numbers)


"""
1️⃣3️⃣ ⚠️ remove()-এর গুরুত্বপূর্ণ বিষয়

যদি value Set-এর মধ্যে না থাকে:
numbers = {10, 20, 30}numbers.remove(50)

তাহলে:
KeyError
হবে।

তাই uncertainty থাকলে remove() সবসময় safest choice নয়।

"""


# 1️⃣4️⃣ discard() — Safe Remove
numbers = {10, 20, 30}

numbers.discard(30)
print(numbers)


# এখন value না থাকলেও:
# কোনো error হবে না।
numbers.discard(50)
print(numbers)

# তাই:
# remove()
# → Missing value হলে error

# discard()
# → Missing value হলেও no error



"""
1️⃣5️⃣ remove() vs discard():

Method	      Value থাকলে	      Value না থাকলে
remove(x)	   Remove	         KeyError
discard(x)	   Remove	         Nothing happens

"""



# 1️⃣6️⃣ len()
## Set
numbers = {10, 20, 30}
print(len(numbers))

# Duplicate থাকলেও unique element count হবে:
numbers = {10, 10, 20, 20, 30}
print(len(numbers))


## List 
numbers = [10, 20, 30, 40, 50]
print(len(numbers))

# Duplicate থাকলেও all element count হবে:
numbers = [10, 10, 20, 20]
print(len(numbers))



# 1️⃣7️⃣ clear()
numbers = {10, 20, 30}

numbers.clear()
print(numbers)

empty_set = numbers.clear()
print(empty_set)



# 1️⃣8️⃣ Set Traversal
# Set-এর elements iterate করা যায়:

numbers = {10, 20, 30}

for number in numbers:
   print(number)

# result = numbers[0]
# print(result)
# Set-কে list-এর মতো index-based sequence হিসেবে ব্যবহার করবে না।
# করলে error হবে।
# কারণ Set-এ list-এর মতো index access নেই।


# List 
numbers = [10, 20, 30]

for number in numbers:
   print(number)

# List index-based
numbers = [100, 200, 300, 400]

index = numbers[0]
print(index)

index = numbers[1]
print(index)



# 1️⃣9️⃣ কেন Set-এ Index নেই?
numbers = [10, 20, 30]

"""
এখানে:
index:
  0   1   2

তাই:
numbers[1]
possible।

কিন্তু Set-এর মূল উদ্দেশ্য:
Unique values
+
Fast membership

Index-based access নয়।

তাই:
numbers = {10, 20, 30}numbers[1]
করবে না।

"""



"""
2️⃣0️⃣ 🔥 Set-এর Order নিয়ে গুরুত্বপূর্ণ কথা
Set-কে sequence order-এর জন্য ব্যবহার করবে না।

যেমন:
numbers = {30, 10, 20}


তুমি Set-এর iteration দেখে কোনো নির্দিষ্ট list-style order ধরে algorithm লিখবে না।

তোমার মূল concern হবে:
Is this value present?

এবং:
Is this value unique?

"""
numbers = {30, 10, 20}

if 20 in numbers:
   print("20 is present")

numbers = {10, 10, 20, 30, 30}

if 20 in numbers:
   print("20 is unique")



# 2️⃣1️⃣ Set-এর মূল চারটি প্রশ্ন
# একটি Set দেখলে নিজেকে জিজ্ঞেস করবে:
seen = {1, 2, 3, 4, 5}

2 in seen
print("Yes -2 in seen.")

if 10 not in seen:
   print("Yes- 10 not in seen. ")

seen.add(6)
print(seen)

seen.remove(1)
print(seen)

seen.discard(6)
print(seen)



"""
2️⃣2️⃣ Set Complexity
এখন complexity।

সাধারণভাবে Python Set-এর জন্য:
Operation	      Average Complexity
x in set	         O(1)
x not in set	   O(1)
add(x)	         O(1) average
remove(x)	      O(1) average
discard(x)	      O(1) average
len(set)	         O(1)
clear()	         O(n)

Interview-এ in, add, remove নিয়ে সাধারণত বলবে:
Average O(1)

"""