# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end="  ")
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="  ")
#     print()
    
# n=int(input("enter your rows:"))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i),end=" ")
#     print()
    
# n=int(input("enter your rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()

# n=int(input("enter your rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+i),end=" ")
#     print()
    
# n=int(input("enter your rows:"))
# import time
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(1)
#         print(n+1-i,end=" ")
#     print()


import time
n=int(input("enter ur no. rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        time.sleep(2)
        print("*",end=" ")
    print()
    
