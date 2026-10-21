

# Basic
text = "Programming"

vowels = "aeiou"
count = 0

for ch in text:
   if ch in vowels:
      count += 1

print(count)


# Uppercase and Lowercase handle
text = "HELLO"

vowels = "aeiou"
count = 0

for cha in text.lower():
   if cha in vowels:
      count += 1

print(count)

"""
I iterate through each character of the string and check whether the character is a vowel.
If it is, I increament a counter.
Since every character is visited once, so the time complexity is 0(n).
Where n is the length of the string.
The auxiliary space complexity is 0(1) 
because I only use a counter and a fixed size set of vowels.

"""

