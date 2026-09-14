

class Solution:
   def isPalindrome(self, x: int) -> bool:
      if x < 0:
         return False

      original = x 
      reverse_num = 0

      while x > 0:
         last_digit = x % 10
         reverse_num = reverse_num * 10 + last_digit 
         x //= 10

      return original == reverse_num 


"""
I first check if the number is negative.
If it is negative, I return false.
Then I saved the original number and reverse the digits using modulo and integer division.
Finally, I compare the original number with the reversed number.
If they are equal, I return true, otherwise false.
The number is a palindrome if it reads the same backward as forward.
So the time complexity is 0(log x), and the space complexity is 0(1).

"""

"""
🟢 LeetCode 9 — Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
1️⃣ Problem Understanding

Problem বলছে:

Given an integer x, return true if x is a palindrome, and false otherwise.

সহজ বাংলায়:

আমাদের একটি integer x দেওয়া হবে।

আমাদের দেখতে হবে সংখ্যাটি সামনে থেকে এবং পিছন থেকে পড়লে একই কিনা।

একই হলে:

true

না হলে:

false

Python-এ:

True
False
2️⃣ Palindrome কী?

Palindrome হলো এমন কিছু যা সামনে থেকে এবং পিছন থেকে পড়লে একই থাকে।

Example
121

সামনে:

121

পিছনে:

121

তাই:

121 → Palindrome

আর:

123

সামনে:

123

পিছনে:

321

একই নয়।

তাই:

123 → Not Palindrome
3️⃣ Input এবং Output
Input

একটি integer:

x
Output

Boolean:

True

অথবা:

False
4️⃣ Example বুঝি
Example 1
Input:
x = 121

Reverse:

121

একই।

Output:
True
Example 2
Input:
x = -121

সামনে:

-121

পিছনে:

121-

একই নয়।

Output:
False
Example 3
Input:
x = 10

Reverse:

01

কিন্তু integer হিসেবে reverse করলে:

1

10 != 1

তাই:

Output:
False
5️⃣ প্রথম Important Pattern — Digit Manipulation

এখানে আমাদের একটি নতুন গুরুত্বপূর্ণ pattern শিখতে হবে:

Digit Manipulation

একটি integer থেকে আমরা কীভাবে শেষ digit বের করব?

Python-এর % 10 ব্যবহার করে।

x % 10
Example
121 % 10 = 1

শেষ digit:

1

আর:

1234 % 10 = 4

শেষ digit:

4
মনে রাখবেন
n % 10
   ↓
last digit

এটা Digit Manipulation-এর খুব গুরুত্বপূর্ণ pattern।

6️⃣ দ্বিতীয় Important Pattern — Last Digit Remove

শেষ digit বের করার পরে সেটাকে number থেকে বাদ দিতে হবে।

এর জন্য:

x // 10

ব্যবহার করব।

Example:

121 // 10 = 12

অর্থাৎ:

121
 ↓
12

আর:

12 // 10 = 1

অর্থাৎ:

12
 ↓
1
মনে রাখবেন
n % 10
   ↓
last digit বের করে

n // 10
   ↓
last digit remove করে

🔥 এই দুইটা pattern আপনার future problem solving-এর জন্য খুব গুরুত্বপূর্ণ।

7️⃣ এখন Reverse Number কীভাবে তৈরি করব?

ধরি:

x = 121

আমরা একটি variable নেব:

reversed_num = 0

তারপর একে একে digit বের করব।

প্রথমে:

121 % 10 = 1

তাই last digit:

1

Reverse number:

0 × 10 + 1
= 1

অর্থাৎ:

reversed_num = 1

এখন original number:

121 // 10 = 12

আবার last digit:

12 % 10 = 2

Reverse:

1 × 10 + 2
= 12

আবার:

12 // 10 = 1

Last digit:

1 % 10 = 1

Reverse:

12 × 10 + 1
= 121

শেষে:

x = 0

তখন reverse:

121
8️⃣ Reverse তৈরির Formula

এটা খুব ভালোভাবে মনে রাখবেন:

reversed_num = reversed_num * 10 + digit

যেখানে:

digit = x % 10

তারপর:

x = x // 10

অর্থাৎ পুরো pattern:

digit = x % 10
        ↓
reverse = reverse * 10 + digit
        ↓
x = x // 10

এটাই আজকের সবচেয়ে গুরুত্বপূর্ণ algorithmic pattern।

9️⃣ Full Dry Run — 121

এখন table দিয়ে দেখি।

Initial:

x = 121
reversed_num = 0
Round 1
digit = 121 % 10
      = 1
reversed_num
= 0 × 10 + 1
= 1

তারপর:

x = 121 // 10
  = 12

State:

x = 12
reverse = 1
Round 2
digit = 12 % 10
      = 2
reverse
= 1 × 10 + 2
= 12

তারপর:

x = 12 // 10
  = 1

State:

x = 1
reverse = 12
Round 3
digit = 1 % 10
      = 1
reverse
= 12 × 10 + 1
= 121

তারপর:

x = 1 // 10
  = 0

Loop শেষ।

এখন:

original = 121
reverse  = 121

দুটো equal।

তাই:

True
🔟 Negative Number কেন False?

ধরি:

x = -121

Palindrome হিসেবে:

-121

reverse:

121-

একই নয়।

তাই negative number-এর ক্ষেত্রে সরাসরি:

if x < 0:
    return False

করতে পারি।

এটা algorithm-কে সহজ করে।

1️⃣1️⃣ এখন মূল Logic

আমাদের algorithm:

Input x
   ↓
x < 0 ?
   ↓
Yes → False
   ↓ No
Save original number
   ↓
Reverse digits
   ↓
Compare original and reversed
   ↓
Same → True
Different → False
1️⃣2️⃣ কেন Original Number Save করতে হবে?

এখানে একটি গুরুত্বপূর্ণ বিষয় আছে।

আমরা যখন লিখব:

x = x // 10

তখন x পরিবর্তিত হবে।

শেষে:

x = 0

হয়ে যাবে।

তাই শুরুতেই:

original = x

রাখতে হবে।

তারপর x-কে modify করব।

শেষে:

original == reversed_num

check করব।

1️⃣3️⃣ এখন Code Structure

এখনও পুরো solution একবারে মুখস্থ করবেন না।

Logic অনুযায়ী structure:

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Step 1: negative number check

        # Step 2: save original number

        # Step 3: create reversed number

        # Step 4: extract digits and reverse

        # Step 5: compare original and reversed
Core pattern:
digit = x % 10

reversed_num = reversed_num * 10 + digit

x = x // 10

এই তিনটি line-ই আজকের core digit-reversal pattern।

1️⃣4️⃣ আপনি নিজে Code করার আগে — Mental Test

এখন নিজে চিন্তা করুন:

Case 1
x = 121

Expected:

True
Case 2
x = -121

Expected:

False
Case 3
x = 10

Expected:

False
Case 4
x = 0

Expected:

True

কারণ:

0 → 0

একই।

🧠 1️⃣5️⃣ Problem Pattern

এই problem-এর pattern:

Digit Manipulation + Number Reversal

আপনি যখন future-এ দেখবেন:

last digit
reverse number
sum of digits
count digits
palindrome number
repeatedly remove digits

তখন আপনার মাথায় আসবে:

% 10
//

অর্থাৎ:

% 10 → last digit
// 10 → remove last digit
⏱️ 1️⃣6️⃣ Time Complexity

ধরি সংখ্যাটিতে dটি digit আছে।

আমরা প্রতিটি digit একবার process করি।

তাই:

Time Complexity = O(d)

যেহেতু integer-এর digit count d সাধারণত log₁₀(x)-এর সমানুপাতিক:

O(log x)

Interview-এ বলতে পারেন:

The time complexity is O(log x), where x is the input number.

💾 1️⃣7️⃣ Space Complexity

আমরা শুধু কয়েকটি variable ব্যবহার করছি:

original
reversed_num
digit

কোনো list/string তৈরি করছি না।

তাই:

Space Complexity = O(1)

🔥 এটা এই problem-এর follow-up-এর একটি বড় সুবিধা।

🎤 1️⃣8️⃣ Interview Question — Why not use String?

Interviewer জিজ্ঞেস করতে পারে:

Can you solve this without converting the integer to a string?

আপনি বলবেন:

Yes. I can reverse the digits mathematically using the modulo and integer division operators. I use % 10 to extract the last digit and // 10 to remove the last digit. Then I compare the reversed number with the original number.

এটা খুব ভালো interview answer।

🇬🇧 1️⃣9️⃣ English Vocabulary
Word	Meaning
integer	পূর্ণসংখ্যা
palindrome	সামনে-পেছনে একই
reverse	উল্টানো
digit	অঙ্ক
divisible	নিঃশেষে বিভাজ্য
extract	বের করা
remainder	ভাগশেষ
compare	তুলনা করা
convert	রূপান্তর করা
original	মূল
otherwise	অন্যথায়
বিশেষ করে মনে রাখবেন:
extract the last digit

= শেষ digit বের করা

reverse the number

= সংখ্যাটি উল্টানো

compare the original number with the reversed number

= মূল সংখ্যা ও উল্টানো সংখ্যার তুলনা করা

🎤 2️⃣0️⃣ Interview English — Short Version

এটা interview-এ বলার জন্য ভালো:

I first check if the number is negative. If it is negative, I return false. Then I save the original number and reverse the digits using modulo and integer division. Finally, I compare the original number with the reversed number. If they are equal, the number is a palindrome. The time complexity is O(log x), and the space complexity is O(1).

📄 2️⃣1️⃣ আপনার 1-Page Interview Note

এটা আপনার খাতায়/নোটে এক পৃষ্ঠায় রাখার মতো final revision note:

LeetCode 9 — Palindrome Number
🎯 Problem

Given an integer x, return True if it reads the same forward and backward; otherwise return False.

Input
x = integer
Output
True / False
Examples
121  → True
-121 → False
10   → False
0    → True
🧠 Pattern

Digit Manipulation + Reverse Number

🔑 Key Operators
x % 10

→ last digit বের করে

x // 10

→ last digit remove করে

🔑 Reverse Formula
digit = x % 10

reverse = reverse * 10 + digit

x = x // 10
Algorithm
1. If x < 0 → False
2. Save original = x
3. reverse = 0
4. While x > 0:
      digit = x % 10
      reverse = reverse * 10 + digit
      x = x // 10
5. Compare original == reverse
6. Return result
Dry Run
x = 121

121 % 10 = 1
reverse = 0*10 + 1 = 1
x = 121//10 = 12

12 % 10 = 2
reverse = 1*10 + 2 = 12
x = 12//10 = 1

1 % 10 = 1
reverse = 12*10 + 1 = 121
x = 1//10 = 0

121 == 121
→ True
Complexity
Time  → O(log x)
Space → O(1)
Interview Keywords
modulo
integer division
last digit
reverse digits
original number
compare
digit manipulation
Interview Answer

I check for negative numbers first. Then I save the original number and reverse its digits using % 10 and // 10. Finally, I compare the original number with the reversed number. If they are equal, I return true. The time complexity is O(log x) and the space complexity is O(1).

⭐ আজকের সবচেয়ে গুরুত্বপূর্ণ ৩টি জিনিস
% 10
   ↓
Last digit
// 10
   ↓
Remove last digit
reverse = reverse * 10 + digit
   ↓
Build reversed number

এই তিনটা pattern ভালোভাবে আয়ত্ত করুন। এগুলো শুধু Palindrome Number-এর জন্য নয়—পরের অনেক digit manipulation problem-এ সরাসরি কাজে লাগবে।

"""