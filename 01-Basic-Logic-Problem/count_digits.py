

n = int(input("Enter a digits: "))

count = 0
while n > 0:
   count += 1
   n //= 10

print(f"Count digits {count}")


"""
I repeatedly divide the number by 10 using integer division.
Each division removes the last digit,
so I increment a counter after every division.
I continue until the number becomes zero.
If the number has d digits, the time complexity is 0(d),
and the space complexity is 0(1).

"""