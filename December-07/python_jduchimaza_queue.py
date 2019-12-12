# Function bribe:
# takes a queue and a ID k
# and moves k to the front of the queue if found
# else, do nothing
def bribe(queue, k):
   for entry in queue:
      if k == entry[1]:
         sav=entry
         queue.remove(entry)
         queue.insert(0,entry)
   return None 

N = int(input("Enter N: "))
tuplist = []
print("Enter ID: ")
for i in range(1,N+1):
   inp = input()
   entry = (i,inp)
   tuplist.append(entry)
for x in tuplist:
   print(x)
k = input("Enter k: ")
bribe(tuplist, k)
for x in tuplist:
   print(x)
