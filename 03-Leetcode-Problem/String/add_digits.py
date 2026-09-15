

class Solution:
   def addDigits(self, num: int) -> int:

      while num >= 10:

         digit_sum = 0

         while num > 0:
            last_digit = num % 10
            digit_sum += last_digit
            num //= 10

         num = digit_sum

      return num

"""
 I repeatedly calculate the sum of the digits until the number becomes a single digit.
 I use the modulo operator to extract the last digit and integer division to remove it.
 I store the sum of the digits and use it as the new number for the next iteration.
 The time complexity is 0(log n) and 
 the space complexity is 0(1).

 """

"""
🟢 LeetCode 258 — Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
🎯 Step 1 — Problemটা আসলে কী বলছে?

Original statement:

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

সহজ বাংলায়:

আমাদের একটি integer num দেওয়া আছে।

আমাদের তার সব digit যোগ করতে হবে।

যদি যোগ করার পরে আবার দুই বা তার বেশি digit থাকে, তাহলে আবার সেই সংখ্যার digitগুলো যোগ করতে হবে।

এভাবে করতে হবে যতক্ষণ না একটি মাত্র digit থাকে।

1️⃣ Input কী?
num

একটি integer।

Example:

38
2️⃣ Output কী?

একটি single-digit integer।

Example:

38 → 2
3️⃣ সবচেয়ে গুরুত্বপূর্ণ শব্দ — repeatedly

Problem-এ আছে:

repeatedly add

repeatedly মানে:

বারবার করা।

অর্থাৎ একবার digit sum করলেই শেষ নয়।

Example:

38
↓
3 + 8
↓
11

এখন 11 এখনও single digit নয়।

তাই আবার:

11
↓
1 + 1
↓
2

এখন 2 single digit।

তাই answer:

2
4️⃣ only one digit মানে কী?

একটি single-digit number হলো:

0 → 9

অর্থাৎ:

num < 10

হলে আমাদের কাজ শেষ।

Example
7

এখানে:

7 < 10

তাই সরাসরি:

7

return করা যায়।

🧠 Step 2 — আজকের মূল Pattern

এখানে আমাদের আগের Palindrome Number problem-এর digit manipulation pattern আবার কাজে লাগবে।

মনে রাখুন:

num % 10

→ শেষ digit বের করে।

আর:

num // 10

→ শেষ digit বাদ দেয়।

5️⃣ Digit Sum কীভাবে করব?

ধরি:

num = 38

আমরা একটি variable নেব:

digit_sum = 0

তারপর:

38 % 10 = 8

শেষ digit:

8

তাই:

digit_sum = 0 + 8
          = 8

তারপর:

38 // 10 = 3

এখন num:

3

আবার:

3 % 10 = 3

তাই:

digit_sum = 8 + 3
          = 11

তারপর:

3 // 10 = 0

Digit extraction শেষ।

আমরা পেলাম:

38 → 11
6️⃣ কিন্তু কাজ এখানেই শেষ নয়

কারণ:

11

এক digit নয়।

তাই আবার digit sum করতে হবে।

11
↓
1 + 1
↓
2

এখন:

2 < 10

তাই:

return 2
🔄 Step 3 — পুরো Algorithm

আমাদের logic হবে:

num
 ↓
num < 10 ?
 ↓ No
সব digit যোগ করো
 ↓
নতুন num = digit_sum
 ↓
আবার check করো
 ↓
num < 10 ?
 ↓ Yes
return num

Python-এর ভাষায়:

while num >= 10:
    digit sum করো
    num = digit_sum

return num

এখানে while খুব natural choice।

কারণ আমরা জানি না কতবার digit sum করতে হবে।

🧪 Step 4 — Full Dry Run

ধরি:

num = 38

Initial:

num = 38

যেহেতু:

38 >= 10

তাই loop চলবে।

প্রথম iteration
38 % 10 = 8
digit_sum = 8

তারপর:

38 // 10 = 3

পরের digit:

3 % 10 = 3
digit_sum = 8 + 3
          = 11

শেষে:

num = 11
দ্বিতীয় iteration
11 >= 10

তাই আবার digit sum।

11 % 10 = 1
digit_sum = 1

তারপর:

11 // 10 = 1

আবার:

1 % 10 = 1
digit_sum = 1 + 1
          = 2

এখন:

num = 2
এবার condition
2 >= 10

False।

তাই loop শেষ।

return 2

✅ Answer = 2

🧪 Step 5 — Example num = 0

Input:

num = 0

Check:

0 >= 10

False।

তাই loop চলবে না।

সরাসরি:

return 0

✅ Answer:

0
🧪 Step 6 — আরেকটা Example

ধরি:

num = 999

প্রথম digit sum:

9 + 9 + 9 = 27

তারপর:

27

আবার:

2 + 7 = 9

তাই:

999 → 27 → 9

Answer:

9
🧠 Step 7 — Problem Pattern

এই problem-এর basic pattern:

Digit Manipulation + Repeated Processing

আমাদের দরকার:

num % 10

→ last digit

num // 10

→ remove last digit

এবং:

while num >= 10:

→ যতক্ষণ single digit না হচ্ছে।

🔥 Step 8 — এখন একটা গুরুত্বপূর্ণ Interview Concept

এই problem-এর একটি mathematical shortcut আছে।

এটাকে বলা হয়:

Digital Root

যেমন:

38
→ 3 + 8
→ 11
→ 1 + 1
→ 2

তাই digital root:

2

Mathematically, positive number-এর ক্ষেত্রে:

digital root = 1 + (num - 1) % 9

আর num = 0 হলে:

0

তবে এখনই এই formula মুখস্থ করার দরকার নেই।

আপনার বর্তমান learning stage-এ প্রথমে:

digit extraction + while loop

ভালোভাবে আয়ত্ত করা বেশি গুরুত্বপূর্ণ।

কারণ আপনি শুধু এই problem-এর answer শিখছেন না; আপনি digit manipulation pattern শিখছেন।

💻 Step 9 — এখন আপনার Coding Task

আমি এখনো complete code দিচ্ছি না। আপনি নিজে লিখবেন।

এই structure ব্যবহার করুন:

class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:

            digit_sum = 0

            # এখানে digit বের করে যোগ করবেন

            # এখানে num থেকে শেষ digit remove করবেন

            # শেষে num = digit_sum করবেন

        return num

আপনার লক্ষ্য:

38
↓
11
↓
2

এবং:

0
↓
0

দুটোই কাজ করতে হবে।

🧠 আপনার জন্য Hint
Hint 1

শেষ digit বের করতে:

num % 10
Hint 2

শেষ digit বাদ দিতে:

num // 10
Hint 3

digit যোগ করতে:

digit_sum += digit
Hint 4

সব digit শেষ হওয়ার পরে:

num = digit_sum
🎤 Step 10 — Interview Thinking

Interviewer যদি জিজ্ঞেস করে:

"What is the approach?"

আপনার basic answer হবে:

I repeatedly calculate the sum of the digits until the number becomes a single digit.

আর একটু detail:

I use a while loop to check whether the number has more than one digit. Inside the loop, I extract each digit using the modulo operator, add the digits, and then replace the number with the digit sum.

📚 Step 11 — English Vocabulary
English	বাংলা
repeatedly	বারবার
digit	অঙ্ক
sum	যোগফল
single digit	এক অঙ্কের সংখ্যা
extract	বের করা
remove	বাদ দেওয়া
replace	পরিবর্তে বসানো
until	যতক্ষণ পর্যন্ত
remainder	ভাগশেষ
integer division	পূর্ণসংখ্যা ভাগ
Important phrases

add all the digits

→ সব digit যোগ করা

until the result has only one digit

→ যতক্ষণ না result-এ মাত্র একটি digit থাকে

extract the last digit

→ শেষ digit বের করা

remove the last digit

→ শেষ digit বাদ দেওয়া

📄 Step 12 — 1-Page Interview Note

এটা আপনার notebook-এর জন্য final revision format:

LeetCode 258 — Add Digits
🎯 Problem

Given an integer num, repeatedly add all its digits until only one digit remains.

Input
num = integer
Output
single-digit integer
Examples
38 → 3+8 → 11 → 1+1 → 2

0 → 0

999 → 27 → 9
🧠 Pattern

Digit Manipulation + Repeated Processing

🔑 Key Operations
num % 10

→ Last digit বের করে

num // 10

→ Last digit remove করে

Algorithm
1. While num >= 10:
2. Set digit_sum = 0
3. Extract each digit
4. Add each digit to digit_sum
5. Remove each digit from num
6. Set num = digit_sum
7. Repeat until num < 10
8. Return num
Core Logic
digit = num % 10
digit_sum += digit
num = num // 10
Dry Run
num = 38

38 → 8 + 3 → 11

11 → 1 + 1 → 2

2 < 10

Answer = 2
Complexity

যদি d = প্রতিটি digit-sum round-এর processing বিবেচনায় মোট digit processing ধরা হয়, তাহলে সহজ interview analysis-এ এটিকে O(log n) হিসেবে বলা যায়; আরও preciseভাবে, repeated digit sums-এর কারণে total work O(d + d/...), যা একই order-এর।

Time  → O(log n)
Space → O(1)
Interview Keywords
digit manipulation
modulo
integer division
digit sum
while loop
single digit
repeatedly
digital root
🎤 Interview Answer

I repeatedly calculate the sum of the digits until the number becomes a single digit. I use the modulo operator to extract the last digit and integer division to remove it. I store the digit sum and use it as the new number for the next iteration. The time complexity is O(log n) and the space complexity is O(1).

⭐ আজকের ৩টি Core Pattern
num % 10
    ↓
Last digit
num // 10
    ↓
Remove last digit
while num >= 10
    ↓
Repeat until single digit
🔥 Connection দেখুন

আপনি এখন পর্যন্ত:

Palindrome Number

% 10 → digit বের
// 10 → digit বাদ

এরপর Add Digits-এ একই pattern:

% 10 → digit বের
// 10 → digit বাদ
+     → digit যোগ
while → আবার repeat

অর্থাৎ আপনি শুধু আরেকটি LeetCode problem করছেন না—আপনি Digit Manipulation-এর একটি reusable pattern তৈরি করছেন।

"""