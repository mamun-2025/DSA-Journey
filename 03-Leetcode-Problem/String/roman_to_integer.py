

class Solution:
   def romanToInt(self, s: str) ->int:
      values = {
         "I": 1,
         "V": 5,
         "X": 10,
         "L": 50,
         "C": 100,
         "D": 500,
         "M": 1000,
      }

      total = 0
      for i in range(len(s)):
         current = values[s[i]]

         if i + 1 < len(s):
            next_value = values[s[i+1]]

            if current < next_value:
               total -= current
            else:
               total += current

         else:
            total += current

      return total 


"""

I use a dictionary to map each Roman symbol to its integer value.
Then I travese the string from left to right.
For each character,I compare its value with the next character's value.
If the current value is smaller, I subtract it, otherwise, I add it. 
For the last character, I simply add its value.

"""

         
      