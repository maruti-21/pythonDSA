names=[7,3,4,5,6,7]
for i in names:
    print(i)
# wap to assign the valus 0 in end position

a=[4,0,2,5,0,1]
for i in a:
    if i==0:
        a.remove(i)
        a.append(i)
print(a)


list1=[1,2,3,4,4,5]
newlist=[]
for i in list1:
    if i not in newlist:
        newlist.append(i)
print(newlist)

list1=[1,2,3]
list2=[2,3,4]
list3=[3,4,5]
for i in list1:
    if i in list2 and i in list3:
        print(i)

        
# array=[10,11,7,12,14]
# sum=0
# len_array=len(array)
# print(len_array)
# for i in range(0,5):
    
    
n= int(input("enter the array"))
arr=[]
for i in range(0,n):
    val=int(input("enter the value"))
    arr.append(val)
print(arr)
sum=0
for i in range(0,n):
    if i+1 < n:  # Ensure we don't go out of bounds
        sum+=abs(arr[i]-arr[i+1]) #abs() function is used to get the absolute value of the difference between two numbers
        
    
print(sum)
        
