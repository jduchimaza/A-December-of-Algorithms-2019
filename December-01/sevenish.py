# sevenish_number
# Brief:  A "sevenish" number is a natural number which is either
#         a power of 7, or the sum of unique powers of 7
# Author: Juan D.H.
# Date:   1 Dec 2019
# 
# This function was written as part of 'A December of Algorithms'
#----------------------------------------------------------------
#
# Define a general n-ish number function
# Arguments: n is the "base" number; i.e., for sevenish, n=7
#            nth is the nth n-ish number
def n_ish_number(n,nth):
   bits = 0 
   n_ish = 0
   while nth > 0: 
       if nth % 2 == 1: val = pow(n,bits) 
       else: val=0
       n_ish = n_ish+val
       bits = bits+1
       nth = nth//2
   return n_ish
#
# Define the sevenish number function that calls n_ish_number
# Arguments: nth is the nth sevenish number
#
def sevenish_number(nth):
   return n_ish_number(7,nth)
#
# Test cases
#
tests=[1,5,10]
for i in tests:
   print("Test "+str(i)+": "+str(sevenish_number(i)))

