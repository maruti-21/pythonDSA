#wap for menu driven code while loop is used spl for user can acess it infinite time 
import sys
def add():
    val1=int(input("enter the no."))
    val2=int(input("enter the no."))
    print("add=",val1+val2)
 
def sub():
    val1=int(input("enter the no."))
    val2=int(input("enter the no."))
    print("sub=",val1-val2) 

def mul():
    val1=int(input("enter the no."))
    val2=int(input("enter the no."))
    print("mul=",val1*val2)
    
def div():
    val1=int(input("enter the no."))
    val2=int(input("enter the no."))
    print("div=",val1/val2)


while True:
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.exit")
    choice=int(input("enter your choice:"))
    
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
         mult()
    elif choice==4:
        div()
    elif choice==5:
        exit()
    
    
    
    
  