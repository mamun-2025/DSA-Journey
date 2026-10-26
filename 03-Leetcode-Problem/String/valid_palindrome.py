

# Leectcode Problem: 125
# String Cleaning + Reverse
class Solution:
   def isPalindrome(self, s: str) -> bool:
      cleaned = ""

      for cha in s.lower():
         if cha.isalnum():
            cleaned += cha 

      return cleaned == cleaned[::-1]

# Complexity
# Time Complexity: O(n) — string পরিষ্কার করা ও reverse তুলনা করার জন্য linear time লাগে।
# Extra Space Complexity: O(n) — cleaned string এবং reverse operation-এর জন্য অতিরিক্ত memory লাগতে পারে।




# Two Pointers
class Solution:
   def isPalindrome(self, s: str) -> bool:
      left = 0
      right = len(s) - 1

      while left < right:

         while left < right and not s[left].isalnum():
            left += 1

         while left < right and not s[right].isalnum():
            right -= 1

         if s[left].lower() != s[right].lower():
            return False

         left += 1
         right -= 1

      return True

# Complexity
# Time Complexity: \(O(n)\) — প্রতিটি pointer কেবল একদিকে এগোয়; কোনো character বারবার অতিক্রম করে না।
# Extra Space Complexity: \(O(1)\) — cleaned string তৈরি করি না; শুধু দুটি pointer ও কয়েকটি variable ব্যবহার করি।

"""
I use two pointers, one from the beginning and one from the end.
I skip non-alphanumeric characters using isalnum().
Then, I compare the remaining characters in lowercase.
If any pair does not match, I return false.
If all valid characters match, I return True.
The time complexity is 0(n) and the space complexity is 0(1).

"""



