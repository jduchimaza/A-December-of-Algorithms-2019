'''
Henry wants to generate prime numbers present in the Fibonacci Series. He needs your help to generate them.
For example, suppose N = 3
Then the series will have 3 Fibonacci prime numbers : 2,3,5
Given the count of prime numbers needed by Henry , compute the series for him.
'''

# function isPrime
# takes in an integer n
# returns True if the integer is a prime number
def isPrime(n):
   if n>1:
      for i in range(2,n//2):
         if n%i == 0:
            return False
      return True
   else:
      return False


# function fibonacci
# takes in an integer n
# returns the nth number in the fibonacci number sequence
def fibonacci(n):
   if n == 1 or n == 2:
      return int(1)
   else:
      return int(fibonacci(n-1)+fibonacci(n-2))

# functino primeFib
# takes in an integer n
# returns a Fibonacci sequence with length n
#   that includes only prime numbers
def primeFib(n):
   seq = []
   i = 1
   while len(seq)!=n:
      fib = fibonacci(i)
      if(isPrime(fib)):
         seq.append(fibonacci(i))
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
