
# Loop Approach
n = int(input("Enter a number: "))

total = 0
for i in range(1, n + 1):
   total += i

print(f"Sum of numbers: {total}")

"""
I initialize a variable called total to zero.
Then I iterate from 1 to n and add each number to total.
The time complexity is 0(n) because I visit n numbers,
and the space complexity is 0(1) because I only use a few variables.

"""

## Formula Optimization
# 1 + 2 + 3 + .... + n 
# n(n+1)/2
n = int(input("Enter a number: "))

total = n * (n + 1) // 2 

print("Sum of numbers:",total)

"""
The straightforward approach is to loop from 1 to n, which takes 0(n) time.
However, we can use the formula n * (n + 1) // 2, which calculates the result in constant time.
Therefore, the optimized solution is 0(1) time and 0(1) space.

"""