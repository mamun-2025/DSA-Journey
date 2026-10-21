

# Built-in Python Slicing
text = "python"

result = text[::-1]
print(result)
# Time complextiy = 0(n)
# Space complexity = 0(n)


# loop 
text = "python"

reversed = ""

for cha in text:
   reversed = cha + reversed

print(reversed)
# Time complexity = 0(n)
# Space complexity = 0(n)
"""
I can reverse a string by traversing it from the end to the beginning.
In Python, I can use slicing with a step -1.
This takes 0(n) because every character is processed
and 0(n) auxiliary space because a new reversed string is created.

"""


# two pointers
text = "python"

chars = list(text)

left = 0
right = len(chars) - 1 

while left < right:
   chars[left], chars[right] = chars[right], chars[left]

   left += 1
   right -= 1

reversed = "".join(chars)
print(reversed)
# Time complexity = 0(n)
# Space complexity = 0(n)
"""
Can you do it without slicing?
= Yes, I can use two pointer technique.
  I convert the string into a mutable list,
  keep one pointer at the beginning and another pointer at the end,
  swap the characters, move both pointers toward the center.

"""


# number reverse
n = int(input("Enter a number.. "))
reverse = 0

while n > 0:
   digit = n % 10 
   reverse = reverse * 10 + digit
   n //= 10

print(reverse)

"""
I repeatdly extract the last digit using %10.
Then I append that digit to the reversed number using 'reverse = reverse * 10 + digit.
Finally, I remove the last digit from the original number using integer division by 10.
I repeat this until the number becomes zero.
If the number has d digits, the time complexity is 0(d)
and the auxiliary space complexity is 0(1).

"""