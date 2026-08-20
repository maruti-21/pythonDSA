# # there are 3 types 
# 1. class
# 2. static 
# 3. instance

# ++++++++++++++++++++++++++++++++++++++++++++++ 

# instannce method
class Student:
    def __int__(self,name,rollno,mob):
        self.name=name
        self.rollno=rollno
        self.mob=mob
        
    def display(self):
        print(self.name,"",self.rollno,"",self.mob)
        
stud = Student("prashant",1001,23456789)
stud.display()
        
        