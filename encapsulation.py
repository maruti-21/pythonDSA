class Base:
    def __init__(self):
        print("parent class constructor called")
        self.a="prashant"
        self.__c= "Ashish"
class Derived(Base):
    def __init__(self):
        Base.__init__(self) 
        # print("calling private menber of class")
        # print("self.a")
        # print(self.__c)

obj1=Derived()
print(obj1.a)
print(obj1.__c)
obj2=Derived()
print(obj2.a)
print(obj2.__c)

