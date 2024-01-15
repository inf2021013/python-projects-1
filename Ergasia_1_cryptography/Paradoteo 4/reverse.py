"""
Αρχικά αποθηκεύεται στη μεταβλητή message το μήνυμα 'This message is gonna get reversed.'
Στη συνέχεια στο i αποθηκεύεται ως τιμή το μέγεθος των χαρακτήρων του αρχικού μηνύματος μείον 1
έτσι ώστε να ξεκινήσει να παίρνει τα γράμματα από το τέλος του String προς την αρχή του, προσθέτοντάς τα,
ένα-ένα σε ένα άλλο string που ονομάζεται translated
και είναι το αρχικό μήνυμα αντιστραμμένο που εκτυπώνεται στο τέλος.
"""
message = 'This message is gonna get reversed.'
translated = '' #cipher text is stored in this variable
i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1
print("The cipher text is : ", translated)
