# def capitalizefirst(arr):
#     result=[]
#     if len(arr)==0:
#         return result
    
    
#     result.append(arr[0][0].upper()+arr[0][1:])   #T+aco=Taco 
#     return result
# print(capitalizefirst(['car','tobacco','banana']))




# def productofarray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0]* productofarray(arr[1:])

# print(productofarray([1,2,3]))
# print(productofarray([1,2,3,10]))

#fibonaccci series


def fib(num):
    if (num<2):
        return num
    return fib(num-1)+fib(num-2)

print(fib(4))
print(fib(10))