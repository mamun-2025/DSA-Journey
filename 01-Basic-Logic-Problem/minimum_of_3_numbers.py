

# simple minimum
a = 10
b = 15
c = 20

minimum = a 

if b < minimum:
   minimum = b 

if c < minimum:
   minimum = c 

print(minimum)

"""
First, I assume the first number is the minumum.
Then I compare the second number with the current minumum and update if it the seocnd number is smaller.
Finally, I compare the third number with the current minumum.
The time complexity is 0(1) and space complexity is 0(1).

"""

# Future array of minimum
array = [5, 8, 2, 7, 9]

minimum = array[0]

for arr in array:
   if arr < minimum:
      minimum = arr 

print(minimum)



# Built-in minimum
a = 10
b = 5
c = 1

minimum = min(a, b, c)

print(minimum)