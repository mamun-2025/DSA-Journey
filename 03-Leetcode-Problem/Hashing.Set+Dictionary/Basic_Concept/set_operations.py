


# 1. Set Operations কী?
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}





# মূলত তিনটি গুরুত্বপূর্ণ Operation:
# - Intersection — Common elements
# - Union — All unique elements
# - Difference — One set-এর exclusive elements


# 2. Intersection — Common Elements
# Intersection অর্থ হলো দুটি Set-এর মধ্যে যে elements common বা একই রয়েছে।

# Method 1: & Operator
result = A & B
print(result)

# Method 2: .intersection()
result = A.intersection(B)
print(result)
# দুটি পদ্ধতির ফলাফল একই।


# 3. Union — All Unique Elements
# Union অর্থ হলো দুটি Set-এর সব unique elements একসঙ্গে করা।

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A | B 
print(result)
# এখানে 3 এবং 4 দুটি Set-এই আছে। কিন্তু Union-এ duplicate রাখা হয় না।
# Union মানে সব unique elements, শুধু common elements নয়।

result = A.union(B)
print(result)



# 4. Difference — Different Elements
# Difference অর্থ হলো প্রথম Set-এ আছে, কিন্তু দ্বিতীয় Set-এ নেই।
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A - B)
print(B - A)

# এখানে একটি গুরুত্বপূর্ণ বিষয়:
# - A - B → A-তে আছে, B-তে নেই।
# - B - A → B-তে আছে, A-তে নেই।
# Difference-এর ক্ষেত্রে order বা direction গুরুত্বপূর্ণ।

print(A.difference(B))
print(B.difference(A))


# 5. তিনটি Operation একসঙ্গে তুলনা
# Operation	         Symbol	      কাজ
# Intersection	        &	         Common elements
# Union	              |	         All unique elements
# Difference	        -	         First set-এর exclusive elements


A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}

print(A & B)
print(A | B)
print(A - B)
print(B - A)


"""
6. LeetCode 349 — Intersection of Two Arrays
Easy
 Hash Set

Intersection of Two ArraysProblem Statement:

Given two integer arrays nums1 and nums2, return an array of their intersection.

Each element in the result must be unique, and you may return the result in any order.

বাংলায় Problem বুঝি
তোমাকে দুটি Integer Array দেওয়া হবে।

তোমাকে এমন একটি নতুন Array return করতে হবে যেখানে:
1. দুটি Array-তেই থাকা elements থাকবে।
2. কোনো duplicate থাকবে না।
3. যেকোনো order-এ return করতে পারবে।


Example 1:
nums1 = [1, 2, 2, 1]nums2 = [2, 2]

Output:
[2]

কারণ দুটি Array-তেই 2 আছে। কিন্তু result-এ 2 একবারই থাকবে।

Example 2:
nums1 = [4, 9, 5]nums2 = [9, 4, 9, 8, 4]

Output:
[9, 4]

অথবা:
[4, 9]

দুটিই সঠিক।


7. Problem Solving Logic
আমাদের কী দরকার?
- দুটি Array-এর common elements।
- Duplicate বাদ দিতে হবে।
- দ্রুত membership checking করতে হবে।
এখানে Set ব্যবহার করাই উপযুক্ত।

Optimized Code:
def intersection(nums1, nums2):    set1 = set(nums1)    set2 = set(nums2)    result = set1 & set2    return list(result)

LeetCode-এ এভাবেই submit করতে পারবে।


8. Dry Run
Input:
nums1 = [1, 2, 2, 1]nums2 = [2, 2]

Step 1 — Convert to Set
set1 = {1, 2}set2 = {2}

Duplicate automatically বাদ হয়ে গেছে।

Step 2 — Intersection
result = set1 & set2

দুটি Set-এর common elements:
result = {2}

Step 3 — Convert to List
return list(result)

Final Output:
[2]




9. Brute Force vs Optimized
Brute Force:
def intersection(nums1, nums2):    result = []    for num in nums1:        if num in nums2 and num not in result:            result.append(num)    return result

Time Complexity: O(n imes m) সাধারণ ক্ষেত্রে, কারণ প্রতিটি membership check list-এ linear search করে।

Optimized — Set:
def intersection(nums1, nums2):    
   set1 = set(nums1)    
   set2 = set(nums2)    
   return list(set1 & set2)



ধরি, n = len(nums1) এবং m = len(nums2)।
Complexity	Brute Force	Optimized
Time	O(n × m)	O(n + m) average
Space	O(k) result	O(n + m)

এখানে k হলো unique common elements-এর সংখ্যা। Optimized version-এ দুটি Set তৈরি করার জন্য অতিরিক্ত memory লাগে।




10. Interview Questions
Q1. What is Set Intersection?

Answer: Set Intersection returns the common elements between two sets.

Q2. What is Set Union?

Answer: Set Union combines all unique elements from two sets.

Q3. What is Set Difference?

Answer: Set Difference returns elements that exist in the first set but not in the second set.

Q4. Why do we use Set in LeetCode 349?

Answer: We use Set to remove duplicates and perform efficient membership checking.

Q5. What is the average time complexity of Set membership checking in Python?

Answer: O(1) average time complexity.



11. Interview Speaking Practice
এই উত্তরটি English-এ বলার অনুশীলন করবে:
First, I convert both arrays into sets to remove duplicates. 
Then, I use the intersection operation to find the common elements. 
Finally, I convert the result back into a list. 
The average time complexity is O(n + m), 
and the space complexity is O(n + m).

"""