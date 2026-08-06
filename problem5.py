for i in range(5,0,-1):
    print(i)
# here we are using range function with 3 parameters, first one is starting point, second one is ending point and third one is step. here we are starting from 5 and ending at 0 and step is -1, so it will print 5,4,3,2,1.
for i in range(10,0,-2):
    print(i)
# here we are starting from 10 and ending at 0 and step is -2, so it will print 10,8,6,4,2.


#wap to reverse this string using for loop
# method1
reverse="mumbai"
for i in reverse:
    reverse+=i+reverse
print(reverse)
# method2
name="mumbai"
newname=""
n=len(name)
for i in range(n-1,-1,-1):
    newname+=name[i]
print(newname)


