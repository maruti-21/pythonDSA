import sys
class node:
    def __init__(self,data):
        self.data=data
        self.next= None
        
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        
#add node










if__name__=='__main__':
    object=linkedlist()# linkedlist object created

while True:
    print('1. add anode linkedlist :')
    print('2. add node in begining')
    print('3. add nide in between ')
    print('4. add node in end   :')
    print('5.  display the linkedlist: ')
    print('6.   exit: ')
    
    ch=int(input('enter your choice:'))
    if ch==1:
        value=int(input('enter the value for node'))
        object.addnode(value)
        print("")