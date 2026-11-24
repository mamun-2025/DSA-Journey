
"""
Square Root (বর্গমূল):
কোনো সংখ্যাকে নিজের সঙ্গে গুণ করলে যে সংখ্যা পাওয়া যায়, সেই সংখ্যাটির Square Root হলো মূল সংখ্যা।
4 X 4 = 16
√16 = 4

3 X 3 = 9
√9 = 3

Square Root যদি পূর্ণসংখ্যা না হয়, তাহলে তার নিচের পূর্ণসংখ্যাটি Return করতে হবে।
উদাহরণ:
√8=2.828427...

আমাদের Return করতে হবে:
2

আরেকটি উদাহরণ:
√15=3.872983...

আমাদের Return করতে হবে:
3

এখানে আমরা সাধারণ Rounding করছি না। আমরা Floor Value নিচ্ছি।

2. Floor কী?
Floor হলো কোনো সংখ্যার সমান বা তার চেয়ে ছোট সবচেয়ে কাছের পূর্ণসংখ্যা।
Number	Floor
2.5	2
3.9	3
4.0	4
8.7	8
10.99	10

তাই আমাদের Problem-এর মূল লক্ষ্য:
Find the largest integer r such that r^2 <= x.
এই একটি Mathematical Condition পুরো Problem বুঝতে সাহায্য করবে।

"""
# Leetcode Problem: 69. Sqrt(x)
# Approach 1 — Simple Approach: Linear Search
class Solution:
   def mySqrt(self, x: int)-> int:

      result = 0

      while (result + 1) * (result + 1) <= x:
         result += 1

      return result 


# Time: O(√x)
# Space: O(1)


"""
Square Root বের করতে Binary Search কেন ব্যবহার করা যাবে?
কারণ আমাদের সম্ভাব্য উত্তরগুলো Sorted Order-এ সাজানো যায়।

ধরো:
x = 16

সম্ভাব্য উত্তর:
0, 1, 2, 3, 4, 5, 6, 7, 8, ...

এখন প্রতিটি সংখ্যার Square পরীক্ষা করলে একটি নির্দিষ্ট Pattern পাওয়া যায়।
0 = 0
1 = 1
2 = 4
3 = 9
4 = 16
5 = 25
6 = 36
7 = 49
8 = 64
9 = 81
10 = 100

Valid: 0–4
Invalid: 5–7

আমাদের খুঁজতে হবে সবচেয়ে বড় Valid Number। সেটিই Integer Square Root।
এই ধরনের Search-কে Binary Search on Answer বলা হয়।
"""

# Approach 2 — Interview Approach (Binary Search)
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., 
# and since we round it down to the nearest integer, 2 is returned.

class Solution:
   def mySqrt(self, x: int)-> int:
      left = 0
      right = x 

      ans = 0

      while left <= right:

         mid = (left + right) // 2

         if mid * mid <= x:
            ans = mid # কারণ বর্তমান mid একটি Valid Answer। কিন্তু আরও বড় Answer থাকতে পারে।
            left = mid + 1 # Square x-এর সমান বা ছোট হলে → Answer সংরক্ষণ করে ডান দিকে Search।

         else:
            right = mid - 1  # Square x-এর চেয়ে বড় হলে → বাম দিকে Search।

      return ans 
   
"""
আমাদের Binary Search প্রতিবার Search Space অর্ধেক করে দেয়।

উদাহরণ:
16 → 8 → 4 → 2 → 1

তাই:
time: O(log x)

আমরা শুধু কয়েকটি Variable ব্যবহার করছি:
কোনো অতিরিক্ত Array বা Data Structure তৈরি করছি না।
space: O(1)

Interview:
I will use Binary Search to solve this problem efficiently.
First, I will define the seach range from zero to x.
Then, I will calculate the middle value and check whether its square is less than or equal to x.
If the square is less than or equal to x, I will store the middle value as a potential answer 
and search in the right half for a larger valid answer.
Otherwise, I will search in the left half.
Finally, I will return the largest valid integer.
The time complexity is O(log x), and the space complexity is O(1).


"""