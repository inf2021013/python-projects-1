import time
import random
# Κάνω import όλες τις ταξινομήσεις από το script sorts.
from sorts import *

# Bubble-Sort
print("")
print("Ο χρόνος εκτέλεσης της ταξινόμησης Bubble-Sort σε κάθε σενάριο είναι:")
List = []
n = 100
''' 
Για κάθε ένα από τα 10 σενάρια, 
γεμίζω τη λίστα με τυχαίους αριθμούς από το 1 μέχρι το 1.000.000,
δηλαδή στο 1ο σενάριο την γεμίζω, με 100 τυχαίους ακεραίους, στο 2ο με 200, στο 3ο με 300 κλπ μέχρι 1.000.
Μετά μετράω τον χρόνο που έκανε η bubble sort να ταξινομήσει τη λίστα.
'''
for j in range(10):
 ftime = 0
 for i in range(n):
  List.append(random.randint(0,1000000))
 c = time.time()
 Bubble_sort(List)
 b = time.time()
 #------------------------------------
 ftime = ftime+(b-c)
 print(str(j + 1) + "o σενάριο", ftime)
 List.clear()
 n = n + 100

# Selection-Sort:
"""
print("")
print("Ο χρόνος εκτέλεσης της ταξινόμησης Selection-Sort σε κάθε σενάριο είναι:")
List = []
n=100
''' 
Για κάθε ένα από τα 10 σενάρια, 
γεμίζω τη λίστα με τυχαίους αριθμούς από το 1 μέχρι το 1.000.000,
δηλαδή στο 1ο σενάριο την γεμίζω, με 100 τυχαίους ακεραίους, στο 2ο με 200, στο 3ο με 300 κλπ μέχρι 1.000.
Μετά μετράω τον χρόνο που έκανε η Selection-Sort να ταξινομήσει τη λίστα.
'''
for j in range(10):
 ftime = 0
 for i in range(n):
  List.append(random.randint(0,1000000))
 c = time.time()
 selectionSort(List,len(List))
 b = time.time()
 #------------------------------------
 ftime = ftime+(b-c)
 print(str(j+1)+"o σενάριο",ftime)
 List.clear()
 n = n + 100
"""

# Merge-Sort:
"""
print("")
print("Ο χρόνος εκτέλεσης της ταξινόμησης Merge-Sort σε κάθε σενάριο είναι:")
List = []
n = 100
''' 
Για κάθε ένα από τα 10 σενάρια, 
γεμίζω τη λίστα με τυχαίους αριθμούς από το 1 μέχρι το 1.000.000,
δηλαδή στο 1ο σενάριο την γεμίζω, με 100 τυχαίους ακεραίους, στο 2ο με 200, στο 3ο με 300 κλπ μέχρι 1.000.
Μετά μετράω τον χρόνο που έκανε η Merge-Sort να ταξινομήσει τη λίστα.
'''
for j in range(10):
 ftime = 0
 for i in range(n):
  List.append(random.randint(0,1000000))
 c = time.time()
 mergeSort(List)
 b = time.time()
 #------------------------------------
 ftime = ftime+(b-c)
 print(str(j + 1) + "o σενάριο", ftime)
 List.clear()
 n = n + 100
"""

# Heap-Sort:
"""
print("")
print("Ο χρόνος εκτέλεσης της ταξινόμησης Heap-Sort σε κάθε σενάριο είναι:")
List = []
n = 100
''' 
Για κάθε ένα από τα 10 σενάρια, 
γεμίζω τη λίστα με τυχαίους αριθμούς από το 1 μέχρι το 1.000.000,
δηλαδή στο 1ο σενάριο την γεμίζω, με 100 τυχαίους ακεραίους, στο 2ο με 200, στο 3ο με 300 κλπ μέχρι 1.000.
Μετά μετράω τον χρόνο που έκανε η Heap-Sort να ταξινομήσει τη λίστα.
'''
for j in range(10):
 ftime = 0
 for i in range(n):
  List.append(random.randint(0,1000000))
 c = time.time()
 heapSort(List)
 b = time.time()
 #------------------------------------
 ftime = ftime+(b-c)
 print(str(j+1)+"o σενάριο",ftime)
 List.clear()
 n = n + 100
"""

# Insertion-Sort:
"""
print("")
print("Ο χρόνος εκτέλεσης της ταξινόμησης Insertion-Sort σε κάθε σενάριο είναι:")
List = []
n=100
''' 
Για κάθε ένα από τα 10 σενάρια, 
γεμίζω τη λίστα με τυχαίους αριθμούς από το 1 μέχρι το 1.000.000,
δηλαδή στο 1ο σενάριο την γεμίζω, με 100 τυχαίους ακεραίους, στο 2ο με 200, στο 3ο με 300 κλπ μέχρι 1.000.
Μετά μετράω τον χρόνο που έκανε η Insertion-Sort να ταξινομήσει τη λίστα.
'''
for j in range(10):
 ftime = 0
 for i in range(n):
  List.append(random.randint(0,1000000))
 c = time.time()
 insertionSort(List)
 b = time.time()
 #------------------------------------
 ftime = ftime+(b-c)
 print(str(j+1)+"o σενάριο",ftime)
 List.clear()
 n = n + 100
"""

# Quick-Sort:
"""
print("")
print("Ο χρόνος εκτέλεσης της ταξινόμησης Quick-Sort σε κάθε σενάριο είναι:")
List = []
n=100
''' 
Για κάθε ένα από τα 10 σενάρια, 
γεμίζω τη λίστα με τυχαίους αριθμούς από το 1 μέχρι το 1.000.000,
δηλαδή στο 1ο σενάριο την γεμίζω, με 100 τυχαίους ακεραίους, στο 2ο με 200, στο 3ο με 300 κλπ μέχρι 1.000.
Μετά μετράω τον χρόνο που έκανε η Quick-Sort να ταξινομήσει τη λίστα.
'''
for j in range(10):
 ftime = 0
 for i in range(n):
  List.append(random.randint(0,1000000))
 c = time.time()
 quickSort(List,0,len(List)-1)
 b = time.time()
 #------------------------------------
 ftime = ftime+(b-c)
 print(str(j+1)+"o σενάριο",ftime)
 List.clear()
 n = n + 100
"""

# Shell-Sort:
"""
print("")
print("Ο χρόνος εκτέλεσης της ταξινόμησης Shell-Sort σε κάθε σενάριο είναι:")
List = []
n=100
''' 
Για κάθε ένα από τα 10 σενάρια, 
γεμίζω τη λίστα με τυχαίους αριθμούς από το 1 μέχρι το 1.000.000,
δηλαδή στο 1ο σενάριο την γεμίζω, με 100 τυχαίους ακεραίους, στο 2ο με 200, στο 3ο με 300 κλπ μέχρι 1.000.
Μετά μετράω τον χρόνο που έκανε η Shell-Sort να ταξινομήσει τη λίστα.
'''
for j in range(10):
 ftime = 0
 for i in range(n):
  List.append(random.randint(0,1000000))
 c = time.time()
 shellSort(List,len(List))
 b = time.time()
 #------------------------------------
 ftime = ftime+(b-c)
 print(str(j+1)+"o σενάριο",ftime)
 List.clear()
n = n + 100
"""