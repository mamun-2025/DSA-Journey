


# 1.. Dictionary Access — Key থেকে Value বের করা
student = {
   "name": "mamun",
   "age": 26,
   "city": "madariput"
}

print(student["name"])
print(student["age"])
print(student["city"])

# print(student["salary"])
# কারণ "salary" Key Dictionary-তে নেই।

# .get() method
# তাই অনেক সময় .get() ব্যবহার করা নিরাপদ।
print(student.get("salary"))

# default value 
print(student.get("salary", 0))

# Interview point
# dict[key] raises KeyError when the key does not exist, 
# while dict.get(key, default) returns the default value.



# 2. Dictionary Add and Update
# Add 
student = {
   "name": "Mamun",
   "age": 26
}

student["department"] = "CSE"
print(student)

# Update
student = {
   "name": "Mamun",
   "age": 26
}

student["name"] = "Sanjib"
print(student)

"""
একই Syntax দিয়ে নতুন Key Add এবং পুরোনো Key Update করা যায়।

Condition	         Operation
Key নেই	            New Key Add
Key আছে	           Existing Value Update
"""



# 3. Frequency Counting কী?
# Frequency অর্থ হলো কোনো একটি element কতবার এসেছে।
# list 
numbers = [1, 2, 2, 1, 2, 3, 4]
"""
প্রতিটি Number কতবার এসেছে।
এখানে:
- 1 এসেছে 2 বার।
- 2 এসেছে 3 বার।
- 3 এসেছে 1 বার।
- 4 এসেছে 1 বার।
এটিই হলো Frequency Map।
"""



# 4. Frequency Map তৈরি করার Basic Logic
numbers = [1, 2, 2, 1, 2, 3, 4]

# প্রথমে একটি Empty Dictionary তৈরি করব।
frequency = {}

# List-এর প্রতিটি Number Traverse করব।
for number in numbers:

   # Number-টি Dictionary-তে আগে থেকেই আছে কি না পরীক্ষা করছি।
   if number in frequency:
      frequency[number] += 1 # আগে থেকে থাকলে তার Count এক বাড়াচ্ছি।
   else:
      frequency[number] = 1 # প্রথমবার এলে তার Count 1 দিয়ে শুরু করছি।

print(frequency)



"""
5. Dry Run — Frequency Map
Input:
numbers = [1, 2, 2, 3, 1]

Initial State:
frequency = {}


Step	   Current Number	   আগে Dictionary-তে আছে?	   Dictionary
1	      1	                     No	                     {1: 1}
2	      2	                     No	                     {1: 1, 2: 1}
3	      2	                     Yes	                  {1: 1, 2: 2}
4	      3	                     No	                     {1: 1, 2: 2, 3: 1}
5	      1	                     Yes	                  {1: 2, 2: 2, 3: 1}

Final Result:
{ 1: 2, 2: 2, 3: 1}

এই Dry Run-টি ভালোভাবে বোঝা জরুরি।

কারণ DSA-তে অনেক সময় পুরো Problem-এর মূল Logic এই Frequency Map-এর মধ্যেই থাকে।

"""



# 6. আরও সহজ পদ্ধতি — .get() দিয়ে Frequency Counting
numbers = [1, 2, 1, 2, 2, 3, 4]


frequency = {}

for num in numbers:
   frequency[num] = frequency.get(num, 0) + 1

print(frequency)

"""
এই একটি Line খুব গুরুত্বপূর্ণ:
frequency[num] = frequency.get(num, 0) + 1

চলো, এটিকে ভেঙে বুঝি।

ধরো:
frequency = {}num = 5

এখন:
frequency.get(5, 0)

যেহেতু 5 Key নেই, তাই Result হবে 0।

এরপর:
0 + 1

Result:
1

তাই:
frequency[5] = 1

এবার Dictionary:
{5: 1}



আবার 5 এলে:
frequency.get(5, 0)

এবার Result হবে 1।

তাই:
frequency[5] = 1 + 1

Result:
{5: 2}

Frequency Map-এর মূল Formula
count[x] = count.get(x, 0) + 1
আগে থাকলে Count বাড়াও, না থাকলে 1 থেকে শুরু করো।

"""



# 7. Frequency Counting — String-এর ক্ষেত্রে
# শুধু Number নয়, String-এর Character-এর Frequency-ও বের করা যায়।
# Basic frequency
text = "banana"

frequency = {}

for char in text:
   if char in frequency:
      frequency[char] += 1
   else:
      frequency[char] = 1

print(frequency)

# .get method
text = "banana"

frequency = {}

for cha in text:
   frequency[cha] = frequency.get(cha, 0) + 1

print(frequency)

# String-এর প্রতিটি Character-কে Dictionary-এর Key হিসেবে ব্যবহার করা যায়।





"""
8. Frequency Map-এর Practical Applications

Problem	                      Frequency Map কী কাজে লাগে?
Valid Anagram	               দুটি String-এর Character Count তুলনা
First Unique Character	      যে Character একবার এসেছে তা খোঁজা
Ransom Note	                  প্রয়োজনীয় Character পর্যাপ্ত আছে কি না
Majority Element	            Element কতবার এসেছে
Top K Frequent Elements	      সবচেয়ে বেশি আসা Elements বের করা
"""