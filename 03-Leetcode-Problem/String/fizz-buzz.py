

class Solution:
   def fizzBuzz(self, n:int) ->list[str]:
      answer = []

      for i in range(1, n + 1):

         if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")

         elif i % 3 == 0:
            answer.append("Fizz")

         elif i % 5 == 0:
            answer.append("Buzz")

         else:
            answer.append(str(i))

      return answer 


"""
We iterate from 1 to n. 
For each number, we check whether it is divisible by both 3 and 5.
If it is, we add "FizzBuzz". 
Otherwise, if it is divisible by 3, we add "Fizz".
If it is divisible by 5, we add "Buzz".
Otherwise, we add the number as a string.
Finally, we return the result list.
"""

"""
# 🟢 LeetCode #412 — Fizz Buzz

## 🎯 Learning Goal

এই Problem থেকে আমরা শিখব:

1. Problem বুঝতে
2. Input এবং Output চিনতে
3. `for loop`
4. `range()`
5. `%` Modulo Operator
6. `if / elif / else`
7. Multiple condition — `and`
8. `list`
9. `append()`
10. Integer → String conversion
11. Return value
12. Dry Run
13. Time Complexity
14. Space Complexity
15. Interview Explanation

---

# 1️⃣ Problem Statement

আমাদের একটি integer `n` দেওয়া হবে।

`1` থেকে `n` পর্যন্ত প্রতিটি number-এর জন্য:

* যদি number **3 এবং 5 উভয় দিয়েই divisible** হয় → `"FizzBuzz"`
* যদি শুধু **3 দিয়ে divisible** হয় → `"Fizz"`
* যদি শুধু **5 দিয়ে divisible** হয় → `"Buzz"`
* অন্যথায় number-টিকে **string** হিসেবে রাখতে হবে।

### Example

যদি:

```python
n = 5
```

তাহলে:

```text
1 → "1"
2 → "2"
3 → "Fizz"
4 → "4"
5 → "Buzz"
```

Output:

```python
["1", "2", "Fizz", "4", "Buzz"]
```

---

# 2️⃣ Step 1 — Input কী?

Input হলো:

```python
n
```

এটি একটি integer।

উদাহরণ:

```python
n = 5
```

অর্থাৎ আমাদের `1` থেকে `5` পর্যন্ত কাজ করতে হবে।

---

# 3️⃣ Step 2 — Output কী?

Output হলো একটি list of strings।

উদাহরণ:

```python
["1", "2", "Fizz", "4", "Buzz"]
```

খেয়াল করুন:

```python
1
```

না, বরং:

```python
"1"
```

কারণ output-এর সব element string হওয়া দরকার।

---

# 4️⃣ Step 3 — প্রথম Line

```python
class Solution:
```

LeetCode সাধারণত solution লেখার জন্য একটি class দেয়।

এখানে:

```python
Solution
```

হলো class-এর নাম।

এটি LeetCode-এর coding format-এর অংশ।

---

# 5️⃣ Step 4 — Function

```python
def fizzBuzz(self, n: int) -> list[str]:
```

এখানে আমরা একটি function তৈরি করছি:

```python
fizzBuzz()
```

### `self`

```python
self
```

class-এর object-কে represent করে।

LeetCode-এর class-based solution-এ এটি সাধারণত লিখতে হয়।

### `n: int`

```python
n: int
```

এর অর্থ:

> `n` একটি integer হবে।

এটি একটি type hint।

### `-> list[str]`

```python
-> list[str]
```

এর অর্থ:

> Function একটি string-এর list return করবে।

যেমন:

```python
["1", "2", "Fizz"]
```

---

# 6️⃣ Step 5 — Empty List তৈরি

```python
answer = []
```

আমরা একটি empty list তৈরি করলাম।

শুরুতে:

```python
answer = []
```

তারপর একে একে result যোগ করব।

উদাহরণ:

```python
answer = []

answer.append("1")
answer.append("2")
answer.append("Fizz")
```

তখন:

```python
answer
```

হবে:

```python
["1", "2", "Fizz"]
```

### কেন list?

কারণ আমাদের অনেকগুলো result একসাথে return করতে হবে।

---

# 7️⃣ Step 6 — For Loop

```python
for i in range(1, n + 1):
```

এটি খুব গুরুত্বপূর্ণ।

আমাদের `1` থেকে `n` পর্যন্ত প্রতিটি number check করতে হবে।

যদি:

```python
n = 5
```

তাহলে:

```python
range(1, 5 + 1)
```

অর্থাৎ:

```python
range(1, 6)
```

এটি generate করবে:

```text
1
2
3
4
5
```

### কেন `n + 1`?

Python-এর `range()`-এর শেষ value include হয় না।

```python
range(1, 5)
```

দেবে:

```text
1, 2, 3, 4
```

তাই `5` পেতে লিখতে হয়:

```python
range(1, 5 + 1)
```

---

# 8️⃣ Step 7 — প্রথম Condition

```python
if i % 3 == 0 and i % 5 == 0:
```

এখানে আমাদের check করতে হবে:

> `i` কি 3 এবং 5 উভয় দিয়ে divisible?

---

# 9️⃣ `%` Modulo Operator

```python
%
```

এটি remainder বের করে।

উদাহরণ:

```python
10 % 3
```

Result:

```text
1
```

কারণ:

```text
10 ÷ 3 = 3 remainder 1
```

আবার:

```python
12 % 3
```

Result:

```text
0
```

কারণ:

```text
12 ÷ 3 = 4 remainder 0
```

তাই কোনো number যদি:

```python
number % 3 == 0
```

হয়, তাহলে number টি 3 দিয়ে divisible।

---

# 🔟 `and` কী করছে?

আমাদের condition:

```python
i % 3 == 0 and i % 5 == 0
```

এখানে দুটি condition আছে:

```python
i % 3 == 0
```

এবং:

```python
i % 5 == 0
```

দুটিই True হতে হবে।

### Example: 15

```python
15 % 3 == 0
```

True

এবং:

```python
15 % 5 == 0
```

True

তাই:

```python
True and True
```

ফলাফল:

```python
True
```

তখন `"FizzBuzz"` হবে।

---

# 1️⃣1️⃣ কেন FizzBuzz Condition প্রথমে?

আমাদের code:

```python
if i % 3 == 0 and i % 5 == 0:
    answer.append("FizzBuzz")

elif i % 3 == 0:
    answer.append("Fizz")

elif i % 5 == 0:
    answer.append("Buzz")
```

এখানে `"FizzBuzz"` condition আগে রাখতে হবে।

কারণ:

```python
15
```

3 দিয়েও divisible:

```python
15 % 3 == 0
```

এবং 5 দিয়েও divisible:

```python
15 % 5 == 0
```

যদি আমরা আগে লিখি:

```python
if i % 3 == 0:
```

তাহলে `15`-এর জন্য `"Fizz"` হয়ে যাবে এবং `"FizzBuzz"` পর্যন্ত আর যাবে না।

তাই:

> **Most specific condition → আগে**

অর্থাৎ:

```text
3 AND 5
↓
3
↓
5
↓
other
```

---

# 1️⃣2️⃣ FizzBuzz Append

```python
answer.append("FizzBuzz")
```

যদি number 3 এবং 5 উভয় দিয়ে divisible হয়, তাহলে list-এ:

```python
"FizzBuzz"
```

যোগ হবে।

Example:

```python
i = 15
```

তাহলে:

```python
answer.append("FizzBuzz")
```

---

# 1️⃣3️⃣ `elif` — 3 দিয়ে Divisible

```python
elif i % 3 == 0:
    answer.append("Fizz")
```

যদি প্রথম condition False হয় এবং `i` 3 দিয়ে divisible হয়:

```python
"Fizz"
```

যোগ হবে।

Example:

```python
i = 9
```

কারণ:

```python
9 % 3 == 0
```

তাই:

```python
"Fizz"
```

---

# 1️⃣4️⃣ 5 দিয়ে Divisible

```python
elif i % 5 == 0:
    answer.append("Buzz")
```

যদি number 5 দিয়ে divisible হয়:

```python
"Buzz"
```

যোগ হবে।

Example:

```python
i = 10
```

কারণ:

```python
10 % 5 == 0
```

তাই:

```python
"Buzz"
```

---

# 1️⃣5️⃣ `else`

```python
else:
    answer.append(str(i))
```

যদি number:

* 3 দিয়ে divisible না হয়
* 5 দিয়েও divisible না হয়

তাহলে original number-টিকে string বানিয়ে list-এ যোগ করব।

Example:

```python
i = 7
```

7 neither divisible by 3 nor 5.

তাই:

```python
str(7)
```

হবে:

```python
"7"
```

তারপর:

```python
answer.append("7")
```

---

# 1️⃣6️⃣ কেন `str(i)`?

এটি খুব গুরুত্বপূর্ণ।

আমাদের output:

```python
list[str]
```

অর্থাৎ list-এর সব element string।

যদি আমরা লিখতাম:

```python
answer.append(i)
```

তাহলে output হতে পারত:

```python
[1, 2, "Fizz", 4, "Buzz"]
```

এখানে `1`, `2`, `4` integer।

কিন্তু আমাদের দরকার:

```python
["1", "2", "Fizz", "4", "Buzz"]
```

তাই:

```python
str(i)
```

ব্যবহার করেছি।

---

# 1️⃣7️⃣ `return answer`

শেষে:

```python
return answer
```

এর অর্থ:

> আমরা যে result list তৈরি করেছি, সেটি function-এর বাইরে পাঠিয়ে দাও।

Example:

```python
answer = ["1", "2", "Fizz", "4", "Buzz"]
```

তাহলে:

```python
return answer
```

এই list-টি output হিসেবে return করবে।

---

# 🧠 সম্পূর্ণ Code

```python
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:

        answer = []

        for i in range(1, n + 1):

            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")

            elif i % 3 == 0:
                answer.append("Fizz")

            elif i % 5 == 0:
                answer.append("Buzz")

            else:
                answer.append(str(i))

        return answer
```

---

# 🔍 Dry Run

ধরি:

```python
n = 15
```

তাহলে loop চলবে:

```text
1 → 15
```

| i  | `i % 3 == 0` | `i % 5 == 0` | Output       |
| -- | ------------ | ------------ | ------------ |
| 1  | False        | False        | `"1"`        |
| 2  | False        | False        | `"2"`        |
| 3  | True         | False        | `"Fizz"`     |
| 4  | False        | False        | `"4"`        |
| 5  | False        | True         | `"Buzz"`     |
| 6  | True         | False        | `"Fizz"`     |
| 7  | False        | False        | `"7"`        |
| 8  | False        | False        | `"8"`        |
| 9  | True         | False        | `"Fizz"`     |
| 10 | False        | True         | `"Buzz"`     |
| 11 | False        | False        | `"11"`       |
| 12 | True         | False        | `"Fizz"`     |
| 13 | False        | False        | `"13"`       |
| 14 | False        | False        | `"14"`       |
| 15 | True         | True         | `"FizzBuzz"` |

Final result:

```python
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```

---

# 🧩 Problem-এর মূল Logic

পুরো problem-টাকে আসলে এভাবে ভাবতে হবে:

```text
প্রতিটি number নাও
       ↓
3 এবং 5 উভয় দিয়ে divisible?
       ↓ Yes
   FizzBuzz
       ↓ No
3 দিয়ে divisible?
       ↓ Yes
     Fizz
       ↓ No
5 দিয়ে divisible?
       ↓ Yes
     Buzz
       ↓ No
   Number
```

এটাই পুরো algorithm।

---

# ⏱️ Time Complexity

আমরা:

```python
for i in range(1, n + 1):
```

দিয়ে `n` বার loop চালাচ্ছি।

প্রতিটি iteration-এর ভিতরে:

* modulo → O(1)
* comparison → O(1)
* append → O(1) average

তাই:

```text
O(n)
```

### Final:

```text
Time Complexity = O(n)
```

---

# 💾 Space Complexity

আমরা:

```python
answer = []
```

এবং `n` টি result সংরক্ষণ করছি।

তাই output-এর জন্য:

```text
O(n)
```

space লাগবে।

### Final:

```text
Space Complexity = O(n)
```

> এখানে output list-এর space-টিও আমরা গণনা করছি।

---

# 🎤 Interview Explanation

ইন্টারভিউতে এভাবে বলতে পারেন:

> "The input is an integer n, and I need to generate a list of strings from 1 to n. For each number, I first check whether it is divisible by both 3 and 5. If so, I add FizzBuzz. Otherwise, if it is divisible by 3, I add Fizz. If it is divisible by 5, I add Buzz. Otherwise, I convert the number to a string and add it to the result list. The time complexity is O(n), and the output space is O(n)."

### সহজ English Version

> "I loop from 1 to n. For each number, I check divisibility by 3 and 5 using the modulo operator. Then I append FizzBuzz, Fizz, Buzz, or the number as a string. The time complexity is O(n) and the space complexity is O(n)."

---

# 🧠 Pattern Recognition

এই problem দেখে আপনার মাথায় এখন এই pattern আসা উচিত:

```text
Loop + Condition + Modulo + List
```

অর্থাৎ:

```text
Problem
   ↓
Need to process 1 → n
   ↓
FOR LOOP
   ↓
Need divisibility
   ↓
MODULO %
   ↓
Different outputs
   ↓
IF / ELIF / ELSE
   ↓
Need multiple results
   ↓
LIST + APPEND
```

---

# ⭐ এই Problem থেকে কী কী শিখলাম?

### Python

```python
for
range()
if
elif
else
and
%
list
append()
str()
return
```

### DSA / Problem Solving

```text
Input
Output
Condition
Iteration
Modulo
Dry Run
Time Complexity
Space Complexity
```

### Complexity

```text
Loop → O(n)
Constant operation → O(1)
Total → O(n)
Output list → O(n)
```

---

# 📝 7-Step Rule — Fizz Buzz

যেকোনো LeetCode problem-এ এখন থেকে এই 7টি প্রশ্ন করবেন:

### 1. Input কী?

```text
n
```

### 2. Output কী?

```text
list[str]
```

### 3. Logic কী?

```text
1 → n loop
3 & 5 → FizzBuzz
3 → Fizz
5 → Buzz
otherwise → number
```

### 4. Dry Run কী?

```text
n = 5

1 → "1"
2 → "2"
3 → "Fizz"
4 → "4"
5 → "Buzz"
```

### 5. Time Complexity?

```text
O(n)
```

### 6. Space Complexity?

```text
O(n)
```

### 7. Interview Explanation?

```text
I loop from 1 to n and check whether each number
is divisible by 3, 5, or both using the modulo operator.
Then I append the appropriate string to the result list.
```

---

# 🔥 Important Interview Point

Fizz Buzz দেখতে খুব সহজ problem।

কিন্তু এখানে interviewer আসলে দেখছে আপনি:

* condition order বুঝতে পারেন কি না
* `%` বুঝেন কি না
* loop বুঝেন কি না
* output type বুঝেন কি না
* edge case ধরতে পারেন কি না
* complexity বলতে পারেন কি না

তাই problem-টি ছোট হলেও **এটি আপনার foundational problem-solving-এর জন্য গুরুত্বপূর্ণ।**

---

# 🏆 আপনার জন্য Practice

এখন code না দেখে নিজে লিখুন:

```text
n = 15
```

নিজের খাতায়/Notepad-এ লিখুন:

1. Input
2. Output
3. Logic
4. Dry Run
5. Time Complexity
6. Space Complexity
7. Interview Explanation

তারপর **code না দেখে আবার Fizz Buzz লিখুন**।

যদি code দেখে লিখতে পারেন, সেটা মুখস্থ।

যদি code না দেখে লিখতে পারেন এবং প্রতিটি line কেন লিখেছেন explain করতে পারেন, সেটা **understanding**।


"""
      