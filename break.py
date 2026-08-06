for i in range(1,5):
    if i==3:
        break
    print(i)
    
    
for i in range(1,5):
    if i==3:
        continue
    print(i)

# task
# for i in range(1,6):
#     if i%3==0:
#         continue

#     print(i)
 
#zip()in python is used to combine two or more iterables (like lists, tuples, etc.) into a single iterable of tuples. Each tuple contains one element from each of the input iterables, paired together based on their positions. The resulting iterable will have a length equal to the shortest input iterable.
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i,j)
    
# WAP to move
# input= prashant*is*a*good*programmer
# output = ****prashantisagoodprogrammer

name=  "prashant*is*a*good*programmer"
newname=''
val=''
for i in name:
    if i!='*':
        newname+=i
    else:
        val+=i
print(newname)
print(str(val+newname))

name = "sudarshan*is*a*good*programmer"
newname = ""
for i in name:
    if i == "*":
        newname += "*"
print(newname + name.replace("*",""))
print(newname)

a=50
b=30
c=20
d=10
print((a+b)*c/d)
print((a-b)*c/d)
print(a+(b*c)/d)

x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]
print(z==y)
print(y==z)
print(x!=z)
print(id(x))
print(id(y))
