# 1
# pop always retur the last element of the list and removes it from the list
from tkinter.messagebox import IGNORE


arr=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,3):
    print(arr[i].pop())
    
# 2
arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
print(arr)
# 3
a=[1,2,3,4,5,6]
a[::2]=10,20,30,40,50,60
print(a)
# 4
a=[1,2,3,4,5,6]
print(a[3:0:-1])
