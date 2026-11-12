

# Leetcode Problem: 128. Longest Consecutive Sequence
# তোমাকে একটি Unsorted Integer Array দেওয়া হবে।
# তোমাকে Array-এর মধ্যে থাকা সবচেয়ে দীর্ঘ Consecutive Number Sequence-এর Length বের করতে হবে।

"""
Consecutive Numbers কী?
= যেসব Number ধারাবাহিকভাবে একটির পর একটি আসে।
  1, 2, 3, 4, 5

যদি কোনো Number-এর আগের Number Set-এ না থাকে, তাহলে সেটিই একটি Sequence Start।

Set-এর সুবিধা:
- Duplicate Remove হয়ে যায়।
- Membership Lookup Average O(1)।
- num in num_set দিয়ে দ্রুত Number খুঁজতে পারি।

"""
nums = [100, 4, 200, 1, 3, 2]

class Solution:
   def longestConsecutive(self, nums: list[int]) -> int:
      num_set = set(nums)

      longest = 0

      for num in num_set:
         if num - 1 not in num_set:
            current_num = num 
            current_len = 1

            while current_num + 1 in num_set:
               current_num += 1
               current_len += 1

            longest = max(longest, current_len)

      return longest



"""
First, I convert the input array into a HashSet to remove duplicates and enable efficient lookups. 
Then, I iterate through the set. For each number, I check whether its previous consecutive number exists. 
If it does not exist, the current number is the start of a new sequence. 
I use a while loop to find the next consecutive numbers and calculate the sequence length. 
Finally, I update the longest sequence length and return the result. 
The average time complexity is O(n), and the space complexity is O(n).

কেন Nested While Loop থাকলেও O(n)?
এটি Interview-এর একটি গুরুত্বপূর্ণ প্রশ্ন।

কোডে একটি for Loop এবং তার ভিতরে একটি while Loop আছে।

দেখে মনে হতে পারে: O(n^2)
কিন্তু এখানে তা নয়।

কারণ আমরা while Loop শুধু Sequence Start থেকে চালাই।

উদাহরণ:
1 → 2 → 3 → 4 → 5

শুধু 1 দিয়ে Sequence শুরু হবে।
- 2 Sequence Start নয়।
- 3 Sequence Start নয়।
- 4 Sequence Start নয়।
- 5 Sequence Start নয়।

অর্থাৎ 1 থেকে 5 পর্যন্ত Number-গুলো এই Sequence Expansion-এ একবার করে পরীক্ষা হয়।
অন্য Sequence থাকলেও সেটি আলাদা এবং প্রতিটি Sequence-এর Number-গুলোও একবার করে Expansion-এ পরীক্ষা হবে।
সব Sequence-এর মধ্যে মোট Number-এর সংখ্যা সর্বোচ্চ n।

তাই:
- Set তৈরি করতে Average O(n)।
- Outer Loop O(n)।
- সব While Loop মিলিয়ে মোট O(n)।

সুতরাং:
O(n)+O(n)+O(n)=O(n)

Important Interview Point
O(n) Average Time
Nested While Loop থাকলেই সবসময় O(n²) হয় না। 
Loop-গুলোর মোট কাজ কতবার হচ্ছে, সেটি বিশ্লেষণ করতে হবে।


বিশেষভাবে মনে রাখবে
- HashSet → Duplicate Remove + Fast Lookup।
- Sequence Start → num - 1 Set-এ নেই।
- Sequence Expansion → num + 1 Set-এ আছে।
- current_length → বর্তমান Sequence-এর Length।
- longest → সবচেয়ে বড় Sequence-এর Length।

"""