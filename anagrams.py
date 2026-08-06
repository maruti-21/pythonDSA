def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

# Test
print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))
print(are_anagrams("evil", "vile")) 

a = "listen"
b = "silent"
if sorted(a) == sorted(b):
    print("anagrams.")
else:
    print(" not anagrams.")
    
str1="these is a sentence"
count=1
for i in str1:
    if i==' ':
        count+=1
print(count)
print(len(str1))


