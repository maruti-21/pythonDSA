list=[1,2,2,3,4,2]
print(list)
n=int(input("enter your element"))
for i in list:
    if  i==n:
        list.remove(i)
print(list)


def cal():
    n1 = int(input("enter your value:"))
    n2 = int(input("enter your value:"))
    n3 = int(input("enter your value:"))
    n4 = int(input("enter you valule:"))
    result = n1 * n2 * n3 * n4
    return result

print(cal())
    