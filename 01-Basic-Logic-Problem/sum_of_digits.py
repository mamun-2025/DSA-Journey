

n = int(input("Enter a digits: "))

total = 0
while n > 0 :
   digit = n % 10
   total += digit 
   n //= 10

print(f"Sum of digits: {total}")


"""
1234 = 4 digits
123456 = 6 digits
time complexity = 0(d)
space complexity = 0(1)

I repeatedly extract the last digit using the modulo operator % 10,
add it to running total, and then remove the last digit using integer division // 10.
I repeat this until the number becomes zero.
If the number has d digts, the time complexity is 0(d),
because I process each digit once.
The auxiliary space complexity is 0(1).

"""