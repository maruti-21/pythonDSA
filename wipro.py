# count repetitive digits and find security key if no repetitive digits are there print -1 as security key
a = [5,7,8,3,7,8,9,2,3]
b = {}
print(a)
count = 0
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
print(b)
for key, value in b.items():
    if value > 1:
        count += 1
if count > 0:
    print("Security key is: ", count)
else:
    print("Security key is: -1")
    
    
list1=[1,2,2,3,4,3,5]
def countfrequency(list1):
    freq = {}
    for element in list1:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    count = 0
    for key in freq:
        if freq[key] > 1:
            count += 1
    return count if count > 0 else -1

print("the security key is :", countfrequency(list1))

