"""
 Αρχικά στο X αποθηκεύεται η τιμή 2 και ελέγχεται συνεχώς μέχρι το X να πάρει την τιμή 8, εκτυπώνοντας
 κάθε φορά την τιμή του Χ. Δηλαδή σε αυτήν την περίπτωση θα εκτυπώσει τα εξής:
    2
    3
    4
    5
    6
    7
    Ο βρόχος loop τερματίστηκε

"""
for X in range(2, 8):
    print(X)
else:
    print('Ο βρόχος loop τερματίστηκε')