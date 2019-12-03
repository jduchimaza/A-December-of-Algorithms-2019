'''
While the list isn't sorted, snap half of all things (remove them from the list). Proceed until the list is sorted or only one item remains (which is sorted by default). This sorting algorithm may give varied results based on implementation.
The item removal (decimation) procedure is up to the implementation to decide, but the list should be half as long as before after one pass of the item removal procedure.
Your algorithm may commit to take away either the first half of the list, the last half of the list, all odd items, all even items, one at a time until the list is half as long, or any not specified above.
'''



def snap(list1):
   list1=list1[::2]
   return list1

list1=[1, 2, 3, 4, 5]
list2=[1, 2, 3, 4, 3]
snap_cnt = 0
wrk = list1
while sorted(wrk)!=wrk:
   wrk=snap(wrk)
   snap_cnt+=1
print("I finally rest. And watch the sun rise on a grateful universe.")
print("And all it took was "+str(snap_cnt)+" snaps.")
