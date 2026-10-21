

# built-in count
numbers = [5, 2, 3, 5, 5, 5]
result = numbers.count(5)
print(result)


# Loop count
numbers = [1, 2, 2, 2, 3, 4]
target = 2

count = 0

for number in numbers:
   if number == target:
      count += 1

print(count)
"""
I initialize a counter to zero and traverse the array once.
Whenever an element equals the target, I increment the counter.
I don't stop after the first match because I need to count all occurences.
The time complexity is 0(n) and the auxiliary space complexity is 0(1).

"""

# frquency count
numbers = [1, 2, 3, 2, 2, 4]
frequency = {}

for number in numbers:
   if number in frequency:
      frequency[number] += 1
   else:
      frequency[number] = 1

print(frequency)