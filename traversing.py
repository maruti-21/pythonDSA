class Node:
    # create a node in the tree
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # insert root node if there is no root node
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self, rootNode, value):
        if value < rootNode.data:
            if rootNode.left is None:
                rootNode.left = Node(value)
            else:
                self.insertNode(rootNode.left, value)
        else:
            if rootNode.right is None:
                rootNode.right = Node(value)
            else:
                self.insertNode(rootNode.right, value)

    def inorder(self, rootNode):
        if rootNode is not None:
            self.inorder(rootNode.left)
            print(rootNode.data, end=" ")
            self.inorder(rootNode.right)


# object creation
btobj = BinaryTree()

# inserting values
btobj.insert(50)
btobj.insert(30)
btobj.insert(70)
btobj.insert(20)
btobj.insert(40)
btobj.insert(60)
btobj.insert(80)

print("Inorder traversal:")
btobj.inorder(btobj.root)