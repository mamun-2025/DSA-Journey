

# Iterative solution
n = 0

result = 1

for i in range(1, n + 1):
   result *= i 

print(result)

##
n = 5

result = 1

for i in range(1, n + 1):
   result *= i 

print(result)




# Addition → সাধারণত 0 দিয়ে শুরু
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
   total += i 

print(total)


# Multiplication → সাধারণত 1 দিয়ে শুরু
n = int(input("Enter a number: "))
result = 1
for i in range(1, n+1):
   result *= i 

print(result)

"""
I initialize the result to 1 because I need to perform multiplication.
Then I iterate from 1 to n and multiply each number with the current result.
Since the loop runs n times, so the time complexity is 0(n) and 
the auxiliary space complexity is 0(1).

"""



## Factorial recursive version 
def factorial(n):
   if n == 0 or n == 1:
      return 1 

   return n * factorial(n-1)

print(factorial(4))

   

