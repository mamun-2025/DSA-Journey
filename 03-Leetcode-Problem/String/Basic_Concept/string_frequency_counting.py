


"""
1️⃣ Frequency কী?
Frequency মানে:
কোনো character/value কতবার এসেছে।

ধরুন:
text = "banana"


Characters:
b a n a n a

Frequency:
b → 1
a → 3
n → 2

"""
# সবচেয়ে সহজ উপায় — count()
text = "banana"
result = text.count("a")
print(result)
print(text.count("n"))



# 2️⃣ নির্দিষ্ট Character Count
# আগে আমরা এভাবে করেছিলাম:
text = "banana"

count = 0

for cha in text:
   if cha == "a":
      count += 1

print(count)

"""
এখানে সমস্যা হলো—আমরা শুধু "a"-এর frequency জানছি।

কিন্তু যদি সব character-এর frequency জানতে চাই?

তখন Dictionary ব্যবহার করব।
"""

# আমরা যদি প্রত্যেক character-এর জন্য count() করি:
text = "banana"

for cha in text:
   print(cha, text.count(cha))

# এখানে সমস্যা হলো একই character বারবার এসেছে।
# আমরা চাই:
# b → 1
# a → 3
# n → 2
# এখানেই Dictionary / HashMap গুরুত্বপূর্ণ হয়ে যায়।




# 3️⃣ Dictionary দিয়ে Frequency Count
text = "banana"

frquency = {}

for cha in text:
   if cha not in frquency:
      frquency[cha] = 1
   else:
      frquency[cha] += 1

print(frquency)
"""
Interview Answer:
"I would use a dictionary to store each character as a key and its frequency as the value. 
I traverse the string once. 
If the character already exists in the dictionary, I increment its count; 
otherwise, I initialize it to one. 
This gives O(n) time complexity and O(n) space complexity in the worst case."
"""
"""
🧠 Logic বুঝুন
শুরুতে:
frequency = {}


মানে:
Empty Dictionary

প্রথম character
ch = 'b'

b dictionary-তে নেই।

তাই:
frequency['b'] = 1


এখন:
{'b': 1}

দ্বিতীয় character
ch = 'a'

a নেই।
frequency['a'] = 1


এখন:
{'b': 1, 'a': 1}

তৃতীয় character
ch = 'n'

তাই:
{'b': 1, 'a': 1, 'n': 1}

চতুর্থ character
আবার:
ch = 'a'

কিন্তু এবার a আছে।

তাই:
frequency['a'] += 1


হয়ে গেল:
{'b': 1, 'a': 2, 'n': 1}

পঞ্চম character
n

তাই:
n → 2

ষষ্ঠ character
a

তাই:
a → 3

Final:
{'b': 1, 'a': 3, 'n': 2}

"""



"""
4️⃣ Dry Run Table
Input:
banana

Step	Character	Dictionary
1	      b	      {b:1}
2	      a	      {b:1, a:1}
3	      n	      {b:1, a:1, n:1}
4	      a	      {b:1, a:2, n:1}
5	      n	      {b:1, a:2, n:2}
6	      a	      {b:1, a:3, n:2}

🔥 Dry Run
Input:
text = "banana"


শুরুতে:
frequency = {}


Iteration 1
ch = 'b'
'b' নেই

তাই:
frequency['b'] = 1

Dictionary:
{'b': 1}

Iteration 2
ch = 'a'

a নেই।
{'b': 1, 'a': 1}

Iteration 3
ch = 'n'

n নেই।
{'b': 1, 'a': 1, 'n': 1}

Iteration 4
ch = 'a'

এবার a আছে।
frequency['a'] += 1


তাই:
{'b': 1, 'a': 2, 'n': 1}

Iteration 5
ch = 'n'

n আগে থেকেই আছে।
{'b': 1, 'a': 2, 'n': 2}

Iteration 6
ch = 'a'

আবার a:
{'b': 1, 'a': 3, 'n': 2}

Final Answer
b → 1
a → 3
n → 2




5️⃣ 7-Step Rule
① Input কী?
"banana"

একটি string।
② Output কী?
প্রতিটি character-এর frequency:
b → 1
a → 3
n → 2

③ Logic কী?
String
 ↓
একটি একটি character নাও
 ↓
Dictionary-তে আছে?
 ↓
না → 1
হ্যাঁ → +1

④ Dry Run কী?
b → 1
a → 1
n → 1
a → 2
n → 2
a → 3

⑤ Time Complexity
String length = n

আমরা প্রতিটি character একবার traverse করছি।

Dictionary lookup average:
O(1)

তাই:

Time = O(n)
⑥ Space Complexity
Worst case-এ প্রতিটি character আলাদা হতে পারে।

যেমন:
"abcdef..."

তখন dictionary-তে nটি key থাকতে পারে।

তাই:

Space = O(n)


⑦ Interview Explanation
"I use a dictionary to store the frequency of each character. 
I traverse the string once, 
and for every character I either initialize its count to one or increment its existing count. 
The average time complexity is O(n), and the space complexity is O(n) 
because the dictionary can store up to n distinct characters."

"""



# 6️⃣ আরও সহজ Python Syntax
# একই কাজ get() দিয়ে করা যায়।
text = "banana"

frquency = {}

for cha in text:
   frquency[cha] = frquency.get(cha, 0) + 1 # ch dictionary-তে থাকলে তার value দাও, না থাকলে 0 দাও।

print(frquency)



"""
# Edge Cases
Frequency counting-এর সময় এগুলো ভাববেন।
Empty String
text = ""


Result:
{}

One Character
text = "a"


Result:
{'a': 1}

All Same
text = "aaaa"


Result:
{'a': 4}

All Unique
text = "abc"


Result:
{'a': 1, 'b': 1, 'c': 1}

"""
"""
7️⃣ get() কীভাবে কাজ করে?
ধরুন:
frequency = {'b': 1}


এখন:
frequency.get('b', 0)


Result:
1

কিন্তু:
frequency.get('a', 0)


Result:
0

তাই:
frequency[ch] = frequency.get(ch, 0) + 1


মানে:
আগের count
     +
    1

"""



# 8️⃣ Frequency দিয়ে Most Frequent Character
# এবার frequency count ব্যবহার করে সবচেয়ে বেশি আসা character বের করা যায়।
text = "banana"

frquency = {}

for cha in text:
   frquency[cha] = frquency.get(cha, 0) + 1

maximum = 0
answer = ""

for cha in frquency:
   if frquency[cha] > maximum:
      maximum = frquency[cha]
      answer = cha 

print(answer)



"""
9️⃣ Interview Pattern Recognition
Problem:
"Find the frequency of each character."

আপনার মাথায় আসবে:
String
 ↓
Traversal
 ↓
Dictionary
 ↓
Frequency

Problem:
"Find the most frequent character."

ভাববেন:
String
 ↓
Frequency Map
 ↓
Find Maximum

Problem:
"Check whether two strings are anagrams."

ভাববেন:
String
 ↓
Frequency
 ↓
Dictionary

এটাই Pattern Recognition।

"""

"""
⭐ আজকের Core Pattern
এটা মনে রাখবেন:
COUNT ONE CHARACTER
        ↓
if ch == target
        ↓
count += 1

আর—
COUNT ALL CHARACTERS
        ↓
Dictionary
        ↓
frequency[ch] += 1

Golden Rule
একটি নির্দিষ্ট জিনিস count → সাধারণ counter যথেষ্ট।
অনেকগুলো জিনিসের frequency → HashMap/Dictionary ব্যবহার করুন।

"""
