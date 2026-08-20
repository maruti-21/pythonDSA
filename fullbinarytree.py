# each node has either 0 or 2 
# no node has a single child

#  COMPLETE BINARY TREE
#  all levels except possibly the last are complety filled
#   nodes in the last level are filed from left to right 


#  PERFECT BINARY TREE
# 1. all internal nodes have exactly two nodes
#  2.  all  leafes nodes are at the same level

class Tree:
    def __init__(self,data):
        self.data = data                        #instance variable
        self.children = []
    
    def addChild(self,child):
        self.children.append(child)

    def __str__(self,level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret+=child.__str__(level+1)              #recursive call
        return ret


rootNode=Tree("N1")
N2 = Tree("N2")
N3 = Tree("N3")
N4 = Tree("N4")
N5 = Tree("N5")
N6 = Tree("N6")
N7 = Tree("N7")
N8 = Tree("N8")
N10 = Tree("N10")

#add child nodes in tree


rootNode.addChild(N2)
rootNode.addChild(N3)

N2.addChild(N4)
N2.addChild(N5)

N3.addChild(N6)
N3.addChild(N7)

N4.addChild(N8)
N4.addChild(N10)

print(rootNode)

#  depth dirst search
#  1 preorder traversal 
#  2 inorder traversal
#  3 post order traversal
 