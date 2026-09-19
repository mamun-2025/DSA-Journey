

n = int(input("Enter a integer number:"))

if n % 2 == 0:
   print(f"{n}- is a Even number.")
else: 
   print(f"{n}- is a Odd number.")

"""
I use the modulo operator.
If the remainder after dividing the number by 2 is zero, the number is even; otherwise, it is odd.
The time complexity is 0(1) and the space complexity is 0(1).

"""