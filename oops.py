class Student:
    roll_no = 101

    # Use a method inside the class, defined with def()
    def studentData(self):
        print("student information")

obj = Student()  # create an instance of the class
print(obj.roll_no)
obj.studentData()


