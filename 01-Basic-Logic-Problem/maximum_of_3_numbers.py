

# Simple maximum number 
a = 25
b = 30
c = 20

maximum = a 

if b > maximum:
   maximum = b 

if c > maximum:
   maximum = c 

print(maximum)


"""
First, I assume the first number is the maximum.
Then I compare the second number with the current maximum and update it if necessary.
Finally, I compare the third number with the current maximum.
The time complexity is 0(1) and space complexity is 0(1).

"""


# Future array of maximum numbers
numbers = [2, 5, 7, 9, 1]

maximum = numbers[0]

for number in numbers:
   if number > maximum:
      maximum = number

print(maximum)



# Built in maximum numbers 
a = 10
b = 25
c = 15

maximum = max(a, b, c)

print(maximum)