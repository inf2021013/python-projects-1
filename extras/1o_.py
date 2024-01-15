
# Node:
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Συνάρτηση εισαγωγής στοιχείου
    def insert(self, data):
        # Συγκρίνετε τη νέα τιμή με τον γονικό κόμβο
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Συνάρτηση αναζήτησης στοιχείου στο δέντρο
    def search(self, data):
        if data == self.data:
            return "Το στοιχείο υπάρχει!\nΚαι περιέχει τα εξής στοιχεία:"
        if data < self.data:
            if self.left is None:
                return "Το στοιχείο δεν υπάρχει!"
            return self.left.search(data)

        if self.right is None:
            return "Το στοιχείο δεν υπάρχει!"
        return self.right.search(data)

# Εκτύπωση του δέντρου
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# -----------------------------------------
# Τρόποι εμφάνισης του δέντρου
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


# ---------------------------------------------------------------


''' 

                Ψάχνει το index στο οποίο βρίσκεται ο αριθμός που έχει δώσει ο χρήστης από την λίστα: 

'''


def search_index(list, key):
    i = 0
    while i < len(list):
        if key == list[i]:
            return i
        else:
            i = i + 1


# Αρχικοποίηση ρίζας του δέντρου:
root = Node(0)

# Εισαγωγή στοιχειών του αρχείου σε μία λίστα
with open("my_file.txt", "r") as f:
    file = f.readlines()
    L = []
    for line in file:
        L.append(line.strip())  # Διαγραφή "\n"
for i in range(len(L)):
    root.insert(L[i])           # Εισαγωγή στοιχείων της λίστας "1 προς 1" στο δέντρο

# Ask for input:
key = input("Δώσε αριθμό για να εμφανιστούν τα επόμενα 3 στοιχεία:")
print(root.search(key))

# PRINT STRING 1-2-3:
index = search_index(L, key)
print(L[index])         # Το στοιχείο που δόθηκε.
print(L[index + 1])       # Το 1ο string που είναι απο κάτω του.
print(L[index + 2])       # Το 2ο string που είναι απο κάτω του.
print(L[index + 3])       # Το 3ο string που είναι απο κάτω του.

# Ελεγχός εγκυρώτητας κωδικού
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
