def linearsearch(Array,target):
    for i in range(len(Array)):
        if Array[i]==target:
            
             return i
    return -1
Array=[1,2,3,4,5,6,7,8,9]
target=56
result= linearsearch(Array,target)
if result==-1:
    print("not found")
else:
    print ("element found")