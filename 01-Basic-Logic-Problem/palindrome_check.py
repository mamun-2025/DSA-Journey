

# Pythonic approach
text = "madam"

if text == text[::-1]:
   print("True")
else:
   print("False")



# Two pointer approach
text = "Madam".lower()

left = 0
right = len(text) - 1

is_palindrome = True

while left < right:
   if text[left] != text[right]:
      is_palindrome = False
      break

   left += 1
   right -= 1

print(is_palindrome)
"""
I would use the two pointer technique.
I intialize one pointer at the beginning and another at the end of the string.
Then I compare the characters at both pointers.
If they are different, the string is not a palindrome.
Otherwise, I move both pointers toward the center.
The worst-case time complexity is 0(n) and space complexity is 0(1).


I use two pointers, one from the left and one from the right.
I compare both characters and move them toward the center.
If any pair is different, I return false.
Otherwise it is a palindrome.
So time is 0(n) and space is 0(1).

"""

