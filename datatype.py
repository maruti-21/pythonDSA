# collection of data types in python
# 1. int
# 2. float
# 3. str
# 4. bool
# 5. list
# 6. tuple
# 7. set
# 8. dict

# ====================

mylist=["apple", "banana", "cherry","mango", "grapes", "orange", "kiwi", "watermelon", "pineapple", "papaya", "strawberry", "blueberry", "raspberry", "blackberry", "peach", "pear", "plum", "apricot", "nectarine", "grapefruit","89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
print(mylist)
print(type(mylist))
print(len(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[-4])
print(mylist[-3])
print(mylist[-2])
print(mylist[-1])
print(mylist[0:5])
print(mylist[5:10])
print(mylist[10:15])
print(mylist[15:20])
print(mylist[20:25:2])
print(mylist[:])
print(mylist[::-1])

mylist.append("guava")
print(mylist)
mylist.insert(13, "avocado")
print(mylist)
mylist.remove("banana")
print(mylist)
mylist.pop()
print(mylist)
mylist[2]="grapes"
print(mylist)
mylist.__add__(["watermelon", "pineapple"])
print(mylist)
mylist.reverse()
print(mylist)


