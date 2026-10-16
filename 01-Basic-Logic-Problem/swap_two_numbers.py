

# Pythonic way
a = 10
b = 20

a, b = b, a 

print(a)
print(b)



# Temp Varialbe (Traditional Method)
a = 10
b = 20

temp = a 
a = b 
b = temp 

print(a)
print(b)

"""
We can swap two numbers using a variable.
First, I store the value of a in temp, 
then I assign b to a and finally assign b to temp.
The time complexity is 0(1) and space complexity is 0(1).
In python, We can also use tuple unpacking: a, b = b, a.

"""