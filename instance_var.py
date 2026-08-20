class new:
    def __init__(self):
        self.a=10
        
obj1=new()
obj2=new()
obj3=new()
print(obj1.a)
print(obj2.a)
print(obj3.a)
obj1.a=20
print()
print(obj1.a)
print(obj2.a)
print(obj3.a)

# where we declare the instance variable
# inside the constructor , outside a class by using obj
class Student:
    def __init__(self):
        self.s_name="prashant"
        self.s_rollno="101"   #declaring instance var in side the constructor
        
    def getdata(self):
        self.s_mb=276345276  # declare a var in side the instance method
        
obj=Student()
obj.getdata()
del obj.s_mb   #del the instance var using obj
obj.s_branch="me"   #adding instance var by using object
print(obj.__dict__)


