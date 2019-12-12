# fibonacci  
# Brief: Find the first n prime numbers in the Fibonacci sequence
# Author: Juan D.H.
# Date:   6 Dec 2019 (comp 11 Dec)
# 
# This function was written as part of 'A December of Algorithms'
#----------------------------------------------------------------

'''
Henry wants to generate prime numbers present in the Fibonacci Series. He needs your help to generate them.
For example, suppose N = 3
Then the series will have 3 Fibonacci prime numbers : 2,3,5
Given the count of prime numbers needed by Henry , compute the series for him.
'''
from math import sqrt

# function isPrime
# takes in an integer n
# returns True if the integer is a prime number
def isPrime(n):
   if n>1:
      for i in range(2,int(sqrt(n))+1):
         if n%i == 0:
            return False
      return True
   else:
      return False


# function primeFib
# takes in an integer n
# returns a Fibonacci sequence with length n
#   that includes only prime numbers
def primeFib(n):
   seq = []
   a=1
   b=1
   i = 1
   while len(seq)!=n:
      fib = b
      b = b+a
      a = fib
      if(isPrime(fib)):
         seq.append(fib)
      i+=1
   return seq
      
n = int(input("Enter the value for (n): "))
print("Generated Fibonacci Prime Number Generation up to ("+str(n)+"):")
print(primeFib(n))
'''
  Enter the value for (n): 5
  
  Generated Fibonacci Prime Number Generation upto (5): 
  2, 3, 5, 13, 89
'''
