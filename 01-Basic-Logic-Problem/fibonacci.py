

# Iterative fibonacci
n = 7

a = 0 # a = current fibonacci number 
b = 1 # b = next fibonacci number 

for _ in range(n):
   print(a)

   a, b = b, a + b 

"""
new a = old b  
new b = old a + old b 

I use two variables to keep track of the current and next fibonacci numbers.
Initially, they are 0 and 1.
In every iteration, I print the current number and update both variables using the sum of the previous two numbers.
Since I iterate n times, the time complexity is 0(n) and space complexity is 0(1).


Iterative Fibonacci
Time  → O(n)
Space → O(1)

Naive Recursive Fibonacci
Time  → O(2^n)
Space → O(n)

"""


# Naive recursive fibonacci
def fib(n):
   if n <= 1:
      return n 

   return fib(n - 1) + fib(n - 2)


print(fib(4))