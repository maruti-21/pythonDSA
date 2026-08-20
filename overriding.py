# # python supports both riding
# 1. method 
# # 2. constructor 

# class rbi:
#     def home_loan(self):
#         print("home loan is 8%")
#     def car_loan(self):
#         print("car loan is 10%")
# class sbi:
#     def home_loan(self):
#         print("home loan of ssbi = 7%")
#         super().home_loan()# by using this we can access the parent class by child class 
# obj= sbi()
# obj.home_loan()

# ===============================================#
# constructor overloading
class father:
    def __init__(self):
        print("father:=i am allready at breakfast table")
class child(father):
    def __init__(self):
        print("child:= i will be late for table")
        
obj=child()
obj=father()