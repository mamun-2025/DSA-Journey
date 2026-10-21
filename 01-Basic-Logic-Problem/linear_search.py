


numbers = [10, 20, 30, 40, 50]
target = 30

found = False

for number in numbers:
   if number == target:
      found = True
      break

print(found)

"""
“I use linear search by traversing the array from the beginning and comparing each element with the target. 
If I find the target, I set a flag to true and stop the loop using break. 
If I reach the end without finding it, the result remains false. 
The best-case time complexity is O(1), while the average and worst-case time complexity are O(n). 
The auxiliary space complexity is O(1).”


The best-case time complexity is O(1), 
when the target is found at the first position. 
The worst-case and average-case time complexity are O(n), 
because we may need to scan the array.

"""

# another approch
numbers = [10, 20, 30, 40, 50]
target = 30

found = False

for i in range(len(numbers)):
   if numbers[i] == target:
      found = True
      break

print(found)


# যদি target-এর index দরকার হয়?
numbers = [10, 20, 30, 40, 50]
target = 30

index = -1

for i in range(len(numbers)):
   if numbers[i] == target:
      index = i 
      break

print(index)
