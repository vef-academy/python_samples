###############################################################################
# Name        : AvlTree.py
# Author      :
# Version     :
# Copyright   : Your copyright notice
# Description : Create AvlNode, AvlTree class
###############################################################################

class AvlNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

class AvlTree:
    def __init__(self, key=None):
        if key is None:
            self.root = None
        else:
            self.root = AvlNode(key)

    def insert(self, key):
        # Implement your code here
        pass

    def delete(self, node):
        # Implement your code here
        pass
    
    def search(self, key):
        # Implement your code here
        pass
    
    def isTreeBalanced(self):
        # Implement your code here
        pass

    def printInOrder(self):
        # Implement your code here
        pass

    def printPreOrder(self):
        # Implement your code here
        pass

    def printPostOrder(self):
        # Implement your code here
        pass

if __name__ == "__main__":
    tree = AvlTree()
    # Basic test insert function
    listNode = [40, 20, 60, 10, 30, 50, 70,
                5, 1, 35, 37, 45, 47, 75, 72]
    for i in listNode:
        tree.insert(i)
        if not(tree.isTreeBalanced()):
            print("Tree is un-balance, after inserting ", i)
            break
