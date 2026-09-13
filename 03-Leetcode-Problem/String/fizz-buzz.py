

class Solution:
   def fizzBuzz(self, n:int) ->list[str]:
      answer = []

      for i in range(1, n + 1):

         if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")

         elif i % 3 == 0:
            answer.append("Fizz")

         elif i % 5 == 0:
            answer.append("Buzz")

         else:
            answer.append(str(i))

      return answer 


"""
We iterate from 1 to n. 
For each number, we check whether it is divisible by both 3 and 5.
If it is, we add "FizzBuzz". 
Otherwise, if it is divisible by 3, we add "Fizz".
If it is divisible by 5, we add "Buzz".
Otherwise, we add the number as a string.
Finally, we return the result list.
"""
      