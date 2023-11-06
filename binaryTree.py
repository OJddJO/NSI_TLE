from queues import Queue

class Node:
    """A node in a binary tree."""
    def __init__(self, key=None):
        """Constructor for a node in a binary tree, takes a key as parameter."""
        self.key = key



class BinaryTree:
    """A binary tree."""
    def __init__(self, key=None):
        """Constructor for a binary tree, takes a key as parameter."""
        self.root = Node(key)
        self.leftSubTree = None
        self.rightSubTree = None

    def size(self):
        """Returns the number of nodes in the tree."""
        size = 0
        if self.leftSubTree != None:
            size += self.leftSubTree.size()
        if self.rightSubTree != None:
            size += self.rightSubTree.size()
        return size + 1

    def distanceMax(self):
        """Returns the height of the tree using the root and the furthest leaf."""
        leftHeight = self.leftSubTree.distanceMax() if self.leftSubTree != None else 0
        rightHeight = self.rightSubTree.distanceMax() if self.rightSubTree != None else 0
        return max(leftHeight, rightHeight) + 1

    def height(self):
        """Returns the height of the tree using the root and the closest leaf."""
        return self.distanceMax() - 1
    
    def breadthFirst(self):
        """Returns a list of the keys of the tree in breadth-first order."""
        queue = Queue(self.size())
        queue.add(self)
        breadthFirst = []
        while not queue.emptyQueue():
            node = queue.remove()
            breadthFirst.append(node.root.key)
            if node.leftSubTree != None:
                queue.add(node.leftSubTree)
            if node.rightSubTree != None:
                queue.add(node.rightSubTree)
        return breadthFirst

    def prefixe(self):
        """Returns a list of the keys of the tree in prefixe order."""
        prefixe = []
        prefixe.append(self.root.key)
        if self.leftSubTree != None:
            prefixe += self.leftSubTree.prefixe()
        if self.rightSubTree != None:
            prefixe += self.rightSubTree.prefixe()
        return prefixe
    
    def infixe(self):
        """Returns a list of the keys of the tree in infixe order."""
        infixe = []
        if self.leftSubTree != None:
            infixe += self.leftSubTree.infixe()
        infixe.append(self.root.key)
        if self.rightSubTree != None:
            infixe += self.rightSubTree.infixe()
        return infixe
    
    def postfixe(self):
        """Returns a list of the keys of the tree in postfixe order."""
        postfixe = []
        if self.leftSubTree != None:
            postfixe += self.leftSubTree.postfixe()
        if self.rightSubTree != None:
            postfixe += self.rightSubTree.postfixe()
        postfixe.append(self.root.key)
        return postfixe


if __name__ == "__main__":
    tree = BinaryTree(45)
    tree.leftSubTree = BinaryTree(2)
    tree.leftSubTree.leftSubTree = BinaryTree(91)
    tree.leftSubTree.leftSubTree.rightSubTree = BinaryTree(30)
    tree.rightSubTree = BinaryTree(1)
    tree.rightSubTree.rightSubTree = BinaryTree(2)
    tree.rightSubTree.rightSubTree.leftSubTree = BinaryTree(66)
    tree.rightSubTree.rightSubTree.rightSubTree = BinaryTree(8)
    tree.rightSubTree.rightSubTree.rightSubTree.leftSubTree = BinaryTree(33)

    print("Tree size:", tree.size())
    print("Tree height:", tree.height())
    print("Tree distance max:", tree.distanceMax())
    print("Tree in breadth-first order:", tree.breadthFirst())
    print("Tree in prefixe order:", tree.prefixe())
    print("Tree in infixe order:", tree.infixe())
    print("Tree in postfixe order:", tree.postfixe())
