name="prashant jha"
print(name)
myname=list(name)
print(myname)
print(type(name))
print(type(myname))


#  for reverse 
mylist=[1,2,3,4,5]
print(mylist)
mylist.reverse()
print(mylist)
# mylist.count(9)
# print(mylist.count(2))

#  for sorting the list
# list shoould be in same data type for sorting
# in python 2 we can sort the list with different data type but in python 3 we can't sort the list with different data type because it will give error. so we have to sort the list with same data type.


mylist=[5,4,3,2,1]
print(mylist)
mylist.sort() # reverse= True for sorting in descending order
print(mylist)
mylist.sort(reverse=True)
print(mylist)