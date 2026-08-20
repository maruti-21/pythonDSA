# to handle overloaded method in python
# handle with default agrument x
class arithmatic:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None:
            print(a+b)
        elif a!= None and b!=None and c!=None:
            print(a+b+c)
        else:
            print("enter your atleat 2 argument")
obj=arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(1,2,3)

# ===================================================================================#

class arithmatic:
    def __init__(self):
        print("there is no argument")
    def __init__(self, a):
        print("passing one argument")
    def __init__(self,a,b):
        print("passing two arguments")
        
obj=arithmatic()
obj=arithmatic(10)
obj=arithmatic(2,2)
