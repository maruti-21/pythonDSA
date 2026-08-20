import sys
class CURD:
    def __init__(self):
        print("STUDENT NAME SYSTEM")
        self.student_id = []
        self.student_name = []
        self.student_city = []
        self.student_rollno = []
        
    def add_student(self):
        self.student_id.append(input("enter your ID:"))
        self.student_name.append(input("enter your name:"))
        self.student_city.append(input("enter the city:"))
        self.student_rollno.append(input("enter rollno.:"))
        
    def update_student(self):
        id = input("enter your ID to update:")
        if id in self.student_id:
            index = self.student_id.index(id)
            self.student_name[index] = input("enter new name:")
            self.student_city[index] = input("enter new city:")
            self.student_rollno[index] = input("enter new rollno:")
            print("Student updated successfully!")
        else:
            print("Student ID not found!")
        
    def show_student(self):
        if not self.student_id:
            print("No students to show!")
            return
        print("Student Details:")
        for i in range(len(self.student_id)):
            print(f"ID: {self.student_id[i]}, Name: {self.student_name[i]}, City: {self.student_city[i]}, Roll No: {self.student_rollno[i]}")
        
    def delete_student(self):
        id = input("enter your ID to delete:")
        if id in self.student_id:
            index = self.student_id.index(id)
            del self.student_id[index]
            del self.student_name[index]
            del self.student_city[index]
            del self.student_rollno[index]
            print("Student deleted successfully!")
        else:
            print("Student ID not found!")
        
    def exit(self):
        print("Chal milte hai fir kabhi...")
        sys.exit()
        
obj = CURD()
while True:
    print("1. Add\n2. Update\n3. Show\n4. Delete\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        obj.add_student()
    elif choice == '2':
        obj.update_student()
    elif choice == '3':
        obj.show_student()
    elif choice == '4':
        obj.delete_student()
    elif choice == '5':
        obj.exit()
    else:
        print("Invalid choice! Please try again.")

    
