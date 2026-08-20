class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head = None
        
linkedlist=linkedlist()


linkedlist.head=Node(5)    # FIRST HEAD 
second         = Node(10)
third          =Node(15)
fourth          = Node(20)
#linking part
linkedlist.head.next=second
second.next=third
third.next= fourth

print(linkedlist.head.data)
print(second.data)
print(third.data)
print(fourth.data)
#display part

while linkedlist.head!=None:
    print("|",linkedlist.head.data ,"|",linkedlist.head.next,"->",end=" ")
    linkedlist.head=linkedlist.head
    

