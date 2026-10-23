


"""
1️⃣ Duplicate Character কী?
যে character একবারের বেশি আসে তাকে duplicate character বলা যায়।

উদাহরণ:
"hello"

Characters:
h → 1
e → 1
l → 2
o → 1

এখানে:
l

duplicate।

কারণ l দুইবার এসেছে।



2️⃣ Unique Character কী?
যে character শুধু একবার আসে তাকে unique character বলা হয়।

"hello"-তে:
h → 1
e → 1
l → 2
o → 1

তাই:
h
e
o

unique।

"""



# 3️⃣ Problem — Duplicate আছে কি না?
# 4️⃣ Solution — Set ব্যবহার করে
text = "hello"

seen = set()

has_duplicate = False

for cha in text:
   if cha in seen:
      has_duplicate = True
      break

   seen.add(cha)


print(has_duplicate)

"""
🧠 Logic
আমরা একটি set রাখব:
seen = set()


এখানে আগে দেখা character রাখব।

Pattern:
Character
    ↓
Already seen?
   ↙      ↘
 Yes       No
  ↓         ↓
Duplicate   Add to set




5️⃣ Dry Run
Input:
hello

Step 1
ch = h

h set-এ নেই।
seen = {h}

Step 2
ch = e

e নেই।
seen = {h, e}

Step 3
ch = l

l নেই।
seen = {h, e, l}

Step 4
আবার:
ch = l

এবার:
l in seen


True ✅

অর্থাৎ duplicate পাওয়া গেছে।
has_duplicate = True

তারপর break।




6️⃣ 7-Step Rule
① Input কী?
"hello"

একটি string।
② Output কী?
String-এর মধ্যে duplicate আছে কিনা।
True

③ Logic কী?
প্রতিটি character seen set-এর মধ্যে আছে কিনা check করব।
- থাকলে → duplicate
- না থাকলে → set-এ add
④ Dry Run কী?
h → নতুন → add
e → নতুন → add
l → নতুন → add
l → already exists → duplicate

⑤ Time Complexity
প্রতিটি character সর্বোচ্চ একবার visit করছি।

Set membership average:
O(1)

তাই:

Time = O(n)
⑥ Space Complexity
Worst case-এ সব character unique হতে পারে।

তখন set-এ nটি character থাকবে।

Space = O(n)

⑦ Interview Explanation
"I use a set to keep track of characters that I have already seen. 
For each character, I check whether it is already in the set. 
If it is, I have found a duplicate. 
Otherwise, I add it to the set. 
The average time complexity is O(n) and the space complexity is O(n)."

"""



"""
7️⃣ যদি Duplicate না থাকে?
Input:
text = "python"


Characters:
p y t h o n

প্রতিটি character নতুন।

শেষে:
False

কারণ কোনো duplicate নেই।


8️⃣ Set কেন ব্যবহার করলাম?
কারণ আমাদের শুধু জানতে হবে:
"এই character আগে দেখেছি কি না?"

আমাদের frequency দরকার নেই।

তাই:
Need only existence?
        ↓
       SET

"""



# 9️⃣ Dictionary দিয়েও করা যায়
# Frequency count ব্যবহার করেও duplicate বের করতে পারি।
text = "Python"

frquency = {}

for cha in text:
   frquency[cha] = frquency.get(cha, 0) + 1

has_duplicate = False

for cha in frquency:
   if frquency[cha] > 1:
      has_duplicate = True
      break

print(has_duplicate)

# এটাও কাজ করবে।
# কিন্তু এখানে আমরা frequency হিসাব করছি, যদিও শুধু duplicate আছে কিনা জানতে চেয়েছি।
# তাই Set বেশি সরাসরি solution।



# 10️⃣ Problem — সব Character Unique কি?
text = "Python"

def is_unique(text):
   seen = set()

   for cha in text:
      if cha in seen:
         return False

      seen.add(cha)

   return True 

unique = is_unique(text)
print("Python_is_unique:", unique)

print(is_unique("hello"))



"""
🧠 এখানে নতুন একটি গুরুত্বপূর্ণ বিষয়
আমরা এখানে:
return False


ব্যবহার করেছি।

কারণ duplicate পাওয়া মাত্রই আমাদের আর পুরো string দেখতে হবে না।

এটি হলো Early Exit।


11️⃣ Best Case vs Worst Case
ধরুন:
"aaabcdef"

প্রথম দুই character:
a
a

দ্বিতীয় a-তেই duplicate পাওয়া গেল।

তাই অনেক input-এর ক্ষেত্রে দ্রুত শেষ হয়ে যাবে।
Best Case
O(1)
Worst Case
যদি শেষ পর্যন্ত duplicate না থাকে:

O(n)

Interview-এ সাধারণত বলবেন:
Worst-case time complexity is O(n).



12️⃣ First Unique Character
এবার আরও গুরুত্বপূর্ণ problem।
Problem
একটি string-এর প্রথম unique character বের করতে হবে।

Input:
"leetcode"

Frequency:
l → 1
e → 3
t → 1
c → 1
o → 1
d → 1

প্রথম unique character:
l

"""



# 13️⃣ Solution — Two Pass
# প্রথমে frequency count করব।
text = "leetcode"

frequency = {}

for cha in text:
   frequency[cha] = frequency.get(cha, 0) + 1

# তারপর আবার string traverse করব।
for cha in text:
   if frequency[cha] == 1:
      print(cha)
      break

# Full coade
text = "swiss"

frequency = {}

for cha in text:
   frquency[cha] = frequency.get(cha, 0) + 1

for cha in text:
   if frequency[cha] == 1:
      print(cha)
      break

"""
🧠 কেন দুইবার traverse?
প্রথমবার:
Character → Frequency

দ্বিতীয়বার:
Original order
      ↓
প্রথম যার frequency = 1

এখানে order গুরুত্বপূর্ণ।

Dictionary-তে unique character পাওয়া গেলেই সেটা first unique নাও হতে পারে, তাই original string-এ দ্বিতীয় traversal করি।




14️⃣ Dry Run — First Unique Character
Input:
"swiss"

Frequency:
s → 3
w → 1
i → 1

দ্বিতীয় traversal:
s → 3 ❌
w → 1 ✅

Answer:
w



15️⃣ 7-Step Rule
① Input
"swiss"

② Output
w

③ Logic
First pass
   ↓
Frequency count
   ↓
Second pass
   ↓
frequency == 1
   ↓
return first one

④ Dry Run
s → 3
w → 1
i → 1

s → not unique
w → unique → answer

⑤ Time
দুইবার traversal:
O(n) + O(n)

Big-O:

O(n)
⑥ Space
Dictionary-তে সর্বোচ্চ nটি character:

O(n)
⑦ Interview Explanation
"First, I build a frequency map for all characters. Then I traverse the original string again to preserve the original order. The first character whose frequency is one is the first unique character. The overall time complexity is O(n) and the space complexity is O(n)."



16️⃣ Important Pattern
আজকের পুরো Lesson-টি এইভাবে মনে রাখুন:
STRING
  ↓
TRAVERSE
  ↓
Need existence?
  ↓
SET

আর:
STRING
  ↓
TRAVERSE
  ↓
Need frequency?
  ↓
DICTIONARY

আর:
FIRST UNIQUE
  ↓
Frequency Map
  ↓
Traverse Original String
  ↓
First frequency == 1

"""


"""
🗣️ Interview Speaking Practice
Interviewer:
"How do you detect duplicate characters in a string?"

আপনি বলবেন:
"I use a set to keep track of characters I have already seen. 
For each character, I check whether it exists in the set. 
If it already exists, I return true because a duplicate is found. 
Otherwise, I add it to the set. 
The average time complexity is O(n) and the space complexity is O(n)."

"""


"""
⭐ আজকের Golden Rule

মনে রাখবেন:
Need to know:
"Have I seen this before?"
        ↓
      SET

Need to know:
"How many times did it appear?"
        ↓
   DICTIONARY

Need:
"First character appearing once?"
        ↓
Frequency Map
        +
Original String Traversal

এটাই আপনার String → Set/HashMap transition-এর প্রথম বড় ধাপ।

"""