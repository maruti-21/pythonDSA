class Demo:
    def __init__(self):
        print("I am a constructor:")
        
    def msg(self):
        print("hello class!")
        
obj1 = Demo()
print(obj1)
obj2 = Demo()
obj1.msg()
# there is only two constructor 1.default 2.parameter

class HOD:
    def __init__(self):
        self.name='prashant jha'
        self.age=53
        self.empid=1001
    def info(self):
        print("my name is :",self.name)
        print("my age is :",self.age)
        print("my emp id:",self.empid)
obj=HOD()
obj.info()


# parameterize constructor
class HOD:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
        
    def show(self):
        print('name=',self.name)
        print('age=',self.age)
        print('rollno',self.rollno)
obj=HOD('Arjun','45','1001')
obj.show()