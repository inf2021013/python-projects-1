import sys
import time

# Δημιουργία ενός κόμβου δέντρου
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



    #Ενημέρωση του balance factor και εξισορρόπηση του δέντρου
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
    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height


    # Λάβετε τον παράγοντα ισορροπίας του κόμβου
    # Get balance factore of the node
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


    #Συνάρτηση Αναζήτησης στοιχείου
    def Search(self,root, key):
        if (root is None):
            return False
        elif (root.key == key):
            return key
        elif (root.key < key):
            return self.Search(root.right, key)
        return self.Search(root.left, key)

    # Διαδρομές Δέντρου

    def preorder(self, root):

        if root:
            # Traverse root
            str(root.key) + "\n"
            # Traverse left
            self.preorder(root.left)
            # Traverse right
            self.preorder(root.right)

    def postorder(self, root):

        if root:
            # Πρώτη επανεμφάνιση στο αριστερό παιδί
            self.postorder(root.left)

            # επανάληψη στο δεξί παιδί
            self.postorder(root.right)

            # εκτύπωση των δεδομένων του κόμβου
            str(root.key) + "\n"

    def inorder(self, root):

        if root:
            # Πρώτη επανεμφάνιση στο αριστερό παιδί
            self.inorder(root.left)

            # εκτύπωση των δεδομένων του κόμβου
            str(root.key) + "\n"

            # εκτύπωση των δεδομένων του κόμβου
            self.inorder(root.right)





#κλήση της κλάσης AVLTree
myTree = AVLTree()

#Αρχικοποίηση του κόμβου
root = None

#Εισαγώγη στοιχείων στο avl δέντρο
start1 = time.time()
with open("my_file.txt", "r") as f:
    file = f.readlines()
    L = []
    for line in file:
        L.append(line.strip())
for i in range(len(L)):
    root = myTree.insert_node(root,L[i])
stop1 = time.time()

#Εμφάνιση Αναζήτησης στοιχείου
key=input("Δώσε στοιχείο προς αναζήτηση:")
start2 = time.time()
myTree.Search(root,str(key))
stop2 = time.time()

#Καταμέτρηση χρόνου των διασχίσεων του δέντρου
startPre = time.time()
myTree.preorder(root)
stopPre = time.time()
Pre = stopPre-startPre

startIn = time.time()
myTree.inorder(root)
stopIn = time.time()
In = stopIn-startIn

startPo = time.time()
myTree.postorder(root)
stopPo = time.time()
Po = stopPo-startPo

#Εισαγωγή καταμέτρησης χρόνου διάσχισης δέντρου σε αρχείο
with open("Time calculation for Tree Traversal.txt", "w", encoding="utf-8") as time:
    time.write(str(In)+"\n")
    time.write(str(Po)+"\n")
    time.write(str(Pre)+"\n")
time.close()

#Εμφάνιση χρονου για την αναζήτηση και την εισαγωγή
with open("time_calculation avl tree.txt", "w", encoding = "utf-8") as time:
    time.write("Ο χρόνος μέτρησης εισαγωγής στοιχείων είναι:")
    time.write(str(stop1 - start1) + "\n")
    time.write("Ο χρόνος μέτρησης αναζήτησης στοιχείων είναι:\n")
    time.write(str(stop2 - start2) + "\n")
time.close()
