

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
# Maximum in a list
numbers = [2, 5, 7, 9, 1]

maximum = numbers[0]

for number in numbers:
   if number > maximum:
      maximum = number

print(maximum)

"""
I initialize the maximum with the first element of the array. 
Then I traverse the array and compare each element with the current maximum. 
If the current element is greater, I update the maximum. 
Since every element needs to be checked, the time complexity is O(n), 
and the auxiliary space complexity is O(1).”

"""


# Built in maximum numbers 
a = 10
b = 25
c = 15

maximum = max(a, b, c)

print(maximum)


arr = [1, 5, 9, 2, 4]
result = max(arr)
print(result)

