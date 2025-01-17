# Python Strings:
string = 'Cryptography!'
""" 
    Μέσα στη μεταβλητή string αποθηκεύεται 
    η τιμή Cryptography. Η τιμή αυτή είναι σε μορφή συμβολοσειράς.
"""

# Python Lists:
big_list = ['rebghdd', 5463, 5.69, 'george', 274.89]
small_list = [343, 'nick']
"""
    Μέσα στη πρώτη λίστα με όνομα big_list έχουν αποθηκευτεί 4 μεταβλητές διαφορετικού είδους, 
    δηλαδή περιέχει τα εξής δεδομένα: 
    ['rebghdd' (συμβολοσειρά), 5463 (Ακέραιος), 5.69 (Πραγματικός), 'george' (συμβολοσειρά), 274.89 (Πραγματικός)]
    και στην δεύτερη λίστα small_list έχουν αποθηκευτεί 2 άλλες μεταβλητές διαφορετικού είδους,
    δηλαδή περιέχει τα εξής δεδομένα: 
    [343 (Ακέραιος), 'nick' (συμβολοσειρά)]
"""

# Python Tuples:
tuple_datas = (3321, 34525, 6442)
"""
    Μέσα στη πλειάδα με όνομα tuple_datas έχουν αποθηκευτεί 3 μεταβλητές τύπου Ακεραίου int.
    δηλαδή περιέχει τα εξής δεδομένα: 
    (3321 (Ακέραιος), 34525 (Ακέραιος), 6442 (Ακέραιος))
"""
# Python Dictionary:
"""
    Μέσα στο λεξικό με όνομα MiniDictionary υπάρχουν αριστερά τα κλειδιά (keys) και δεξιά οι τιμές (values) 
    δηλαδή ως εξής:
    keys:
        1. first name
        2. last name
        3. grade
    Values:
        1. john
        2. smith
        3. 15.2
"""
MiniDictionary = {'first name': 'john', 'last name': 'smith', 'grade':15.2 }

# εκτυπώνει το αποτέλεσμα της πράξης 9-3=6:
print (9-3)
# εκτυπώνει το αποτέλεσμα της πράξης (23+3)/2*3=39:
print ((23+3)/2*3)

# εκτυπώνει για όλες τις πράξεις το αποτέλεσμα 3.333333333:
print (10/3, 10/3.0, 10.0/3, 10.0/3.0, 10./3,
10/3., 10./3.)

# εκτυπώνει τα αποτέλεσμα για 6**3=216 και για 8**0.5=2.8284271247461903:
print (6**3, 8**0.5)


# Υπολογίζει και Εκτυπώνει τη διακρίνουσα της δευτεροβάθμιας εξίσωσης -4x^2 + 2x + 7=0
a=-4
b=2
c=7
diak=(b*b-4*a*c)
print (diak)
