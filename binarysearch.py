
def BinarySearch(array,target):
    low=0
    high=len(array)-1
    while low<=high:
        mid=(low+high)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

array=[1,2,3,4,5,6,7,8,9]
target=55
result=BinarySearch(array,target)
if result==-1:
    print("element not found")
else:
    print("element found at index",result)
