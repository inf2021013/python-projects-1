import random
import sys
import string



# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

 # Συνάρτηση εισαγωγής κόμβου
    def insert_node(self, root, key):

        # Ευρεση της σωστής θέσης και εισαγωγής του κόμβου σε αυτήν
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

    # Ενημέρωση του balance factor και εξισορρόπηση του δέντρου
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root


# Σύναρτηση για τη διαγραφή ενός κόμβου
    def delete_node(self, root, key):

    # Εύρεση τού κόμβου που θέλουμε να διαγράψουμε και διαγραφή του συγκεκριμένου κόμβου
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

    # Ενημερώση του balance factor των κόμβων
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

    # εξισορρόπηση του δέντρου
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

# Συνάρτηση για εκτέλεση αριστερής περιστροφής
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

# Συνάρτηση για εκτέλεση δεξιάς περιστροφής
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

# Λάβετε το ύψος του κόμβου
    def getHeight(self, root):
         if not root:
            return 0
         return root.height

# Λάβετε τον παράγοντα ισορροπίας του κόμβου
    def getBalance(self, root):
         if not root:
            return 0
         return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

#Εμφάνιση Δέντρου
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)



#-----------------------------------------------------------
# Διαδρομές Δέντρου

    def preorder(self, root):

        if root:
            # Traverse root
            print(str(root.key) + "\n")
            # Traverse left
            self.preorder(root.left)
            # Traverse right
            self.preorder(root.right)

    def postorder(self, root):

        if root:
            # First recur on left child
            self.postorder(root.left)

            # the recur on right child
            self.postorder(root.right)

            # now print the data of node
            print(str(root.key) + "\n")

    def inorder(self, root):

        if root:
            # First recur on left child
            self.inorder(root.left)

            # then print the data of node
            print(str(root.key) + "\n")

            # now recur on right child
            self.inorder(root.right)

#Συνάρτηση αναζήτησης στοιχείου στο δέντρο
def search_index(list, key):
    i = 0
    while i < len(list):
     if key == list[i]:
        return i
     else:
        i = i + 1


myTree = AVLTree()
root = None
#Εισαγώγη στοιχείων στο avl δέντρο
with open("my_file.txt", "r") as f:
    file = f.readlines()
    L = []
    for line in file:
        L.append(line.strip())
for i in L:
    root = myTree.insert_node(root,i)




#εμφάνιση δέντρου
myTree.printHelper(root, "", True)

#Εμφάνιση Αναζήτησης στοιχείου
key = input("Δώσε αριθμό για να εμφανιστούν τα επόμενα 3 στοιχεία:")

# PRINT STRING 1-2-3:
index = search_index(L, key)
print(L[index])         # Το στοιχείο που δόθηκε.
print(L[index + 1])       # Το 1ο string που είναι απο κάτω του.
print(L[index + 2])       # Το 2ο string που είναι απο κάτω του.
print(L[index + 3])       # Το 3ο string που είναι απο κάτω του.




#Ελεγχός εγκυρώτητας κωδικού
option = input("Τρόπος επιλογής παρουσίασης δέντρου(in=inorder,pr=preorder,po=postorder:")
if option == "in":
    print(myTree.inorder(root))
elif option == "pr":
    print(myTree.preorder(root))
elif option == "po":
    print(myTree.postorder(root))
while option != "in" and option != "pr" and option != "po":
    print("Λάθος κωδικός!Δοκιμάστε ξανα:")
    option = input("Τρόπος επιλογής παρουσίασης δέντρου(in=inorder,pr=preorder,po=postorder:")
    if option == "in":
        print(myTree.inorder(root))
    elif option == "pr":
        print(myTree.preorder(root))
    elif option == "po":
        print(myTree.postorder(root))



