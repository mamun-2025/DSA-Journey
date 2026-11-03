

# 1. Dictionary:
"""
Python Dictionary হলো একটি collection যেখানে প্রতিটি তথ্য Key → Value আকারে সংরক্ষিত থাকে।

বাস্তব উদাহরণ:

ধরো, একটি Student Database:
Student ID (Key)	Student Name (Value)
101	            Rahim
102	            Karim
103	            Mamun

এখানে:
- 101 হলো Key।
- Rahim হলো Value।
- 102 হলো Key।
- Karim হলো Value।

Python-এ:
"""
students = {
   101: "Rahim",
   102: "Karim",
   103: "Mamun"
}

print(students)



# 2. Dictionary vs List vs Set
"""
Feature	         List	         Set	         Dictionary
Structure	      Values	      Unique values	Key → Value
Duplicate	      Allowed	      Not allowed	   Keys unique
Index	            Yes	         No	            Access by key
Main purpose	   Store sequence	Membership	   Store related information
Lookup	         O(n)	         O(1) avg.	   O(1) avg.

"""
# List
numbers = [10, 20, 30]

# Set
numbers = {10, 20, 30}

# Dictionary
students = {
   "name": "Mamun",
   "age": 25
}
# Dictionary-তে name এবং age হলো Key, আর "Mamun" এবং 25 হলো Value।




# 3. Dictionary তৈরি করা
# Method 1:
person = {
   "name": "Mamun",
   "age": 25,
   "city": "Bashundhara"
}

# Method 2:
person = dict(
   name="Mamun",
   age=25,
   city="Madaripur"
)

# Empty dictionary:
data = {}
data = dict()

# Remember
empty_set = set()

empty_dict = {}
empty_dict = dict()



# 4. Dictionary থেকে Value Access করা
# Dictionary-তে Value বের করার জন্য Key ব্যবহার করি।
student = {
   "name": "Mamun",
   "age": 26,
   "department": "CSE"
}

result = student["name"]
print(result)
print(student["age"])
print(student["department"])

# student["name"] = এর অর্থ হলো "name" Key-এর Value বের করো।

# গুরুত্বপূর্ণ: Key না থাকলে কী হয়?
student = {
   "name": "Mamun",
   "age": 26
}
# print(student["salary"])
# KeyError: 'salary'
# কারণ Dictionary-তে "salary" Key নেই।




# 5. .get() Method
# .get() হলো Dictionary থেকে Value Access করার একটি নিরাপদ পদ্ধতি।

student = {
   "name": "Mamun",
   "age": 25
}

print(student.get("name"))

print(student.get("salary"))
# এখানে salary Key নেই, তাই Error না দিয়ে None দিয়েছে।

# Default value use:
student = {
   "name": "Mamun",
   "age": 26,
   "city": "Madaripur"
}

result = student.get("salary", 0)
print(result)

print(student.get("income", 0))
# অর্থাৎ Key না থাকলে আমরা নিজের পছন্দমতো Default Value দিতে পারি।

# interview Point:
# - dict[key] → Key না থাকলে KeyError।
# - dict.get(key) → Key না থাকলে None।
# - dict.get(key, default) → Key না থাকলে Default Value।



# 6. Dictionary-তে নতুন Value Add করা
student = {
   "name": "mamun",
   "age": 26
}

student["city"] = "Madaripur"
print(student)



# 7. Existing Value Update
student = {
   "name": "mamun",
   "age": 26
}
student["name"] = "habib"
print(student)
# এখানে নতুন Key তৈরি হয়নি। আগের name-এর Value পরিবর্তন হয়েছে।


# .update() Method
# একসঙ্গে একাধিক Value Update বা Add করা যায়।
student = {
   "name": "Mamun",
   "age": 26
}

student.update({
   "age": 27,
   "city": "Bashundhara"
})
print(student)




# 8. Dictionary থেকে Data Delete করা
# 1.del 
student = {
   "name": "mamun",
   "age": 25,
   "city": "Madaripur",
}

del student["age"]
print(student)

# 2.pop()
student = {
   "name": "mamun",
   "age": 25,
   "city": "Madaripur",
}

removed_value = student.pop("age")
print(removed_value)
# pop() Key-টি remove করে এবং তার Value return করে।

print(student)

# Default Value দিলে Key না থাকলেও Error এড়ানো যায়:
student = {
   "name": "mamun",
   "age": 25,
   "city": "Madaripur",
}

removed_value = student.pop("salary", 0)
print(removed_value)

# 3.clear()
student = {
   "name": "mamun",
   "age": 25,
   "city": "Madaripur",
}

student.clear()
print(student)
# এটি পুরো Dictionary খালি করে দেয়। {}




# 9. Dictionary Membership Checking
# Dictionary-তে in ব্যবহার করলে সাধারণত Key check করা হয়, Value নয়।
student = {
   "name": "Mamun",
   "age": 25
}

print("name" in student)
print("Mamun" in student)
print("Mamun" in student.values())
# "name" in student → Key আছে কি না।
# "Mamun" in student → "Mamun" নামে Key আছে কি না।
# "Mamun" in student.values() → Value আছে কি না।


print("age" in student)
print("city" in student)

# Dictionary membership checking by key is O(1) average.




# 10. Dictionary Traversal
# Dictionary-এর Data বিভিন্নভাবে Traverse করা যায়।
# A. শুধু Keys
student = {
    "name": "Mamun",
    "age": 25,
    "city": "Barisal"
}

for key in student:
   print(key)


# B. শুধু Values
student = {
    "name": "Mamun",
    "age": 25,
    "city": "Barisal"
}

for value in student.values():
   print(value)


# C. Keys এবং Values একসঙ্গে
student = {
    "name": "Mamun",
    "age": 25,
    "city": "Barisal"
}

for key, value in student.items():
   print(key, ":", value)

# items() Dictionary-এর Key-Value pairs দেয়।





# 11. Dictionary-এর Time Complexity
"""
Operation	            Average Time
Access dict[key]	      O(1)
.get(key)	            O(1)
Insert	               O(1)
Update	               O(1)
Delete / pop	         O(1)
Key membership in       O(1)
Traverse	               O(n)
.clear()	               O(n)

এগুলো Average Case Complexity। 
Hash collision বা resizing-এর কারণে কিছু Operation-এর Worst Case ভিন্ন হতে পারে।
"""