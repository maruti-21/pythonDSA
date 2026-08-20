    # WAP to reverse the order of elements in a list

list = [1, 2, 3, 4, 5]
new = []
for i in list:
    new.insert(0, i)

print("Original list:", list)
print("Reversed list:", new) 

# WAP fuction to check palindrome

list=[1,2,3,2,1]
print(list)
print(list[::-1])
if list == list[::-1]:
    print("it is palindrome")
else:
    print("it is not palindrome")
    
# WAP to call common value in list

list=[1,2,3,4]
new=[3,4,5,6]
common = [x for x in list if x in new]
print("Common values:", common)
