# run time is expecption handling i.e ru time error ko handle karna
# n1=int(input("enter 1st value"))
# n2=int(input("enter 2nd value"))
# try:
#     print(n1/n2)
# except:
#     print("shana mat ban")
# print("to be continue") 


# try:
    
#     n1=int(input("enter 1st value:"))
#     n2=int(input("enter 2nd value:"))
    
#     print(n1/n2)
# except ZeroDivisionError:
#     print("shana mat ban")
# except ValueError:
#     print("enter your value,value error")


# we can handle multiple error in single exception Error
# try:
#     n1=int(input("enter 1st value:"))
#     n2=int(input("enter 2nd value:"))
    
#     print(n1/n2)
# except (ZeroDivisionError,ValueError)as message:
#     print(message)

# try:
#     n1=int(input("enter 1st value:"))
#     n2=int(input("enter 2nd value:"))
    
#     print(n1/n2)
# except (ZeroDivisionError,ValueError)as message:
#     print("Enter correct number:",message)
    
# except:
#     print("this is default part of except block")

# try:
#     n1=int(input("enter 1st value:"))
#     n2=int(input("enter 2nd value:"))
    
#     print(n1/n2)
# except (ZeroDivisionError,ValueError)as message:
#     print("Enter correct number:",message)
# else:
#     print("everything is ok")
    
# final block is the only block is always executed wherther try block generate or not
# why it is use becoz there is should be connection and close perfectly,internally data should not be affected!

# try:
#     n1=int(input("enter 1st value:"))
#     n2=int(input("enter 2nd value:"))
    
#     print(n1/n2)
# except (ZeroDivisionError,ValueError)as message:
#     print("Enter correct number:",message)
# finally:
#     print("I will allways executed")
    
# nested try except block 
# try:
#     n1=int(input("enter 1st value:"))
#     n2=int(input("enter 2nd value:"))
#     try:
#         print(n1/n2)        
#     except ZeroDivisionError as message:
#          print(message)
# except ValueError as message:
#     print(message)
    
try:
    n1=int(input("enter 1st value:"))
    n2=int(input("enter 2nd value:"))
    print(n1/n2)
except (ZeroDivisionError,ValueError) as message:
    print(message)    
else:
    print("there are no error in try block")
finally:
    print("i am finally block i will always exceuted wheather is it error or not")