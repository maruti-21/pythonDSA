import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["StudentID","rollno","name","mobileno"])

StudentID=int(input("enter your student id:"))
rollno= int(input("enter your roll no:"))
name= input("enter your name:")
mobileno= int(input("enter your no.:"))
a.writerow([StudentID,rollno,name,mobileno])
print("student record has save")
