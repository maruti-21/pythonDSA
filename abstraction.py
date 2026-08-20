#we have to use [import] in abstract 
from abc import ABC , abstractmethod
class help4code(ABC):
    def training(self):
        pass
    
    def placement(self):
        pass
    
class Ashish (help4code):
    def training(self):
        print('c,c++,java')
    def placement(self):
        print("java plancement")
        
class Ankush(help4code):
    def training(self):
        print("python| djngo")
    def placement(self):
        print("python placement students")
        
class prashant(help4code):
    def training(self):
        print("machine learning")
    def placement(self):
        print("data science")
        
obj1=Ashish()
obj1.training()
obj1.placement()

obj2=Ankush()
obj2.training()
obj2.placement()

obj3=prashant()
obj3.training()
obj3.placement()

#===========================#==================================#
from abc import ABC, abstractmethod   
class Irctc(ABC):#abstract class  
  
    @abstractmethod  
    def bookTicket(self): # abstract method  
        pass  
  
class MakeMyTrip(Irctc):  
  
    def bookTicket(self):  
        print( "  ==========================================")  
        print("    Welcome To makemytrip   ")  
        source      = input("Enter a source station name")  
        destination = input("Enter destination name")  
        date        = input("Enter date")  
        print( "  ==========================================")  
          
class GoIbibo(Irctc):  
      
    def bookTicket(self):  
        print("    Welcome To GOIBIBO")  
        source      = input("Enter a source station name")  
        destination = input("Enter destination name")  
        date        = input("Enter date")  
  
class Yatra(Irctc):  
      
    def bookTicket(self):  
        print("    Welcome To Yatra  ")  
        source      = input("Enter a source station name")  
        destination = input("Enter destination name")  
        date        = input("Enter date")  
  
m = MakeMyTrip()  
m.bookTicket()  
g = GoIbibo()  
g.bookTicket()  
y = Yatra()  
y.bookTicket()

