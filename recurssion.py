# def poweroftwo(n):
#     if n==0:
#         return 1
#     else:
#         power=poweroftwo(n-1)
#     return power*2
    
    
# def poweroftwo(n):
#     i=0
#     power=1
#     while i<n:
#         power=power*2
#         i=i+1
#     return power

#factorial solutioon
def fact(num):
    if num<=1:
        return 1
    return num*fact(num-1)

print(fact(5))