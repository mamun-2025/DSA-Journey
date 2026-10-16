

n = int(input("Enter a number: "))

for i in range(1, n+1):
   print(n, "X", i, "=", n*i)


"""
I will use a for loop from 1 to n.
For each iteration, I multiply the given number by current loop variable and print the result.
Since the loop runs n times, so time complexity is 0(n) and space complexity is 0(1).

"""

##
n = int(input("Enter a number: "))

for i in range(1, 11):
   print(f"{n} x {i} = {i * n}")


