list=int(input("enter the size"))
even=[]
odd=[]
for i in range(list):
    a=int(input("enter a no."))
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
print(even+odd)
    