
import time


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

#Συνάρτηση εισαγωγής στοιχείου
    def insert(self, data):
    # Συγκρίση της νέας τιμής με τον γονικό κόμβο
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Εμφάνιση του Δέντρου
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
#---------------------------------------------
#Τρόποι εμφάνισης του δέντρου
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res
#----------------------------------------------------------------
#Συνάρτηση αναζήρησης στοιχείου
    def search(self, data):
        if data == self.data:
            return True

        if data < self.data:
            if self.left == None:
                return False
            return self.left.search(data)

        if self.right == None:
            return False
        return self.right.search(data)

#Αρχικοποίηση ρίζας του δέντρου
root = Node(0)

#Φορτωσή εγγραφών στο δέντρο
with open("my_file.txt", "r") as f:
    file = f.readlines()
    L = []
    for line in file:
        L.append(line.strip())
for i in range(len(L)):
    root.insert(L[i])


#Αναζήτηση ενός στοιχείου
question=input("Θέλετε να αναζητήσετε κάποιο στοιχείο απο το δέντρο(Y/N)?:")
if question == "Y":
   element = input("Δώσε ένα στοιχείο:")
   print(root.search(element))
else:
    print("")



#Ελεγχός εγκυρώτητας κωδικού
option = input("Τρόπος επιλογής παρουσίασης δέντρου(in=inorder,pr=preorder,po=postorder:")
if option == "in":
    print(root.inorderTraversal(root))
elif option == "pr":
    print(root.PreorderTraversal(root))
elif option == "po":
    print(root.PostorderTraversal(root))
while option != "in" and option != "pr" and option != "po":
    print("Λάθος κωδικός!Δοκιμάστε ξανα:")
    option = input("Τρόπος επιλογής παρουσίασης δέντρου(in=inorder,pr=preorder,po=postorder:")
    if option == "in":
        print(root.inorderTraversal(root))
    elif option == "pr":
        print(root.PreorderTraversal(root))
    elif option == "po":
        print(root.PostorderTraversal(root))


