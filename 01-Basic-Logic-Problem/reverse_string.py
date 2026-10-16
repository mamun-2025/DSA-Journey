

n = int(input("Enter a number.. "))
reverse = 0

while n > 0:
   digit = n % 10 
   reverse = reverse * 10 + digit
   n //= 10

print(reverse)


"""
I repeatdly extract the last digit using %10.
Then I append that digit to the reversed number using 'reverse = reverse * 10 + digit.
Finally, I remove the last digit from the original number using integer division by 10.
I repeat this until the number becomes zero.
If the number has d digits, the time complexity is 0(d)
and the auxiliary space complexity is 0(1).

"""