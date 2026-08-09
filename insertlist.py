# f= open("myfile.txt","w")
# mylist=["prashant ","mahesh ","suresh "]
# dict={"prashant ","mahesh ","suresh "}
# tuple=("hyy ","mahesh ","suresh ")
# f.writelines(mylist)
# f.close()
# print("written works has done successfully")


# f=open("myfile.txt","r")
# print(f.read())
# f.close()

# using with statement block
with open("myfile.txt","w") as f:
    f.write("amit\n")
    f.write("hero\n")
    f.write("rohit\n")
    print("file closed :",f.closed)
print("file closed:",f.closed)


with open("myfile.txt","r") as f:
    content=f.read()
    print(content)
    
f1=open("image.jpg","rb")
f2=open("shana.jpg","wb")
data=f1.read()
f2.write(data)
print("new image is available with the name:")