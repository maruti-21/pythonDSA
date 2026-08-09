# WAP TO CHECK IF A KEY IS PRESENT OR NOT

# dict1= {"name": "alice"}
# dict2={"age": "20"}
# print("dict1+dict2 is :",dict1,dict2)


list1=[1,2,2,3,4,3,5]
def countfrequency(list1):
    freq={}
    for element in list1:
        if element  in freq:
            freq[element]+=1
        else:
            freq[element]=1
    return freq
print(countfrequency(list1))
            
    


