import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["StudentID","rollno","name","mobileno","percentage","p1","p2","p3","total"])

StudentID=int(input("enter your student id:"))
rollno= int(input("enter your roll no:"))
name= input("enter your name:")
mobileno= int(input("enter your no.:"))
p1=int(input("enter your p1 marks:"))
p2=int(input("enter your p2 marks:"))
p3=int(input("enter your p3 marks:"))
total=p1+p2+p3
percentage=(((p1+p2+p3)/300)*100)
if p1>=40 and p2>=40 and p3>=40:
    print("pass")
else:
    print("fail")
    
a.writerow([StudentID,rollno,name,mobileno,p1,p2,p3,total,percentage])
print("student record has save")