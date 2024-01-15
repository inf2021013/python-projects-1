# print a message:
# Filename: function1.py
"""
    Πρώτα ορίζεται η συνάρτηση sayWelcome() η οποία περιέχει ως σετ εντολών την εντολή που εκτυπώνει
    το μύνημα: Welcome!
    και στη συνέχεια καλείται 3 φορές εκτελόντας τρείς φορές το σετ των εντολών που περιέχει
"""
def sayWelcome():
    print('Welcome!')

sayWelcome()
sayWelcome()
sayWelcome()

# print the max of 2 numbers:
# Filename: func_param.py
"""
    Ορίζεται η printMax η οποία παίρνει δύο παραμέτρους το l και το k και στη συνέχεια τα συγκρίνει.
    Δηλαδή αν το l είναι μεγαλύτερο απο το k 
    εμφανίζει ότι το l είναι το μέγιστο 
    αλλιώς αν το l είναι ίσο με το k εμφανίζει αντίστοιχα ότι το l είναι ίσο με το k
    αλλιώς εμφανίζει ότι το k είναι είναι το μέγιστο.
    Στη συνέχεια καλείται αρχικά με παραμέτρους τους αριθμούς 9 ως το l και 2 ως το k 
    και εμφανίζει ως αποτέλεσμα ότι το 9 είναι το μέγιστο μετά καλείται με τις μεταβλητές x ως l και y ως k,
    έχοντας το x να παίρνει την τιμή 3 και το y να παίρνει την τιμή 3 και να εμφανίζει ότι είναι ίσα.  
"""
def printMax(l, k):
    if l > k:
        print(l, 'είναι το μέγιστο')
    elif l == k:
        print(l, 'είναι ίσο με το', k)
    else:
        print(k, 'είναι το μέγιστο')
printMax(9, 2)
y = 3
x = 3
printMax(x, y)

"""
 Με τη βιβλιοθήκη sys μας δίνονται πληροφορίες για το λειτουργικό σύστημα,
 για παράδειγμα μπορούμε με την παρακάτω εντολή for να εκτυπώσουμε το path του συγκεκριμένου αρχείου.
"""
# Filename: using_sys.py
import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')
"""
Γίνεται import όλες οι συναρτήσεις-κλάσεις του αρχείου mymodule_demo.py μετά
εκτελείται η συνάρτησή sayhi() του πάνω αρχείου και τυπώνει ως version το '0.342' δηλαδή την τιμή που έχει αποθηκευτεί.
"""
# Filename: mymodule_demo.py
import myModule # Προαιρετικά import *
myModule.sayhi()
print ('Version', myModule.__version__)