

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
# Minimum in a list
array = [5, 8, 2, 7, 9]

if not array:
   print("array is empty")

else:
   minimum = array[0]

   for arr in array:
      if arr < minimum:
         minimum = arr 

   print(minimum)

"""
I initialize the minimum with the first element. 
Then I traverse the array and compare each element with the current minimum. 
If I find a smaller element, I update the minimum. 
Since I visit every element once, the time complexity is O(n), 
and the auxiliary space complexity is O(1).”

"""



# Built-in minimum
a = 10
b = 5
c = 1

minimum = min(a, b, c)

print(minimum)


arr = [1, 5, 9, 2, 4]
result = min(arr)
print(result)




