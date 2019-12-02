'''
Problem
Are credit card numbers just a random combination of the digits from 0-9? NO!
Credit card numbers are a systematic combination of numbers that can satisfy a single test. This test is created so that errors can be avoided while typing in credit card numbers as well as detect counterfeit cards!

The algorithm is as follows:

1. Reverse the order of the digits in the number.
2. Take the first, third, ... and every other odd digit in the reversed digits and sum them to form the partial sum s1
3. Taking the second, fourth ... and every other even digit in the reversed digits:
3a. Multiply each digit by two and sum the digits if the answer is greater than nine to form partial sums for the even digits
3b. Sum the partial sums of the even digits to form s2
4. If s1 + s2 ends in zero then the original number is in the form of a valid credit card number as verified by the Luhn test.

Example

Input : 49927398716
Output: 49927398716 passes the test
'''

def trans_even(x):
   x *= 2
   if x > 9:
      return x//10+x%10
   else:
      return x
def is_cc_number(cc_num):
   string_cc = str(cc_num)
   string_cc = string_cc[::-1] # Reverse the order of the digits
   int_cc = list(map(int,string_cc))
   # Sum all the odd digits
   s1 = sum(int_cc[::2])
   # Sum of evens
   # trans_even multiplies each even num by 2 and form partial sums
   s2 = sum(list(map(trans_even,int_cc[1::2])))
   return (s1+s2)%10==0

#cc = int(49927398716)
cc = 61789372994
if is_cc_number(cc): print(str(cc)+" passes the test")
else: print(str(cc)+" is a fake")
