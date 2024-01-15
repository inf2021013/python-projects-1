import time


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Συνάρτηση εισαγωγής στοιχείου
    def insert(self, data):
        # Σύγκριση της νέας τιμής με τον γονικό κόμβο
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

    # ------------------------------------
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

    # ----------------------------------------------------------------
    # Συνάρτηση αναζήτησης στοιχείου
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


# Φόρτωση εγγραφών στο δέντρο και καταγραφή χρόνου
with open("my_file.txt", "r") as f:
    file = f.readlines()
    L = []
    for line in file:
        L.append(line.strip())
for i in range(len(L)):
    root.insert(L[i])


#Καταμέτρηση χρόνου
give = int(input("Πόσα στοιχεία θέλετε να αναζητήσετε?:"))
sum = 0
for i in range(give):
    n = input("Δώστε ένα στοιχείο:")
    start = time.time()
    root.search(n)
    stop = time.time()
    sum = 100*(stop - start) + sum

#Καταμέτρηση χρόνου των διασχίσεων του δέντρου
startPre = time.time()
print(root.PreorderTraversal(root))
stopPre = time.time()
Pre = stopPre-startPre

startIn = time.time()
print(root.inorderTraversal(root))
stopIn = time.time()
In = stopIn-startIn

startPo = time.time()
print(root.PostorderTraversal(root))
stopPo = time.time()
Po = stopPo-startPo

#Εισαγωγή καταμέτρησης χρόνου διάσχισης δέντρου σε αρχείο
with open("Time calculation for Tree Traversal.txt", "w", encoding="utf-8") as time:
    time.write(str(In)+"\n")
    time.write(str(Po)+"\n")
    time.write(str(Pre)+"\n")
time.close()

# Εισαγωγή καταμέτρησης χρόνου στοιχειών σε αρχείο
with open("time_calculation binary tree.txt", "w", encoding="utf-8") as calt:
    calt.write("Ο χρόνος μέτρησης αναζήτησης στοιχείων είναι:\n")
    calt.write(str(sum) + "\n")
calt.close()
