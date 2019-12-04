# sevenish_number
# Brief: Algorithm to find the h-index given a list of # of citations 
#        corresponding to papers written by an author.
# Author: Juan D.H.
# Date:   4 Dec 2019
# 
# This function was written as part of 'A December of Algorithms'
#----------------------------------------------------------------

'''
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:
A researcher has index h if at least h of his N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.
For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]
Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.
Given a list of paper citations of Dr. Bruce Banner, calculate his h-index.
'''

def h_index(N, papers):
   # N is the number of publications, should be = len(papers)
   if N != len(papers):
      print("Error: Number of papers given doesn't match number of citations given")
      return 0
   h = 0 # variable h indicates the h-index (int)
   # Sort the papers in reverse order of # of citations
   # Make a copy of the list of # of citations to leave original list intact
   pprs = papers.copy()
   pprs.sort()
   pprs = pprs[::-1]
   # An author has index h if at least h of his N papers have h citations each
   # Iterate through the list and find the index for which the # of citations is higher than that index
   while h < N and pprs[h] > h: h+=1
   return h

# Test Cases:
papers = [4,3,0,1,5]
h = h_index(len(papers), papers)
print("For papers with citations: "+str(papers)+", Dr. Banner has h-index = "+str(h))

papers = [4,5,2,0,6,4]
h = h_index(len(papers), papers)
print("For papers with citations: "+str(papers)+", Dr. Banner has h-index = "+str(h))

