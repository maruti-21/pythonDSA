# name = "racear"
# for i in name:
#     print(i)
# Check if there are duplicates
# iflen(name) != len(set(name)):
#     # Remove duplicates while preserving order
#     unique_name = ''.join(dict.fromkeys(name))
#     print(f"Duplicates removed: {unique_name}")
# else:
#     print("No duplicates found.")



name="racear "
newname=" "
for i in name:
    if i not in newname:
        newname+=i
print(newname)
print(len(name))
print(name)