"""
 Αρχικά δημιουργείται μία λίστα με διάφορα ψώνια, όπου
    εκτυπώνεται το μέγεθος της λίστας και το κάθε αντικείμενό της ξεχωριστά,
    προσθέτεται το ρύζι στη λίστα και εκτυπώνεται η νέα λίστα,
    εκτυπώνεται η λίστα ταξινομημένη,
    εκτυπώνεται το πρώτο αντικείμενο της λίστας ('χυμός πορτοκάλι') και αποθηκεύεται στη μεταβλητή olditem.
    Στη συνέχεια αφαιρείται ο 'χυμός πορτοκάλι' από τη λίστα δίοτι αγοράζεται και εκτυπώνεται
    το olditem καθώς και η ανανεωμένη λίστα.
"""
# Filename: using_list.py
shoplist = ['χυμός πορτοκάλι', 'πατάτες', 'μπριζόλες',
'ντομάτες', 'μαγιονέζα']
print('Πρέπει ν\' αγοράσω', len(shoplist),
'πράγματα.')
print('Τα πράγματα αυτά είναι:', end=' ')
for item in shoplist:
    print(item, end=' ')
print('\nΠρέπει επίσης ν\' αγοράσω ρύζι.')
shoplist.append('ρύζι')
print('Η λίστα αγορών μου τώρα είναι:',
shoplist)
print('Θα ταξινομήσω τη λίστα μου τώρα')
shoplist.sort()
print('Η ταξινομημένη λίστα μου είναι',
      shoplist)
print('Το πρώτο πράγμα που θ\' αγοράσω είναι',
      shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Αγόρασα το',
      olditem)
print('Η λίστα αγορών μου τώρα είναι',
      shoplist)
"""
Αρχικά αποθηκεύεται στη μεταβλητή message το μήνυμα 'This message is gonna get reversed.'
στη συνέχεια στο i αποθηκεύεται ως τιμή το μέγεθος των χαρακτήρων του αρχικού μηνύματος μείον 1 
έτσι ώστε να ξεκινήσει να παίρνει τα γράμματα από το τέλος του String προς την αρχή του, προσθέτοντάς τα,
ένα-ένα σε ένα άλλο string που ονομάζεται translated 
και είναι το αρχικό μήνυμα αντιστραμμένο που εκτυπώνεται στο τέλος. 
"""
# Filename: reverse.py
message = 'This message is gonna get reversed.'
translated = '' #cipher text is stored in this variable
i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1
print("The cipher text is : ", translated)
