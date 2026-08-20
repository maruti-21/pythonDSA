class rbi:
    def publicpolicy(self):
        print("check the public policy of RBI")
        
    def _privatepolicy(self):
        print("there is somem private policy which is not accessible for public")
        
class sbi(rbi):
    def __init__(self):  # frist sbi class const called
        rbi.__init__(self)   # second parent class constr called
        
    def callingpublicmethod(self):
        print("\nInside child class")  
        self.publicpolicy()  #calling parent class public method
        
    def callingprivatemethod(self):
        print("\nInside child class")  
        self.privatepolicy()  #calling parent class private method
        
# obj1=sbi()
# obj1.callingpublicmethod()
# obj1.callingprivatemethod()
# # obj1.publicpolicy()
# obj1.__privatepolicy()
obj2=rbi()
obj2.publicpolicy()
obj2.__privatepolicy()
# obj2=rbi()
# obj2.publicpolicy()
# obj2._rbi_privatepolicy()