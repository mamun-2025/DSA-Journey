

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