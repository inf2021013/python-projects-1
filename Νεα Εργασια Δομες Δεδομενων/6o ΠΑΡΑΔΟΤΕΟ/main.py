import time
from sorts import Bubble_sort
L=[]
ftime=0
#for i in range(20000):
filename = 'my_file.txt'
with open(filename) as domes:
    for i in domes:
         L.append(i)
# ------------------------------------
for i in range(1000):
 n=len(L)
 c = time.time()
 Bubble_sort(L)
 b = time.time()
#------------------------------------
ftime=ftime+(b-c)
print("Ο χρόνος εκτέλεσης της bubblesort είναι:",ftime)