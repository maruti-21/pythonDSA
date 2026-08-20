# dict represented by{key:value} paranthesisi
# duplicate keys are not allowed 
# duplicate values are  allowed
# dict by nature is muttable
# it is unordered data 
mydict={
    101:"prashant",
    102:"kumar",
    103:"singh",
    104:"yadav",
    "102":"kumar",
    "103":"dubey",
    103:"patil"
    
}
print(mydict)


# with the help of key we have to print values
a=mydict["102"]
print(a)

# we will replace the order value
mydict["102"]="peter"
print(mydict)

#  to print only key
for x in mydict:
    print(x)  #we wil use (x)
    
# to print values x=0
for x in mydict.values():
    print(x)
    
# for printing both values and keys
for x in mydict.items():
    print(x)
    
# if i have to add new key and value pair in my dict
mydict["mobile_no"]="2345678"
print(mydict)

# to remove the content in the dict.
mydict={101:"prasthantdeveloper","email":101}
mydict.pop(101)
print(mydict)


# mcq on dict

a={(1,2):1,(2,3):2,(4,5):3}
print(a[4,5])
# result=3

# a={'a':1,'b':2,'c':3}
# print(a['a','b'])
# result error beacuse there is , in the print whih is value error
arr={}
arr[1]=1
arr['1']=2
arr[1]+=1
sum = 0
for k in arr:
    sum+=arr[k]
print(sum)

my_dict={}
my_dict[1]=1
my_dict['1']=2
my_dict[1.0]=4
sum = 0
for k in my_dict:
    sum+=my_dict[k]
print(sum)


my_dict={}
my_dict[(1,2,4)]=8
my_dict[(4,2,1)]=10
my_dict[(1,2)]=12
sum=0
for k in my_dict:
    sum+= my_dict[k]
print(sum)
print(my_dict)


# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# jars['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))
# result is error

dict={'c':97,'a':96,'b':98}
for _ in sorted(dict):
    print(dict[_])
# this will sorted using alphabetically

rec={"name":"python","age":"20"}
r=rec.copy()
print(id(r)==id(rec))
print(id(r))
print(id(rec))

# result is false because copy is udes to copy the content not the address
rec={"name":"python","age":"20","nj":"company"}
id1=id(rec)
del rec
rec={"name":"python","age":"20","nj":"company"}
id2=id(rec)
# del(id)
print(id1==id2)
print(id1)
print(id2)


# wap to find the key with the minimum value in a dict,.


mydict = {"x": 20, "y": 10, "z": 30}

min_key = min(mydict, key=mydict.get)
max_key = max(mydict, key= mydict.get)
print("Key with minimum value:", min_key)
print("Minimum value:", mydict[min_key])
print("Key with maximum value:", max_key)
print("Maximum value:", mydict[max_key])


