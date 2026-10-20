

# Basic Prime 
n = 7

is_prime = True

if n < 2:
   is_prime = False

for i in range(2, n):
   if n % i == 0:
      is_prime = False
      break

print(is_prime)


# Optimized Prime
n = 29

is_prime = True

if n < 2:
   is_prime = False

i = 2 

while i * i <= n:
   if n % i == 0:
      is_prime = False
      break

   i += 1 

print(is_prime)


"""
I first handle numbers less than 2 because they are not prime. 
Then I check whether the number is divisible by any integer starting from 2.
To optimize the solution, I only check up to the square root of the number,
because if a number has a factor greater than its square root, 
it must have a corresponding factor smaller than the squre root.
Therefore, the optimized time complexity is 0(√n) 
and the space complexity is 0(1).

"""