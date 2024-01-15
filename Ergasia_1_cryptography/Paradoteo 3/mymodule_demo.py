"""
Γίνεται import όλες οι συναρτήσεις-κλάσεις του αρχείου mymodule_demo.py μετά
εκτελείται η συνάρτησή sayhi() του πάνω αρχείου και τυπώνει ως version το '0.342' δηλαδή την τιμή που έχει αποθηκευτεί.
"""
import myModule
myModule.sayhi()
print ('Version', myModule.__version__)