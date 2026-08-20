# # import re 
# # count = 0
# # # print(pattern)
# # matcher=re.finditer("Hi","HiHii")
# # # print(matcher)
# # for i in matcher:
# #     count+=1
# #     print(i.start(),"...",i.end(),"...",i.group())
# # print("the number of occurence : ",count)       



# # import re  
# # obj = input("enter any character")  
# # objmatch=re.finditer(obj,"a7b @k9z")  
# # #print(objmatch)  
# # for match in objmatch:  
# #     print(match.start(),"...",match.end(),"...",match.group())
    
# # # match function {it alawys match the starting of the paragraph}


# # import re
# # a= input("enter string to perform match operation :")
# # match=re.match(a,"python is very important language")
# # print(match)
# # if match!=None:
# #     print("match found at begining level")
# #     print(match.start(),"",match.end())
    
# # else:
# #     print("there is no matching at begining level") 
    
# # # fullmatch()

# # # as a name suggest when we have to match full string with the given pattern then we have to use fullmatch(). if match iss done then we get match obj if not it get none

# # import re
# # a= input("enter string to perform match operation :")
# # match=re.fullmatch(a,"python is very important language")
# # print(match)
# # if match!=None:
# #     print("match found")
# #     print(match.start()," ",match.end())
    
# # else:
# #     print("there is no matching at begining level") 
    
# #search function()
#  if we found anywhere in the string then it return object else it eill return none

# import re
# a = input("Enter a string to perform search operation:")
# mtch = re.search(a, "python is very important language")
# print(mtch)
# if mtch != None:
#     print(mtch.start(), " ", mtch.end(), " ", mtch.group())
# else:
#     print("There is no matching")
    
# import re

# text = "python is very important language"

# pattern = input("Enter text to search: ")

# match = re.search(pattern, text)

# if match:
#     print("Match Found!")
#     print("Start:", match.start())
#     print("End:", match.end())
#     print("Matched Text:", match.group())
# else:
#     print("No matching found")

# findall()function
# this function return a list which containing all matches

# import re 
# match = re.findall('[^0-9,A-Z,a-z]',"abcgdgfibf76#$^&hgui567")
# print(match)


# sub()function
# this function perform substitution or replacement re. sub(expression,replacement,string)here every match pattern be replaced by pprovided replacement

# import re
# obj=re.sub('[a-zA-Z]','🐦🐦','2345 AFUA jdkd jspf')
# print(obj)


# subn()- It is as similiar as sub() function only one thing is different that it also return number of replacement. This return intuple where first element is string and second one is number of replacement 
# split()- This function is used to split the given string as per the some pattern then we should use split()
#mukhda tujha mukhda janu chandravani fulala tujhaya rupachacahndan majhya manat ha guntala ra.

# import re
# import re 
# obj = re.subn('[0-7]','@','ab3gd6nkl7')
# print(obj)
# print("The string is =",obj[0])
# print ("The number of replacement is =",obj[1])

# import re
# mo= input("enter the mobile number: +91")
# obj=re.fullmatch("[0-9]\d{9}",mo)
# if obj!=None:
#     print("valid number")
# else:
#     print("invalid number")
    
# import re

# s = input("Enter email id: ")

# pattern = r"\w[a-zA-Z0-9_.]*@(gmail\.com|ybit\.ac\.in)"

# m = re.fullmatch(pattern, s)

# if m is not None:
#     print("Valid email id")
# else:
#     print("Invalid email id")


#WAP to check whether the given file is present or not .
# if yes then print the  content

import sys , os
fname=input("enter the file name:")
if os.path.isfile(fname):
    print("file exists:",fname)
    f=open(fname,"r")
    
else :
    print("file does not exits:",fname)
    sys.exit(0)
print("the content of file is:")
data=f.read()
print(data)
