# Extending property form one class to another class is called inheritance
# directyly we are getting here reusability concept
# 1. base class:-- a class which inherits its property to another is called base class or parent class
# 2. a class in which properties are inherited or derived 
# types -
# 1. single
# 2. multi level
# 3. multiple
# =====================================================================#
# single level inheritance

class college:
    def college_name(self):
        print("modern college")
class student(college):
    def student_info(self):
        print("name:  prashant jha")
        print("branch:   mechanical")
obj=student()
obj.college_name()
obj.student_info()

# ==========================================================================#

# multilevel inheritance

class college:
    def college_name(self):
        print("modern college")
class student(college):
    def student_info(self):
        print("name: jha")
        print("branch:  mechanical")
        
class exam(student):
    def subject(self):
        print("subject1:design engineer")
        print("subject2:math")
        print("subject3:c-language")
obj=exam()
obj.college_name()
obj.student_info()
obj.subject()

# ============================================================== #

class subjmarks:
    math=int(input("enter your marksof maths:"))
    DE=int(input("enter your marksof DE:"))
    c=int(input("enter your marksof c:"))
    eng=int(input("enter your marksof eng:"))
    
class practmarks:
    cprat= int(input("enter practcal marks of c :"))
    
class result(subjmarks,practmarks):
    
    def total(self):
        
        if self.math>=40 and self.DE>=40 and self.eng>=40 and self.cprat>=20:
         print("pass")
        else:
         print("fail")
obj=result()
obj.total()
        