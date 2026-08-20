d = {"c": 3, "b": 2, "a": 1}

sorted_dict = dict(sorted(d.items()))

print(sorted_dict)


def delete_key(d, key):
    if key in d:
        del d[key]
    return d

# Example
d = {"a":1, "b":2, "c":3}
print(delete_key(d, "b"))


# ============================================================#

def countSpecialCharacters(string):
    special_characters = "!@#$%^&*()_+-=~`|\\:;\"'<>,.? /"
    count = 0
    for char in string:
        if char in special_characters:
            count += 1
    return count

string = input("enter the string to count")
print(countSpecialCharacters(string))



# ======================================================#

import math

arr = list(map(int, input("Enter numbers (space separated): ").split()))

for i in arr:
    root = int(math.sqrt(i))
    if root * root == i:
        print(root) 
        
