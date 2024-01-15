import random
import string
import new_sorts


# --------------------------
# Δημιουργία κλάσης record
class record:
    def __init__(self, i, s1, s2, s3):
        self.i = i
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def __str__(self):
        return (str)(self.i) + " - " + self.s1 + " - " + self.s2 + " - " + self.s3

# Δημιουργία αρχείου
def create_file(file_name, num_items):
    # Open File:
    f = open(file_name, "w")
    for i in range(num_items):
        # Random integer form 0 to 1.000.000:
        num = random.randint(0, 1000000)
        # Random strings for s1, s2 and s3:
        s1 = ''.join((random.choice(string.ascii_letters) for x in range(10)))
        s2 = ''.join((random.choice(string.ascii_letters) for x in range(10)))
        s3 = ''.join((random.choice(string.ascii_letters) for x in range(10)))
        # Write in given file name:
        f.write(str(num) + "\n")
        f.write(s1 + "\n")
        f.write(s2 + "\n")
        f.write(s3 + "\n")
    f.close()


# Ανάγνωση αρχείου
def read_file_in_list(file_name):
    l = []
    f = open(file_name, "r")
    info = f.read()
    lines = info.split("\n")
    i = 0
    while i < len(lines) and lines[i] != "":
        l.append(record(int(lines[i]), lines[i + 1], lines[i + 2], lines[i + 3]))
        i += 4
    f.close()
    return l
#Εμφάνιση λίστας
def show_list(l, title):
    print(title)
    for item in l:
        print(item)
    print()


"""
-----------------------------------
"""

# Bubble-Sort:
create_file("my_file.txt", 100)
l = read_file_in_list("my_file.txt")
show_list(l, "Πριν από Bubble_sort")
new_sorts.Bubble_sort(l)
show_list(l, "Μετά από Bubble_sort")


"""
-----------------------------------
"""
# selectionSort:
'''
create_file("my_file.txt", 100)
l = read_file_in_list("my_file.txt")
show_list(l, "Πριν από selectionSort")
new_sorts.selectionSort(l,len(l))
show_list(l, "Μετά από selectionSort")
'''

"""
-----------------------------------
"""

# mergeSort:
'''
create_file("my_file.txt", 100)
l = read_file_in_list("my_file.txt")
show_list(l, "Πριν από mergeSort")
new_sorts.mergeSort(l)
show_list(l, "Μετά από mergeSort")
'''
"""
-----------------------------------
"""

# heapSort:
'''
create_file("my_file.txt", 100)
l = read_file_in_list("my_file.txt")
show_list(l, "Πριν από heapSort")
new_sorts.heapSort(l)
show_list(l, "Μετά από heapSort")
'''
"""

-----------------------------------
"""
# insertionSort:
'''
create_file("my_file.txt", 100)
l = read_file_in_list("my_file.txt")
show_list(l, "Πριν από insertionSort")
new_sorts.insertionSort(l)
show_list(l, "Μετά από insertionSort")
'''

"""
-----------------------------------
"""
# quickSort:
'''
create_file("my_file.txt", 100)
l = read_file_in_list("my_file.txt")
show_list(l, "Πριν από quickSort")
new_sorts.quickSort(l,0,len(l)-1)
show_list(l, "Μετά από quickSort")

'''

"""
-----------------------------------
"""
# shellSort:
'''
create_file("my_file.txt", 100)
l = read_file_in_list("my_file.txt")
show_list(l, "Πριν από shellSort")
new_sorts.shellSort(l,len(l))
show_list(l, "Μετά από shellSort") 
'''
