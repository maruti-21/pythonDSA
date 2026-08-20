class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertnode(self.root, value)

    def insertnode(self, rootnode, value):
        if value < rootnode.data:
            if rootnode.left is None:
                rootnode.left = Node(value)
            else:
                self.insertnode(rootnode.left, value)
        else:
            if rootnode.right is None:
                rootnode.right = Node(value)
            else:
                self.insertnode(rootnode.right, value)

    # 🌳 TREE HEIGHT
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # 🌳 PRINT LEVEL (for centered tree)
    def print_level(self, node, level, space):
        if node is None:
            print(" " * space, end="")
            return

        if level == 1:
            print(str(node.data).center(space), end="")
        else:
            self.print_level(node.left, level - 1, space)
            self.print_level(node.right, level - 1, space)

    # 🌳 PERFECT TREE STRUCTURE
    def print_tree(self):
        h = self.height(self.root)
        space = 4 * (2 ** h)

        for i in range(1, h + 1):
            self.print_level(self.root, i, space)
            print("\n")
            space //= 2

    # 🔹 INORDER (LNR)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # 🔹 PREORDER (NLR)
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # 🔹 POSTORDER (LRN)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
    def levelOrderTraversal(self,rootNode):
        if rootNode is None:
            return
        queue = []
        queue.append(rootNode)
        while len(queue) > 0:
            currentnode = queue.pop(0)
            print(currentnode.data,end=" ")
            if currentnode.leftChild is not None:
                queue.append(currentnode.leftChild)
            if currentnode.rightChild is not None:
                queue.append(currentnode.rightChild)

# -------- RUN --------
bt = BinaryTree()
bt.insert(50)
bt.insert(30)
bt.insert(70)
bt.insert(20)
bt.insert(40)
bt.insert(60)
bt.insert(80)

print("\n🌳 TREE STRUCTURE:\n")
bt.print_tree()

print("Inorder Traversal (LNR):")
bt.inorder(bt.root)

print("\n\nPreorder Traversal (NLR):")
bt.preorder(bt.root)

print("\n\nPostorder Traversal (LRN):")
bt.postorder(bt.root)

print("levelOrderTraversal:")
bt.levelOrderTraversal(bt.root)